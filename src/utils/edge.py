from .state import *
from langgraph.graph import END


def route_type_node(state:IventState) -> str:
    """
    Inspects the state after the 'type' node runs 
    and returns the name of the next destination node.
    """
    # Replace 'type_category' with the actual key stored in your State
    type_value = state.type

    mapping = {
        "Drug Selection related" : "drugSubtype",
        "Dosage Regimen related": "dosageSubtype",
        "Route, Site, Diluent, Container, Dilution-related" : "routeSubtype",
        "Monitoring" : "monitoringSubtype",
        "Operational" : "operationalSubtype"
    }

    if type_value in mapping: 
        return mapping.get(type_value) 
    
    raise ValueError(f"Invalid type encountered: {type_value}")

def route_drug_subtype(state: IventState) -> str:
    if state.outcome in ("Rejected", "Uncertain"):
        return END

    subtype_value = state.subtype
    
    mapping = {
        "Stopped Drug - No indication": "processRelatedCausesv2",
        "(Re)Started Drug for Untreated indication - Indication" : "processRelatedCausesv3",
        "Changed Drug or Dosage form or Strength - Efficacy" : "processRelatedCausesv1",
        "Changed Drug or Dosage form or Strength - Safety" : "processRelatedCausesv1",
        "Stopped Drug because of duplicate therapy - Safety" : "processRelatedCausesv2",
        "Changed Drug or Dosage Form because of ADR/Allergy or Contraindication/Precaution or Interaction - Safety" : "processRelatedCausesv1",
        "Changed Drug or Dosage form or Strength for cost savings - Adherence" : "processRelatedCausesv4",
        "Changed Drug or Dosage form or Strength because unavailable - Operational" : "processRelatedCausesv5",
    }

    if subtype_value in mapping:
        return mapping.get(subtype_value)

    raise ValueError(f"Invalid subtype encountered: {subtype_value}")

def route_dosage_subtype(state: IventState) -> str:
    if state.outcome in ("Rejected", "Uncertain"):
        return END
    
    subtype_value = state.subtype

    mapping = {
        "Dose /frequency increased – Efficacy":"processRelatedCausesv1",
        "Rate of infusion increased – Efficacy":"processRelatedCausesv1",
        "Duration or Quantity increased – Efficacy":"processRelatedCausesv6",
        "Dose or Frequency reduced - Safety":"processRelatedCausesv1",
        "Rate of infusion reduced – Safety":"processRelatedCausesv7",
        "Duration or Quantity reduced – Safety":"processRelatedCausesv1",
        "Dose or Frequency changed - Adherence":"processRelatedCausesv1",
        "Dose or Frequency changed for cost savings - Adherence":END,
    }

    if subtype_value in mapping:
        return mapping.get(subtype_value)

    raise ValueError(f"Invalid subtype encountered: {subtype_value}")

def route_route_subtype(state: IventState) -> str:
    if state.outcome in ("Rejected", "Uncertain"):
        return END
    
    subtype_value = state.subtype

    mapping = {
        "Route or site of administration changed – Efficacy":"processRelatedCausesv1",
        "Diluent or dilution or container changed – Efficacy":"processRelatedCausesv8",
        "Route or site of administration changed – Safety":"processRelatedCausesv1",
        "Diluent or dilution or container changed – Safety":"processRelatedCausesv8",
        "Route or site of administration changed - Adherence":END,
    }

    if subtype_value in mapping:
        return mapping.get(subtype_value)

    raise ValueError(f"Invalid subtype encountered: {subtype_value}")