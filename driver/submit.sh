#!/bin/bash

# working-dir will be zipped as a pkg and upload to ray cluster shm
ray job submit --address='http://ray_head:8265' --verbose --working-dir . -- python "$@"