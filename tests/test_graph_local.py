import sys
from pathlib import Path

# Adds the project root (iventClassification) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from rich import print as rprint
from src.agent import app
from langchain_core.messages import HumanMessage

def main() -> None:
    documentation = """
    History amlodipine 5mg OM but prescribed 10mg OM. confirmed with prescriber to reduce to 5mg OM
    """

    result = app.invoke({
        "messages": [
            HumanMessage(content=documentation)
        ]
    })

    rprint("Graph result:")
    rprint(result)

    # assert result.get("type") == "Drug Selection related"
    # assert result.get("outcome") == "Accepted"
    # assert result.get("subtype") == (
    #     "Stopped Drug because of duplicate therapy - Safety"
    # )
    # # assert result.get("processRelatedCauses") is not None

    # print("Graph test passed.")


if __name__ == "__main__":
    main()