#!/bin/sh

pytest -sv --reportportal -m "not command_skip" -n 2 tests | tee /dev/tty | sed -rn 's/Report Portal Launch UUID: ([^\\r\\n]+)/LAUNCH_UUID=\1/ w launch.env'
