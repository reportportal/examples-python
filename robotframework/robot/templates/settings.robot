*** Settings ***
Documentation  Test templates defined through settings
Test Template  Login with invalid credentials should fail

*** Variables ***
${VALID USER}      User
${VALID PASSWORD}  Password

*** Keywords ***
Login with invalid credentials should fail
    [Arguments]                   ${user}              ${password}
    Run Keyword And Expect Error  Invalid credentials  Validate credentials
    ...                           ${user}              ${password}
Validate credentials
    [Arguments]                   ${user}      ${password}
    Should Be Equal               ${user}      ${VALID USER}      Invalid credentials  False
    Should Be Equal               ${password}  ${VALID PASSWORD}  Invalid credentials  False

*** Test Cases ***
Invalid User Name                 invalid          ${VALID PASSWORD}
Invalid Password                  ${VALID USER}    invalid
Invalid User Name and Password    invalid          invalid
Empty User Name                   ${EMPTY}         ${VALID PASSWORD}
Empty Password                    ${VALID USER}    ${EMPTY}
Empty User Name and Password      ${EMPTY}         ${EMPTY}