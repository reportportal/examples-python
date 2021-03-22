#!/bin/sh

# Replace runner variables with your variables
robot --listener robotframework_reportportal.listener \
      --variable RP_UUID:"your_user_uuid" \
      --variable RP_ENDPOINT:"http://localhost:8080" \
      --variable RP_LAUNCH:"Robot Framework" \
      --variable RP_PROJECT:"default_personal" ./robot
