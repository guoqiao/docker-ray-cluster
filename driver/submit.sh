#!/bin/bash

ray job submit --address='http://ray_head:8265' --verbose --working-dir . -- python "$@"