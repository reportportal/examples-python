# This method is recommended way of storing screenshots
*** Settings ***
Documentation     A simple failure test which takes and logs screenshot
Library           SeleniumLibrary
Library           webdrivermanager.chrome.ChromeDriverManager
Library           library/Log.py
Library           OperatingSystem
Suite Setup       Run Keywords                          Download And Install    AND
...               Register Keyword To Run On Failure    Post screenshot         AND
...               Set Screenshot Directory              .
Suite Teardown    Close Browser

*** Variables ***
${DELAY}          1 second

*** Keywords ***
Open Page
    [Arguments]                ${browser}                 ${url}
    Open Browser               ${url}                     ${browser}
    Maximize Browser Window
    Set Selenium Speed         ${DELAY}
Post screenshot
    ${screenshot_file}         Capture Page Screenshot
    Screenshot Log             ERROR                      Screenshot    ${screenshot_file}

*** Test Cases ***
Screenshot test
    Open Page          Chrome      http://www.example.com
    Title Should Be    Google
