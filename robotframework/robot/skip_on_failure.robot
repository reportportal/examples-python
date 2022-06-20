*** Settings ***
Documentation    Example of using '--skiponfailure' parameter. To run use:
...              robot --skiponfailure not_ready robot/critical.robot

*** Test Cases ***
Skip Failing Test
    [Tags]            not_ready
    Log               Skip Failing Test
    Should be True    False
