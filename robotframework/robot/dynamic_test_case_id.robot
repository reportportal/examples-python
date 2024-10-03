*** Settings ***
Documentation  Example of setting Test Case ID in runtime
Library        library/Log.py
Library        library/TestCaseId.py

*** Test Cases ***
Test set dynamic Test Case ID
    Item Log  INFO               A test with dynamic Test Case ID generation
    Case Id   dynamic_tags.robot[{scope_var}]
