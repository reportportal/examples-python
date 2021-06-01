*** Settings ***
Library        DataDriver
Test Template  Login with invalid credentials should fail

*** Variables ***
${VALID USER}      User
${VALID PASSWORD}  Password

*** Test Cases ***
Login with user '${username}' and password '${password}'  Default  UserData

*** Keywords ***
Login with invalid credentials should fail
    [Arguments]                   ${username}          ${password}
    Run Keyword And Expect Error  Invalid credentials  Validate credentials
    ...                           ${username}          ${password}
Validate credentials
    [Arguments]      ${username}  ${password}
    Should Be Equal  ${username}  ${VALID USER}      Invalid credentials  False
    Should Be Equal  ${password}  ${VALID PASSWORD}  Invalid credentials  False
