# Use pypy JIT python implementation for better performance.
NUM_TAGS = 200
TAG_LEN = 64
NUM_ITERATION = 2000

import random

def getTag():
    return "".join([str(random.randint(0,1)) for _ in range(TAG_LEN)])
        
def genTags(num):
   tags = []
   for x in range(num):
       tags.append(getTag())
   return tags

def binarySearch(TAGS, prefix):
    slots = 0
    # Do Query
    for i in range (8):
        slots += 1
        # 000, 001, 010, 011...
        addedPrefix = bin(i)[2:].rjust(3, "0")
        # Find if anything matches the cumulative prefix for this slot
        c = doesMatchPrefix(TAGS, prefix + addedPrefix)
        
        if c > 1:
            #Collision!
            slots += binarySearch(TAGS, prefix + addedPrefix)
        elif c == 1:
            #Do we need to fully query the tag? Normally they only send back 8 bits, do we need to get the full id?
            pass
    return slots

def doesMatchPrefix(tags, prefix):
    count = 0
    for t in tags:
        if t.startswith(prefix):
            count += 1
    return count

if __name__ == "__main__":
    results = []
    for i in range(NUM_ITERATION):
        if i % 100 == 0:
            print("%.2f%% Completed" % (float(i) / NUM_ITERATION * 100))
        results.append(binarySearch(genTags(NUM_TAGS), ''))
    print("Slots: %s...\nMean: %.2f" % (results[:10], sum(results)/ len(results)))