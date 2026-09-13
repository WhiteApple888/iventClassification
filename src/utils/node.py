from .state import *
from .prompts.prompt import *
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

_default_llm = ChatOpenAI(model="gpt-4o", temperature = 0)

_type_classifier_chain =  TYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(TypeClassification)
_drug_subtype_classifier_chain = DRUG_SUBTYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(DrugClassification)
_dosage_subtype_classifier_chain = DOSAGE_SUBTYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(DosageClassification)
_route_subtype_classifier_chain = ROUTE_SUBTYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(RouteClassification)
_monitoring_subtype_classifier_chain = MONITORING_SUBTYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(MonitoringClassification)
_operational_subtype_classifier_chain = OPERATIONAL_SUBTYPE_CLASSIFIER_PROMPT | _default_llm.with_structured_output(OperationalClassification)

_process_related_causes_chain_1 = PROCESS_RELATED_CAUSES_PROMPT_1 | _default_llm.with_structured_output(ProcessRelatedCausesStateV1)
_process_related_causes_chain_2 = PROCESS_RELATED_CAUSES_PROMPT_2 | _default_llm.with_structured_output(ProcessRelatedCausesStateV2)
_process_related_causes_chain_3 = PROCESS_RELATED_CAUSES_PROMPT_3 | _default_llm.with_structured_output(ProcessRelatedCausesStateV3)
_process_related_causes_chain_4 = PROCESS_RELATED_CAUSES_PROMPT_4 | _default_llm.with_structured_output(ProcessRelatedCausesStateV4)
_process_related_causes_chain_5 = PROCESS_RELATED_CAUSES_PROMPT_5 | _default_llm.with_structured_output(ProcessRelatedCausesStateV5)
_process_related_causes_chain_6 = PROCESS_RELATED_CAUSES_PROMPT_6 | _default_llm.with_structured_output(ProcessRelatedCausesStateV6)
_process_related_causes_chain_7 = PROCESS_RELATED_CAUSES_PROMPT_7 | _default_llm.with_structured_output(ProcessRelatedCausesStateV7)
_process_related_causes_chain_8 = PROCESS_RELATED_CAUSES_PROMPT_8 | _default_llm.with_structured_output(ProcessRelatedCausesStateV8)

def typeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _type_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def drugSubtypeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _drug_subtype_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def dosageSubtypeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _dosage_subtype_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def routeSubtypeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _route_subtype_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def monitoringSubtypeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _monitoring_subtype_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def operationalSubtypeClassifier(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _operational_subtype_classifier_chain.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv1(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_1.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv2(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_2.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv3(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_3.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv4(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_4.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv5(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_5.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv6(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_6.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()
    
def processClassifierv7(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_7.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()

def processClassifierv8(state: IventState, config: RunnableConfig) -> IventState:
    if not state.messages:
        raise ValueError("At least one documentation message is required.")

    result = _process_related_causes_chain_8.invoke(
        {"iventDocumentation" : state.messages[-1]},
        config=config
    )
    return result.model_dump()
