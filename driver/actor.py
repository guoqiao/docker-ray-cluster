#!/usr/bin/env python3

import ray
# connect to existing cluster
ray.init(address='auto')


@ray.remote
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        self.n += 1

    def read(self):
        return self.n


counter_obj_refs = [Counter.remote() for i in range(4)]
[c.increment.remote() for c in counter_obj_refs]
futures = [c.read.remote() for c in counter_obj_refs]
print(ray.get(futures))  # [1, 1, 1, 1]