
from simulation import run_simulation
import sys
import settings
from reader import BinaryTagReader, GenOneTagReader
from settings import logger
from plotter import Plot

def print_header(text):
    logger.info("#"*(len(text)+5))
    logger.info(f"# {text}  #")
    logger.info("#"*(len(text)+5))

if len(sys.argv) > 1 and sys.argv [-1] == '--debug':
    print_header("BINARY DEBUG SIMULATION")
    run_simulation()
    exit(0)

plot = Plot(title="NFC Collision Algorithm Comparison", y_label="slots", x_label="tags")

#############################
# Gen 1 Protocol Simulation
############################

x = []
y = []

print_header("GEN 1 PROTOCOL")
for s in settings.SAMPLE_SIZES:
    _, num_slots = run_simulation(num_tags=s, reader_cls=GenOneTagReader)
    x.append(s)
    y.append(num_slots)

plot.add(x,y, settings.GRAPH_COLOURS[0], label="Gen 1 Protocol")

#############################
# Binary Tree Protocol Simulation
############################

x = []
y = []

print_header("BINARY TREE")
for s in settings.SAMPLE_SIZES:
    _, num_slots = run_simulation(num_tags=s, reader_cls=BinaryTagReader)
    x.append(s)
    y.append(num_slots)

plot.add(x,y, settings.GRAPH_COLOURS[1], label="Binary Tree Protocol")



plot.show()
