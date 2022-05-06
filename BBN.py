# 7. Program based on Bayesian Belief Network (BBN)

# !pip install pybbn

from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
from pybbn.generator.bbngenerator import convert_for_drawing
import matplotlib.pyplot as plt
import networkx as nx
import warnings

# from subprocess import STDOUT, check_call
# import os
# check_call(['apt-get', 'install', '-y', 'graphviz-dev'],
#      stdout=open(os.devnull,'wb'), stderr=STDOUT) 
# !pip install pygraphviz


# Declare nodes for BBN
john = BbnNode(Variable(0, "John", ["calls","not_call"]), [0.9, 0.1, 0.05, 0.95])
mary = BbnNode(Variable(1, "Mary", ["calls","not_call"]), [0.7, 0.3, 0.01, 0.99])
earthquake = BbnNode(Variable(2, "Earthquake", ["occurs","not_occur"]), [0.02,0.98])
burglary = BbnNode(Variable(3, "Burglary", ["occurs","not_occur"]), [0.5, 0.5])
alarm = BbnNode(Variable(4,"Alarm", ["triggers","not_trigger"]), [0.95, 0.05, 0.94, 0.06, 0.29, 0.71, 0.001, 0.999])

bbn = Bbn().add_node(john).add_node(mary).add_node(burglary).add_node(earthquake).add_node(alarm) \
        .add_edge(Edge(alarm, john, EdgeType.DIRECTED )) \
        .add_edge(Edge(alarm, mary, EdgeType.DIRECTED )) \
        .add_edge(Edge(burglary, alarm, EdgeType.DIRECTED )) \
        .add_edge(Edge(earthquake, alarm, EdgeType.DIRECTED ))

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    
    graph = convert_for_drawing(bbn)
    pos = nx.nx_agraph.graphviz_layout(graph, prog='neato')

    plt.figure(figsize=(20, 10))
    plt.subplot(121) 
    labels = dict([(k, node.variable.name) for k, node in bbn.nodes.items()])
    nx.draw(graph, pos=pos, with_labels=True, labels=labels)
    plt.title('BBN DAG')

# convert the BBN to a join tree
join_tree = InferenceController.apply(bbn)

# insert an observation evidence
ev = EvidenceBuilder() \
    .with_node(join_tree.get_bbn_node_by_name('Alarm')) \
    .with_evidence('not_trigger', 1.0) \
    .build()

join_tree.set_observation(ev)

# print the marginal probabilities
for node in join_tree.get_bbn_nodes():
    potential = join_tree.get_bbn_potential(node)
    print(node)
    print(potential)
    print('--------------------->')
