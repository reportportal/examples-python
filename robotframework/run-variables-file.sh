#!/bin/sh

# Replace runner variables with yours in 'variables.yaml'
robot --noncritical not_ready \
      --listener robotframework_reportportal.listener \
      --variablefile variables.yaml ./robot
