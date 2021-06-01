*** Settings ***
Documentation  Test templates defined through keyword

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
Invalid Password
    [Template]     Login with invalid credentials should fail
    invalid        ${VALID PASSWORD}
    ${VALID USER}  invalid
    invalid        invalid
    ${EMPTY}       ${VALID PASSWORD}
    ${VALID USER}  ${EMPTY}
    ${EMPTY}       ${EMPTY}
