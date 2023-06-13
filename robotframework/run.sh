#!/bin/sh

# Replace runner variables with your variables
robot --skiponfailure not_ready \
      --listener robotframework_reportportal.listener \
      --variable RP_API_KEY:"your_rp_access_token" \
      --variable RP_ENDPOINT:"http://localhost:8080" \
      --variable RP_LAUNCH:"Robot Framework" \
      --variable RP_PROJECT:"default_personal" \
      --variable RP_LAUNCH_ATTRIBUTES:"tag key1:value1 key2:value2" \
      --variable RP_LAUNCH_DOC:"My test launch" ./robot
