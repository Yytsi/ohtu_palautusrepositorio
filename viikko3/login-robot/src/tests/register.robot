*** Settings ***
Resource          resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New User Credentials  testuser  validPass123!
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New User Credentials  testuser  anotherPass123!
    Input New User Credentials  testuser  anotherPass123!
    Output Should Contain  User with username testuser already exists

Register With Too Short Username And Valid Password
    Input New User Credentials  xy  validPass123!
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input New User Credentials  test_user  validPass123!
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input New User Credentials  validuser  short
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New User Credentials  validuser  onlyletters
    Output Should Contain  Invalid password

*** Keywords ***
Input New User Credentials
    [Arguments]  ${username}  ${password}
    Input  new
    Input  ${username}
    Input  ${password}
    Run Application

Input
    [Arguments]  ${input}
    AppLibrary.Input  ${input}

Run Application
    AppLibrary.Run Application
