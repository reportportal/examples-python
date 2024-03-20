#!/bin/sh

# Replace runner variables with yours in 'variables.yaml'
robot --skiponfailure not_ready \
      --metadata Scope:smoke \
      --listener robotframework_reportportal.listener \
      --variablefile variables.yaml ./robot
