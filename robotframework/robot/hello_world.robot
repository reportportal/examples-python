*** Settings ***
Documentation     Example of a sipmple test on Robot Framework, taken from official documentation:
...               http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#space-separated-format
Library           OperatingSystem

*** Variables ***
${MESSAGE}        Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test.
    Log    ${MESSAGE}
    My Keyword    ${CURDIR}

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
