*** Settings ***
Documentation     Example using tags, will give two tags: 'one two' and 'three'. Tags are separated by two spaces.

*** Variables ***
${MESSAGE}        Hello, world!

*** Test Cases ***
My Test
    [Tags]  one two  three
    Log     ${MESSAGE}
