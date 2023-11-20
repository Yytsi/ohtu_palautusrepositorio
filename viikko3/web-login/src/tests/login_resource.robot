*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Go To Login Page
    Go To  ${LOGIN_URL}
    Login Page Should Be Open

Set Login Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Login Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Login
    Click Button  Login

Login Page Should Be Open
    Title Should Be  Login

Ohtu Page Should Be Open
    Title Should Be  Ohtu Application main page
