# iventClassification

`iventClassification` classifies free-text clinical pharmacy intervention documentation into a structured medication-intervention record. It is a LangGraph workflow backed by OpenAI chat-model structured output; it is not a trained local machine-learning model.

Given a pharmacist intervention note, the workflow identifies the intervention category and outcome, chooses a category-specific subtype, and—where applicable—assigns an underlying process-related cause. It is intended for standardising pharmacy-review documentation and medication-safety analyses.

## Key features

- Classifies five primary intervention categories: drug selection, dosage regimen, route/site/diluent/container/dilution, monitoring, and operational.
- Produces one of three outcomes: `Accepted`, `Rejected`, or `Uncertain`.
- Assigns one constrained subtype for every primary category.
- Uses conditional LangGraph routing to select the appropriate process-related-cause taxonomy for accepted drug-selection, dosage-regimen, and route-related interventions.
- Enforces response schemas with Pydantic models and `ChatOpenAI.with_structured_output`.
- Includes a local invocation example in `tests/test_graph_local.py` and LangGraph deployment metadata in `langgraph.json`.

## Architecture

The compiled graph is exposed as `src.agent:app`.

```text
intervention note (last message)
            |
            v
  type + outcome classifier
            |
            +--> drug subtype ------+--> applicable process-cause classifier --> end
            +--> dosage subtype -----+--> applicable process-cause classifier --> end
            +--> route subtype ------+--> applicable process-cause classifier --> end
            +--> monitoring subtype -------------------------------------------> end
            +--> operational subtype ------------------------------------------> end
```

If the outcome is `Rejected` or `Uncertain`, drug, dosage, and route branches stop after subtype classification. Some accepted subtypes also end without a process-cause classification, as defined by the routing table in `src/utils/edge.py`.

The workflow uses a single `ChatOpenAI(model="gpt-4o", temperature=0)` instance configured in `src/utils/node.py`. Each graph node combines a Markdown system prompt from `src/utils/prompts/` with structured output constrained by the Pydantic literals in `src/utils/state.py`.

## Repository structure

```text
.
├── src/
│   ├── agent.py                    # Builds and compiles the LangGraph application
│   └── utils/
│       ├── state.py                # State and allowed output labels
│       ├── node.py                 # LLM-backed classification nodes
│       ├── edge.py                 # Conditional graph routing
│       └── prompts/                # Category and process-cause prompt definitions
├── tests/test_graph_local.py       # Local end-to-end invocation example
├── langgraph.json                  # LangGraph graph entry point and .env configuration
├── pyproject.toml                  # Project metadata and direct dependencies
├── requirements.txt                # Fully pinned export of dependencies
├── uv.lock                         # Locked dependency graph for uv
└── graph_visualization.png         # Rendered graph image
```

There are no dataset loaders, preprocessing scripts, model-training routines, model checkpoints, or evaluation-metric implementations in this repository. Input preparation consists of supplying the intervention documentation as a LangChain `HumanMessage`; validation and evaluation must be implemented by the consuming application if required.

## Installation and prerequisites

Prerequisites:

- Python 3.11 or later (the repository currently pins Python 3.12 in `.python-version`).
- An OpenAI API key with access to the configured model (`gpt-4o`).
- `uv` is recommended; `pip` is also supported through the exported `requirements.txt`.

1. Clone the repository and enter it.

   ```bash
   git clone <repository-url>
   cd iventClassification
   ```

2. Create a `.env` file at the repository root:

   ```dotenv
   OPENAI_API_KEY=your_api_key_here
   ```

   `python-dotenv` loads this file when `src.utils.node` is imported. Keep it out of version control; `.env` is already ignored.

3. Install dependencies using one of the following options.

   With uv (recommended):

   ```bash
   uv sync
   ```

   With pip:

   ```bash
   python -m venv .venv
   # PowerShell
   .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

## Quickstart and usage

### Run the included local example

The included script sends a sample intervention note through the compiled graph and prints the resulting state. It makes a live OpenAI API request.

```bash
uv run python tests/test_graph_local.py
```

After a pip-based installation, run:

```bash
python tests/test_graph_local.py
```

### Invoke from Python

```python
from langchain_core.messages import HumanMessage
from src.agent import app

documentation = (
    "History amlodipine 5 mg once daily, but 10 mg once daily was prescribed. "
    "The prescriber confirmed reduction to 5 mg once daily."
)

result = app.invoke(
    {"messages": [HumanMessage(content=documentation)]}
)

print(result)
```

The input is a graph state containing a `messages` sequence. Every classifier reads only the final message (`messages[-1]`), and a missing or empty sequence raises `ValueError`.

The result is a state dictionary with these fields:

```python
{
    "messages": [...],
    "type": "Dosage Regimen related",
    "outcome": "Accepted",
    "subtype": "Dose or Frequency reduced - Safety",
    "processRelatedCauses": "Transcribing error",
}
```

`processRelatedCauses` is optional and can be absent or `None` when its branch is not applicable. Exact output labels are declared in `src/utils/state.py`.

### Serve through LangGraph

`langgraph.json` registers the application as `agent` using `./src/agent.py:app` and points the runtime at `.env`. With the CLI dependency installed, start the local development server from the repository root:

```bash
uv run langgraph dev
```

## Configuration

| Item | Location | Current behaviour |
| --- | --- | --- |
| OpenAI credentials | `.env` | `OPENAI_API_KEY` is required by `ChatOpenAI`. |
| Model and temperature | `src/utils/node.py` | Hard-coded to `gpt-4o` and `0`; edit `_default_llm` to change them. |
| Category, subtype, and outcome labels | `src/utils/state.py` | Pydantic `Literal` types constrain structured responses. |
| Classification instructions | `src/utils/prompts/*.md` | Markdown system prompts define the decision rules. |
| Process-cause options | `process_related_causes_types.py`, `state.py`, and `edge.py` | Eight context-specific cause sets are selected by subtype. |
| LangGraph entry point | `langgraph.json` | Exposes `src.agent:app` as `agent`. |

## Data preparation, training, and evaluation

This codebase does not provide commands for dataset preparation, training, or batch evaluation. It performs inference directly against the configured OpenAI model. To evaluate it, provide labelled intervention notes externally, invoke `app` for each note, and compare the returned `type`, `outcome`, `subtype`, and (when applicable) `processRelatedCauses` fields with your reference labels.
