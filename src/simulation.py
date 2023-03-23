
from tag import BaseTag
from reader import BinaryTagReader
import time
import settings

def run_simulation(num_tags=5000, tag_cls=BaseTag, reader_cls=BinaryTagReader):
    # Create a collection of tags
    tags = [tag_cls() for _ in range(num_tags)]
    tag_reader = reader_cls()

    #Current epoch time
    min_time = int(time.time())
    max_time=min_time + settings.SIMULATED_DURATION

    for t in tags:
        print(f"TIME: {t.generate_time(min_time, max_time)}, tag: {t.id}")

    transmission_map = {}
    for t in tags:
        # transmission_map[t.transmit_time] = [t.id] if not transmission_map.get(t.transmit_time) else transmission_map[t.transmit_time].append(t.id)
        if not transmission_map.get(t.transmit_time):
            transmission_map[t.transmit_time] = [t]
        else:
            transmission_map[t.transmit_time].append(t)
        # print(f"Transmission map: {transmission_map}")

    slots = 0

    for t, tags in transmission_map.items():
        if len(tags) <= 1:
            continue

        print(f"[NEW COLLISION] De-colliding: {tags} at time: {t}")
        slots += tag_reader.manage_collision(tags)
    
    print(f"Total Slots: {slots}")


