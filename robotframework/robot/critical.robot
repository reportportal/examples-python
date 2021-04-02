*** Settings ***
Documentation    Example using critiacl and non-critical tags. To run use:
...              robot --noncritical not_ready robot/critical.robot

*** Test Cases ***
Not Critical Failing Test
    [Tags]            not_ready
    Log               Not Critical Failing Test
    Should be True    False
