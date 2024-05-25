#!/usr/bin/env python3

import ray
# connect to existing cluster
ray.init(address='auto')

from pprint import pprint
pprint(ray.nodes())

@ray.remote
def f(x):
    import time
    time.sleep(3)
    return x * x

obj_refs = [f.remote(i) for i in range(4)]
pprint(obj_refs)

result = ray.get(obj_refs)
print(result)