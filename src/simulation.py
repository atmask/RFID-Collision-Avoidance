
from tag import BaseTag
from reader import BinaryTagReader
import time
import settings

def run_simulation(num_tags=10, tag_cls=BaseTag, reader_cls=BinaryTagReader):
    # Create a collection fo tags
    tags = [tag_cls() for _ in range(num_tags)]
    tag_reader = reader_cls()

    #Current epoch time
    min_time = int(time.time())
    max_time=min_time + settings.SIMULATED_DURATION

    for t in tags:
        print(f"TIME: {t.generate_time(min_time, max_time)}, tag: {t.id}")

    transmission_map = {}
    for t in tags:
        transmission_map[t.transmit_time] = [t.id] if None else transmission_map[t.transmit_time].append(t.id)
    

    slots = 0

    for _,tags in transmission_map:
        if len(tags) <= 1:
            continue
            
        slots += tag_reader.manage_collision(tags)


