*** Settings ***
Documentation  Example of a failed keyword expectation

*** Test Cases ***
Expect Error
    Run Keyword And Expect Error    Expected to Fail
    ...                             Fail    Expected to Fail