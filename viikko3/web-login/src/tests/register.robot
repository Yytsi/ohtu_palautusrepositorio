*** Settings ***
Resource          resource.robot
Library           AppLibrary
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Go To Starting Page
Test Teardown     Reset Application State
Resource          login_resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  userduser
    Set Password  ValidPassword42!
    Set Password Confirmation  ValidPassword42!
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  ab
    Set Password  ValidPassword00!
    Set Password Confirmation  ValidPassword00!
    Submit Registration
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Go To Register Page
    Set Username  validMonkey2
    Set Password  short
    Set Password Confirmation  short
    Submit Registration
    Registration Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  validDrummer3
    Set Password  ValidPassword123!
    Set Password Confirmation  Doesnot23!
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Register Page
    Set Username  newuser123
    Set Password  Newpassword1!
    Set Password Confirmation  Newpassword1!
    Submit Registration
    Registration Should Succeed
    Go To Main Page
    Logout
    login_resource.Go To Login Page
    Set Username  newuser123
    Set Password  Newpassword1!
    Submit Login
    Ohtu Page Should Be Open

Login After Failed Registration
    Go To Register Page
    Set Username  existinguser
    Set Password  Pass1234!
    Set Password Confirmation  DifferentPass123!
    Submit Registration
    Registration Should Fail With Message  Passwords do not match
    login_resource.Go To Login Page
    Set Username  existinguser
    Set Password  Pass1234!
    Submit Login
    login_resource.Login Page Should Be Open


*** Keywords ***
Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Logout
    Click Button  Logout