#!/bin/sh

# Replace runner variables with your variables
python -m robotframework_reportportal.post_report \
        --variable RP_API_KEY:"your_rp_api_key" \
        --variable RP_ENDPOINT:"http://localhost:8080" \
        --variable RP_LAUNCH:"Robot Framework Post Report" \
        --variable RP_PROJECT:"default_personal" \
        --variable RP_LAUNCH_ATTRIBUTES:"tag key1:value1 key2:value2" \
        --variable RP_LAUNCH_DOC:"My test launch" ./output.xml
