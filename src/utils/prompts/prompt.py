from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
from .process_related_causes_types import *

# Get the directory containing prompt.py
PROMPT_DIR = Path(__file__).parent

type_classifier_system_prompt = Path(PROMPT_DIR / "type_classifier.md").read_text(encoding="utf-8")
drug_classifier_system_prompt = Path(PROMPT_DIR / "drug_classifier.md").read_text(encoding="utf-8")
dosage_classifier_system_prompt = Path(PROMPT_DIR / "dosage_classifier.md").read_text(encoding="utf-8")
route_classifier_system_prompt = Path(PROMPT_DIR / "route_classifier.md").read_text(encoding="utf-8")
monitoring_classifier_system_prompt = Path(PROMPT_DIR / "monitoring_classifier.md").read_text(encoding="utf-8")
operational_classifier_system_prompt = Path(PROMPT_DIR / "operational_classifier.md").read_text(encoding="utf-8")

process_related_causes_classifier_system_prompt = Path(PROMPT_DIR / "process_related_causes_classifier.md").read_text(encoding="utf-8")
set1 = "\n".join([inaccurate_medication_history, transcribing_error, others])
set2 = "\n".join([inaccurate_medication_history, transcribing_error, others, wrong_patient])
set3 = "\n".join([inaccurate_medication_history, transcribing_error, others, wrong_patient, labs_or_culture])
set4 = "\n".join([inaccurate_medication_history, transcribing_error, others, affordability])
set5 = "\n".join([not_in_formulary, out_of_stock])
set6 = "\n".join([inaccurate_medication_history, transcribing_error, others, tcu_mismatch])
set7 = "\n".join([transcribing_error, others])
set8 = "\n".join([incompatability, drug_concentration, others])

TYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", type_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

DRUG_SUBTYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", drug_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

DOSAGE_SUBTYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", dosage_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

ROUTE_SUBTYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", route_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

MONITORING_SUBTYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", monitoring_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

OPERATIONAL_SUBTYPE_CLASSIFIER_PROMPT = ChatPromptTemplate.from_messages([
    ("system", operational_classifier_system_prompt),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_1 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set1)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_2 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set2)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_3 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set3)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_4 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set4)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_5 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set5)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_6 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set6)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_7 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set7)),
    ("user", "Documentation: \n {iventDocumentation}")
])

PROCESS_RELATED_CAUSES_PROMPT_8 = ChatPromptTemplate.from_messages([
    ("system", process_related_causes_classifier_system_prompt.format(process_related_causes=set8)),
    ("user", "Documentation: \n {iventDocumentation}")
])