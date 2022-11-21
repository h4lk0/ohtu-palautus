*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  s4l4
    Set Confirmation  s4l4
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  s4l4s4n4
    Set Confirmation  s4l4sana
    Submit Registration
    Registration Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Set Username  minna
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Registration
    Registration Should Succeed
    Click Main Page Link
    Click Logout Button
    Set Username  minna
    Set Password  s4l4s4n4
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  b
    Set Password  s4l4s4n4
    Set Confirmation  s4l4s4n4
    Submit Registration
    Register Page Should Be Open
    Click Link  Login
    Login Page Should Be Open
    Set Username  b
    Set Password  s4l4s4n4
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Registration
    Click Button  Register

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

Click Main Page Link
    Click Link  Continue to main page
    Main Page Should Be Open

Click Logout Button
    Click Button  Logout
    Login Page Should Be Open