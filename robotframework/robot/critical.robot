*** Settings ***
Documentation    Example using critiacl and non-critical tags

*** Test Cases ***
Critical Passing Test
    [Tags]            smoke
    Log               Critical Passing Test
Not Critical Failing Test
    [Tags]            not_ready
    Log               Not Critical Failing Test
    Should be True    False
