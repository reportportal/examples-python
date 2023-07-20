#!/bin/sh

pytest --reportportal -m "not command_skip" tests -n 4
