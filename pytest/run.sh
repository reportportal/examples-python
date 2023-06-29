#!/bin/sh

pytest --reportportal -m "not command_skip" tests
