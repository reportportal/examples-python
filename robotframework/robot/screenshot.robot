*** Settings ***
Documentation     A simple failure test which takes and logs screenshot
Library           SeleniumLibrary
Library           webdrivermanager.chrome.ChromeDriverManager
Library           library/Log.py
Library           OperatingSystem
Suite Setup       Run Keywords                          Download And Install    AND
...               Set Screenshot Directory              EMBED
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
