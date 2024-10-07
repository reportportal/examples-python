# This example is recommended way of capturing Browser screenshots
*** Settings ***
Documentation     A simple failure test which takes and logs screenshot
Library           Browser
Suite Setup       Run Keywords              Register Keyword To Run On Failure  Take Screenshot

*** Keywords ***
Open Page
    [Arguments]                ${browser}                 ${url}
    New Browser                ${browser}
    New Page.                  ${url}

*** Test Cases ***
Screenshot test
    Open Page          Chrome      http://www.example.com
    Get Title          matches     Google
