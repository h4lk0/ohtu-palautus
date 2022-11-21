*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  s4l4
    Set Confirmation  s4l4
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  s4l4s4n4
    Set Confirmation  s4l4sana
    Submit Credentials
    Registration Should Fail With Message  Password and confirmation do not match

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Registration Should Succeed
    Welcome Page Should Be Open

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open