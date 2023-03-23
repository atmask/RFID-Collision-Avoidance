
from simulation import run_simulation
import sys
import settings
from reader import BinaryTagReader, GenOneTagReader
from settings import logger

def print_header(text):
    logger.info("#"*(len(text)+5))
    logger.info(f"# {text}  #")
    logger.info("#"*(len(text)+5))

if len(sys.argv) > 1 and sys.argv [-1] == '--debug':
    print_header("BINARY DEBUG SIMULATION")
    run_simulation()
    exit(0)


#############################
# Gen 1 Protocol Simulation
############################

print_header("GEN 1 PROTOCOL")
for s in settings.SAMPLE_SIZES:
    run_simulation(num_tags=s, reader_cls=GenOneTagReader)


#############################
# Binary Tree Protocol Simulation
############################

print_header("BINARY TREE")
for s in settings.SAMPLE_SIZES:
    run_simulation(num_tags=s, reader_cls=BinaryTagReader)

