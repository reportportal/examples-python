*** Settings ***
Documentation     An example of using before and after hooks
Suite Setup       Log suite setup
Suite Teardown    Log suite tear down
Test Setup        Log test setup
Test Teardown     Log test tear down

*** Variables ***
${FIRST_MESSAGE}   My first test
${SECOND_MESSAGE}  My second test

*** Test Cases ***
My first test
    Log    ${FIRST_MESSAGE}
My second test
    Log    ${SECOND_MESSAGE}

*** Keywords ***
Log suite setup
    Log    Suite setup step
Log suite tear down
    Log    Suite tear down step
Log test setup
    Log    Test setup step
Log test tear down
    Log    Test tear down step
