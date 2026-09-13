inaccurate_medication_history = """
Causes: "Inaccurate Medication History"
   - Discrepancies between the requested order and external/historical health records (e.g., NEHR, EPIC history, Nursing Home [NH] charts, Dialysis Center records, GP or Private clinic notes).
"""

transcribing_error="""
Causes: "Transcribing error"
   - Discrepancies between doctor's clinical documentation (CDOC plans, progress notes, side remarks) and the generated prescription order.
   - Prescribing incorrect step-down/step-up doses (wrong step-dosing logic).
   - Unintentional isolated duration errors on single drugs (e.g., all chronic meds prescribed for 3 months, but atenolol unintentionally written for 1 month).
"""

wrong_patient ="""
Causes: "Wrong patient"
   - Medication order entered or processed under the incorrect patient profile or account.
"""

labs_or_culture ="""
Causes: "Labs or culture not noted"
   - Prescriber overlooked, missed, or failed to check relevant laboratory parameters, serum levels, or microbiology/culture results prior to writing the order.
"""

affordability ="""
Causes: "Affordability"
   - Financial constraints, high out-of-pocket costs, or patient inability to pay for the prescribed medication.
"""

not_in_formulary ="""
Causes: "Not in formulary"
   - Prescribed drug or specific formulation is not listed on or has been removed from the institution's official drug formulary.
"""

out_of_stock ="""
Causes: "Out of stock"
   - Drug is temporarily unavailable due to supply chain issues, backorders, or pharmacy inventory stockouts.
"""

tcu_mismatch ="""
Causes: "TCU mismatch"
   - Systemic under-duration affecting ALL chronic medications by MORE THAN 14 days compared to the patient's To-Come-Until (TCU) or next clinical review date.
"""

others ="""
Causes: "Other slips and lapses"
   - Any other issues that does not fall into the other categories.
"""

drug_concentration="""
Causes: "Drug concentration"
     - **Triggers:** Adjusting concentration to maintain drug solubility, prevent crystallization, ensure full dose delivery, or preserve therapeutic potency.
     - **Triggers:** Adjusting concentration to prevent fluid overload (e.g., fluid restriction in HF/ESRD), reduce phlebitis/peripheral vein irritation, or avoid infusion toxicity.
"""

incompatability = """
Causes: "Incompatibility"
    - **Triggers:** Physical precipitation, Y-site incompatibility, IV line mixing issues, container leaching 
(e.g., DEHP/PVC issues with nitroglycerin or paclitaxel), or IV solution fluid mismatch (e.g., D5W vs Normal Saline causing drug instability or precipitation).
"""