#pip install pybbn 
from pybbn.graph.dag import Bbn 
from pybbn.graph.edge import Edge, EdgeType 
from pybbn.graph.jointree import EvidenceBuilder 
from pybbn.graph.node import BbnNode 
from pybbn.graph.variable import Variable 
from pybbn.pptc.inferencecontroller import InferenceController 
from subprocess import STDOUT, check_call 
import os 
check_call(['apt-get', 'install', '-y', 'graphviz-dev'],  stdout=open(os.devnull,'wb'), stderr=STDOUT) 
#pip install pygraphviz 
from pybbn.generator.bbngenerator import convert_for_drawing 
import matplotlib.pyplot as plt 
import networkx as nx 
import warnings 
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
ev = EvidenceBuilder().with_node(join_tree.get_bbn_node_by_name('Alarm')).with_evidence('not_trigger', 1.0).build() 
join_tree.set_observation(ev) 
# print the marginal probabilities 
for node in join_tree.get_bbn_nodes(): 
    potential = join_tree.get_bbn_potential(node)  
    print(node) 
