#!/usr/bin/env python3

import utils
import ray
# connect to existing cluster, do not create
ray.init(address='auto')


from pprint import pprint
pprint(ray.nodes())


def multiple(x, y):
    return x * y


@ray.remote
def task(x):
    import time
    import os
    print(os.getcwd())
    # demo how a remote function call other modules
    x = utils.add(1, 2)
    print(f'x is {x}')
    y = multiple(9, 8)
    print(f'y is {y}')
    time.sleep(3)
    return x * x

obj_ref = task.remote(3)
pprint(obj_ref)

result = ray.get(obj_ref)
print(result)