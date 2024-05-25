#!/bin/bash

ray start \
    --address=ray_head:6379 \
    --block \
    --verbose