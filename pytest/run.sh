#!/bin/sh

pytest --reportportal -m "not command_skip" -n 2 tests
