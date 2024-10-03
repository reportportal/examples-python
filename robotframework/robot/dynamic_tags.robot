*** Settings ***
Documentation  Example of setting test tags in runtime
Library        library/Log.py
Library        library/TestCaseId.py

*** Variables ***
${TEST_VARIABLE}  my_test_variable

*** Test Cases ***
Test tag set
    [Tags]  static_tag
    Item Log  INFO               A test with a tag set in runtime
    Set Tags  dynamic_tag
Test no tag
    Item Log  INFO               A test with no tags set
Test set multiple tags
    Item Log  INFO               A test with multiple tags set in runtime
    Set Tags  multiple_tags_one  multiple_tags_two
Test set dynamic Test Case ID
    Item Log  INFO               A test with dynamic Test Case ID generation
    Case Id   dynamic_tags.robot[{scope_var}]
