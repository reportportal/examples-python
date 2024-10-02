#!/bin/sh

# Copyright 2024 EPAM Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace variables with your variables
RP_API_KEY="your_rp_api_key"
RP_ENDPOINT="http://localhost:8080"
RP_PROJECT="default_personal"
RP_LAUNCH="Robot Framework Pabot"
RP_LAUNCH_DOC="My test launch"
START_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Extract the launch ID using curl, grep, and sed
RP_LAUNCH_UUID=$(curl --location --request POST "${RP_ENDPOINT}/api/v1/${RP_PROJECT}/launch" \
--header "Authorization: Bearer ${RP_API_KEY}" \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": [
    {
      "key": "key",
      "value": "value"
    }
  ],
  "description": "'"${RP_LAUNCH_DOC}"'",
  "mode": "DEFAULT",
  "name": "'"${RP_LAUNCH}"'",
  "startTime": "'"${START_TIME}"'"
}' | grep -o '"id": *"[^"]*"' | sed 's/"id": *"\([^"]*\)"/\1/')

# Run tests with Pabot
pabot --skiponfailure not_ready \
      --metadata Scope:smoke \
      --listener robotframework_reportportal.listener \
      --variable RP_LAUNCH_UUID:"${RP_LAUNCH_UUID}" \
      --variable RP_API_KEY:"${RP_API_KEY}" \
      --variable RP_ENDPOINT:"${RP_ENDPOINT}" \
      --variable RP_PROJECT:"${RP_PROJECT}" \
      --variable RP_LAUNCH:"${RP_LAUNCH}" \
      ./robot

EXIT_CODE=$?

END_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
# Finish the launch using curl
curl --location --request PUT "${RP_ENDPOINT}/api/v1/${RP_PROJECT}/launch/${RP_LAUNCH_UUID}/finish" \
--header "Authorization: Bearer ${RP_API_KEY}" \
--header 'Content-Type: application/json' \
--data-raw '{
  "endTime": "'"${END_TIME}"'"
}'
exit "${EXIT_CODE}"
