import logging

# Configure logger
logger=logging.getLogger('logger')
FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

SIMULATED_DURATION=10
SAMPLE_SIZES = [50, 100, 300, 500, 1000, 1500, 2000]