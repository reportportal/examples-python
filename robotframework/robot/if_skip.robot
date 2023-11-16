*** Settings ***
Documentation  Example of skipping failure statement by 'IF'

*** Variables ***
${SKIP}    True

*** Test Cases ***
Test If Skip
    Log  One passed step to check
    IF   not ${SKIP}
         Fail  This step should be skipped
    ELSE
         Log   This step should pass
    END
