*** Settings ***
Documentation  Example of different log types
Library        library/Log.py
Library        OperatingSystem
Library        String
Library        mimetypes.MimeTypes
Test Setup     Set Log Level    TRACE

*** Variables ***
${ATTACHMENTS}        res/files

*** Keywords ***
Get file
    [Arguments]    ${file}
    ${data}        Get Binary File    ${file}
    ${name}        Fetch From Right   ${file}               /
    ${type}        Guess Type         ${file}
    ${result}      Create Dictionary
    ...            mime               ${type}[0]
    ...            name               ${name}
    ...            data               ${data}
    [return]       ${result}

*** Test Cases ***
Test logging
    Item Log        TRACE                      Trace log entry
    Item Log        DEBUG                      Debug log entry
    Item Log        INFO                       Info log entry
    Item Log        WARN                       Warning log entry
    Item Log        ERROR                      Error log entry
    @{file_list}    List Files In Directory    ${ATTACHMENTS}
    FOR             ${file}                    IN                         @{file_list}
                    ${attachment}              Get file                   ${ATTACHMENTS}/${file}
                    Item Log                   INFO                       I'm logging ${attachment}[mime]   ${attachment}
    END
