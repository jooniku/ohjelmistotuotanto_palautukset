*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  joona
    Set Password  joona123123!!
    Set Password Confirmation  joona123123!!
    Submit Credentials
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  JAJSDIJD2434!"#"
    Set Password Confirmation  JAJSDIJD2434!"#"
    Submit Credentials
    Page Should Contain  Username too short

Register With Valid Username And Invalid Password
    Set Username  joona
    Set Password  kierokasi
    Set Password Confirmation  kierokasi
    Submit Credentials
    Page Should Contain  Password must contain at least one happy character

Register With Nonmatching Password And Password Confirmation
    Set Username  joona
    Set Password  kissa123!
    Set Password Confirmation  koira123!
    Submit Credentials
    Page Should Contain  Password confirmation incorrect

Login After Successful Registration
    Set Username  joonaa
    Set Password  joonajoona123!
    Set Password Confirmation  joonajoona123!
    Submit Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Username  joonaa
    Set Password  joonajoona123!
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  joonaaa
    Set Password  joonajoona123
    Set Password Confirmation  joonajoona123!
    Submit Credentials
    Go To Login Page
    Login Page Should Be Open
    Set Username  joonaaa
    Set Password  joonajoona123
    Submit Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Register Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
