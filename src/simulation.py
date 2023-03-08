
from tag import BaseTag
import time

def run_simulation(num_tags=10, tag_cls=BaseTag):
    # Create a collection fo tags
    tags = [BaseTag() for _ in range(num_tags)]

    #Current epoch time
    min_time = int(time.time())

    for t in tags:
        print(f"TIME: {t.generate_time(min_time)}, tag: {t.id}")

