from typing import Annotated, Literal, Sequence, TypeAlias
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

InterventionType: TypeAlias = Literal[
    "Drug Selection related",
    "Dosage Regimen related",
    "Route, Site, Diluent, Container, Dilution-related",
    "Monitoring",
    "Operational",
]

Outcome: TypeAlias = Literal["Accepted", "Rejected", "Uncertain"]

DrugSubtype: TypeAlias = Literal[
    "Stopped Drug - No indication",
    "(Re)Started Drug for Untreated indication - Indication",
    "Changed Drug or Dosage form or Strength - Efficacy",
    "Changed Drug or Dosage form or Strength - Safety",
    "Stopped Drug because of duplicate therapy - Safety",
    "Changed Drug or Dosage Form because of ADR/Allergy or Contraindication/Precaution or Interaction - Safety",
    "Changed Drug or Dosage form or Strength for cost savings - Adherence",
    "Changed Drug or Dosage form or Strength because unavailable - Operational",
]

DosageSubtype: TypeAlias = Literal[
    "Dose /frequency increased – Efficacy",
    "Rate of infusion increased – Efficacy",
    "Duration or Quantity increased – Efficacy",
    "Dose or Frequency reduced - Safety",
    "Rate of infusion reduced – Safety",
    "Duration or Quantity reduced – Safety",
    "Dose or Frequency changed - Adherence",
    "Dose or Frequency changed for cost savings - Adherence",
]

RouteSubtype: TypeAlias = Literal[
    "Route or site of administration changed – Efficacy",
    "Diluent or dilution or container changed – Efficacy",
    "Route or site of administration changed – Safety",
    "Diluent or dilution or container changed – Safety",
    "Route or site of administration changed - Adherence",
]

MonitoringSubtype: TypeAlias = Literal[
    "Adverse drug reaction or Allergy monitoring -Safety",
    "Drug interactions or Precautions - Safety",
    "Test added to see therapeutic response - Efficacy",
    "Test added for undiagnosed condition – Indication",
    "Remove unnecessary test – Operational",
    "Remove wrong lab test – Operational",
]

OperationalSubtype: TypeAlias = Literal[
    "No original prescription",
    "Missing or Incomplete dosage regimen or signature",
    "Request by patient",
    "Referral or Update to HCP",
]

Subtype: TypeAlias = DrugSubtype | DosageSubtype | RouteSubtype | MonitoringSubtype | OperationalSubtype

class IventState(BaseModel):
    messages: Annotated[Sequence[BaseMessage] | None, add_messages]
    type : InterventionType | None = Field(default=None, description="Primary medication-intervention category.")
    subtype : Subtype | None = Field(default=None, description="Subtype assigned after type classification.")
    processRelatedCauses: str | None = Field(default=None, description="Underlying process-related cause, when applicable.",)
    outcome: Outcome | None = Field(default=None, description="Whether the recommendation was accepted or rejected.")

class TypeClassification(BaseModel):
    """The only fields produced by _type_classifier_chain."""
    type: InterventionType
    outcome: Outcome

class DrugClassification(BaseModel):
    subtype: DrugSubtype = Field(description="Subtype of drug selection related intervention reflecting the specific action recommended to the prescriber.")

class DosageClassification(BaseModel):
    subtype: DosageSubtype = Field(description="Subtype of dosage regimen related intervention reflecting the specific action recommended to the prescriber.")

class RouteClassification(BaseModel):
    subtype: RouteSubtype = Field(description="Subtype of Route, Site, Diluent, Container, Dilution-related intervention reflecting the specific action recommended to the prescriber.")

class MonitoringClassification(BaseModel):
    subtype: MonitoringSubtype = Field(description="Monitoring-related intervention reflecting the specific action recommended to the prescriber.")

class OperationalClassification(BaseModel):
    subtype: OperationalSubtype = Field(description="Subtype of operational-related intervention reflecting the specific action recommended to the prescriber.")

# v1 applies to majority
class ProcessRelatedCausesStateV1(BaseModel):
    processRelatedCauses: Literal[
        "Inaccurate Medication History",
        "Transcribing error",
        "Other slips and lapses",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v2 applies to Stopped Drug - No indication and Stopped Drug because of duplicate therapy - Safety
class ProcessRelatedCausesStateV2(BaseModel):
    processRelatedCauses: Literal[
        "Inaccurate Medication History",
        "Transcribing error",
        "Wrong Patient",
        "Other slips and lapses",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v3 aplies to (Re)Started Drug for Untreated indication - Indication
class ProcessRelatedCausesStateV3(BaseModel):
    processRelatedCauses: Literal[
        "Inaccurate Medication History",
        "Transcribing error",
        "Other slips and lapses",
        "Wrong Patient",
        "Labs or culture not noted",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v4 applies to Changed Drug or Dosage form or Strength for cost savings - Adherence
class ProcessRelatedCausesStateV4(BaseModel):
    processRelatedCauses: Literal[
        "Inaccurate Medication History",
        "Transcribing error",
        "Other slips and lapses",
        "Affordability",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v5 applies to Changed Drug or Dosage form or Strength because unavailable - Operational
class ProcessRelatedCausesStateV5(BaseModel):
    processRelatedCauses: Literal[
        "Not in formulary",
        "Out of stock",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v6 applies to Duration or Quantity increased – Efficacy
class ProcessRelatedCausesStateV6(BaseModel):
    processRelatedCauses: Literal[
        "Inaccurate Medication History",
        "Transcribing error",
        "Other slips and lapses",
        "TCU mismatch",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v7 applies to Rate of infusion reduced – Safety
class ProcessRelatedCausesStateV7(BaseModel):
    processRelatedCauses: Literal[
        "Transcribing error",
        "Other slips and lapses",
        None,
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")

# v8 applies to Diluent or dilution or container changed – Efficacy and Diluent or dilution or container changed - Safety
class ProcessRelatedCausesStateV8(BaseModel):
    processRelatedCauses: Literal[
        "Incompatibility",
        "Drug concentration",
        "Other slips and lapses",
        ] = Field(description="The underlying process-related error or slip that caused the medication event.")