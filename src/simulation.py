
from tag import BaseTag
import time
import settings

def run_simulation(num_tags=10, tag_cls=BaseTag):
    # Create a collection fo tags
    tags = [BaseTag() for _ in range(num_tags)]

    #Current epoch time
    min_time = int(time.time())
    max_time=min_time + settings.SIMULATED_DURATION

    for t in tags:
        print(f"TIME: {t.generate_time(min_time, max_time)}, tag: {t.id}")


    # for each timestamp in the SIMULATED_DURATION
        # check if multiple tags attempted to transmit
        # if yes:
            # collision detection
        # else:
            # continue

