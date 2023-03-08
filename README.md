# RFID-Collision-Avoidance
A repo for the simulation of RFID collision avoidance algorithms in Python

# How to Run
`>>> python3 src`

# Design
Design Psudeo Code:

```python
tags = Tag[200]

min = current_epoch

for t in tags:
    t.generate_time(min, max)


Reader.detect_collisions(Tags)

Reader.binary_tree()



class Reader:

    def __init__(tags):
        self.tags=tags

    def detect_collisions():
        time_interval_map = {'30':[...], '60':[...] ...}

        for t in tags:
            if t.time in current_interval:
                time_intrval_map.append(t)

    def binary_tree():
        init_ptr = 0
        for time_interval in time_interval_map
            if collisions:
                for permutations of 000
                    query(permutation, ptr=init_ptr)

    def query(permutation, ptr):
        if tag.id[ptr] has multiple:
            for permutation of 000:
                query(permutation, ptr+3)
```
        

