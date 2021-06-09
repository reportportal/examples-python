*** Settings ***
Documentation   The example demonstrates saucelabs integration. Set \
...             'SAUCELABS_USER' and 'SAUCELABS_TOKEN' environment variables \
...             with yours.
Library         String
Library         OperatingSystem
Library         SeleniumLibrary
Suite Teardown  Close Browser

*** Variables ***
${DELAY}               1 second
${SAUCELABS_URL}       https://ondemand.eu-central-1.saucelabs.com:443/wd/hub
${SAUCELABS_PLATFORM}  Windows 10


*** Keywords ***
Open Page
    [Arguments]              ${browser}         ${url}
    ${sl_user}               Get Environment Variable  SAUCELABS_USER
    ${sl_token}              Get Environment Variable  SAUCELABS_TOKEN
    ${sauce:options}         Create Dictionary
    ...                      name               ${TEST NAME}
    ${capabilities}          Create Dictionary
    ...                      browserName        ${browser}
    ...                      browserVersion     latest
    ...                      platformName       ${SAUCELABS_PLATFORM}
    ...                      sauce:options      ${sauce:options}
    ${sl_host}               Fetch From Right   ${SAUCELABS_URL}          //
    ${sl_protocol}           Fetch From Left    ${SAUCELABS_URL}          //
    ${user_password}         Catenate           SEPARATOR=:
    ...                      ${sl_user}         ${sl_token}
    ${remote_url}            Catenate           SEPARATOR=
    ...                      ${sl_protocol}     //
    ...                      ${user_password}   @
    ...                      ${sl_host}
    Open Browser             ${url}             remote_url=${remote_url}
    ...                      desired_capabilities=${capabilities}
    Maximize Browser Window
    Set Selenium Speed       ${DELAY}
Attach Saucelabs Report
    ${session}               Get Session Id
    ${sl_tag}                Catenate           SEPARATOR=:
    ...                      SLID               ${session}
    Set Tags                 ${sl_tag}

*** Test Cases ***
Example page test
    Open Page          Chrome          http://www.example.com
    Title Should Be    Example Domain
    Attach Saucelabs Report
