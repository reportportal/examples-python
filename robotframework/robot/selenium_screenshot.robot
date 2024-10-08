# This example is recommended way of capturing Selenium screenshots
*** Settings ***
Documentation     A simple failure test which takes and logs screenshot
Library           SeleniumLibrary
Suite Setup       Run Keywords              Register Keyword To Run On Failure  Capture Page Screenshot  AND
...               Set Screenshot Directory  .
Suite Teardown    Close Browser

*** Variables ***
${DELAY}          1 second

*** Keywords ***
Open Page
    [Arguments]                ${browser}                 ${url}
    Open Browser               ${url}                     ${browser}
    Maximize Browser Window
    Set Selenium Speed         ${DELAY}

*** Test Cases ***
Screenshot test
    Open Page          Chrome      http://www.example.com
    Title Should Be    Google
