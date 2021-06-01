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
