
from simulation import run_simulation
import sys
import settings
from reader import BinaryTagReader, GenOneTagReader
from settings import logger
from plotter import Plot


# Utilitiy for printing the header
def print_header(text):
    logger.info("#"*(len(text)+5))
    logger.info(f"# {text}  #")
    logger.info("#"*(len(text)+5))


def execute(name, title, reader_cls, colour=settings.GRAPH_COLOURS[0], iterations=settings.TEST_ITERATIONS):
    '''
    Run a specified simulation and get the average of the output across iterations
    '''
    y_sum = [0] * len(settings.SAMPLE_SIZES) # Pre-fill with zeroes so we can just add

    print_header(name)

    for _ in range(iterations):
        for i, s in enumerate(settings.SAMPLE_SIZES):
            _, num_slots = run_simulation(num_tags=s, reader_cls=reader_cls)
            # x.append(s)

            # Get the average number of slots across all iterations
            y_sum[i] += (num_slots)

    y_avg = list(map(lambda y: y/iterations, y_sum))
    
    for tags, slots in zip(settings.SAMPLE_SIZES, y_avg):
        logger.info(f"Tags: {tags}\t Total Slots: {slots}")

    plot.add(settings.SAMPLE_SIZES, y_avg, colour, label=title)


# Debug mode for a small sample
if len(sys.argv) > 1 and sys.argv [-1] == '--debug':
    print_header("BINARY DEBUG SIMULATION")
    run_simulation()
    exit(0)


# initialize plot
plot = Plot(title="NFC Collision Algorithm Comparison", y_label="slots", x_label="tags")

# Configure Simultation Suite to run
SIMULATIONS = [
    {
        "name": "GEN 1 PROTOCOL",
        "title": "Gen 1 Protocol",
        "reader_cls": GenOneTagReader
    },
    {
        "name": "BINARY TREE",
        "title": "Binary Tree Protocol",
        "reader_cls": BinaryTagReader
    }
]

# Run the simulations specified
for index, s in enumerate(SIMULATIONS):
    execute(**s, colour=settings.GRAPH_COLOURS[index])


##############################
# Research paper data
##############################
print_header("Research Paper")
x = []
y = []
for x_p,y_p in settings.PAPER_BINARY_PROTOCOL_DATA:
    x.append(x_p)
    y.append(y_p)
    print(f"Tags: {x_p}\t Total Slots: {y_p}")

plot.add(x,y, settings.GRAPH_COLOURS[2], label="Research Paper Binary Protocol")

plot.show()
