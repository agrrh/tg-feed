#!/usr/bin/env bash

TGFEED_INTERVAL=${TGFEED_INTERVAL:-300}

pwd

while true; do
  python main.py
  sleep ${TGFEED_INTERVAL}
done
