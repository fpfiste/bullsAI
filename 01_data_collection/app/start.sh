#!/bin/sh

udevadm control --reload


python3 -m flask run --host=0.0.0.0 --port=7007

sleep infinity
