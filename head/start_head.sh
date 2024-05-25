#!/bin/bash

ray start --head \
    --port=6379 \
    --include-dashboard=true \
    --dashboard-host=0.0.0.0 \
    --dashboard-port=8265 \
    --disable-usage-stats \
    --block \
    --verbose