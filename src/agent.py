import sys
from pathlib import Path

# Adds the project root (iventClassification) to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from langgraph.graph import StateGraph, START, END
from src.utils import *

graph = StateGraph(IventState)
graph.add_node("type", typeClassifier)
graph.add_node("drugSubtype", drugSubtypeClassifier)
graph.add_node("dosageSubtype", dosageSubtypeClassifier)
graph.add_node("routeSubtype", routeSubtypeClassifier)
graph.add_node("monitoringSubtype", monitoringSubtypeClassifier)
graph.add_node("operationalSubtype", operationalSubtypeClassifier)

for i in range(1,9):
    graph.add_node(f"processRelatedCausesv{i}", globals()[f"processClassifierv{i}"])

graph.add_edge(START, "type")
graph.add_conditional_edges("type", route_type_node, ["drugSubtype", "dosageSubtype", "routeSubtype", "monitoringSubtype", "operationalSubtype", END])
graph.add_conditional_edges("drugSubtype", route_drug_subtype, ["processRelatedCausesv1", "processRelatedCausesv2", "processRelatedCausesv3", "processRelatedCausesv4", "processRelatedCausesv5", END])
graph.add_conditional_edges("dosageSubtype", route_dosage_subtype, ["processRelatedCausesv1", "processRelatedCausesv6", "processRelatedCausesv7", END])
graph.add_conditional_edges("routeSubtype", route_route_subtype,["processRelatedCausesv1", "processRelatedCausesv8", END])
graph.add_edge("operationalSubtype", END)
graph.add_edge("monitoringSubtype", END)

app = graph.compile()

# Generate PNG bytes and save to a file
# image_data = app.get_graph().draw_mermaid_png()
# with open("graph_visualization.png", "wb") as f:
#     f.write(image_data)