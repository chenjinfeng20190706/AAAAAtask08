*** Settings ***
Library  SeleniumLibrary
Library  Collections
Resource  cfg.robot

#*** Variables ***
#${MgrLoginUrl}      http://localhost/mgr/login/login.html
#&{database}     name=auto   pw=sdfsdfsdf

*** Keywords ***

setup Website
    # 打开浏览器
    open browser    http://localhost/      chrome
    set selenium implicit wait  10

teardown Website
    close browser
loginSystem
    [Arguments]     ${username}     ${password}
    go to           ${MgrLoginUrl}
    #登录系统
    Input Text   id=username    ${username}
    Input Text   id=password    ${password}
    Click Button    css=button[onclick="postLoginRequest()"]
addCourse
    [Arguments]     ${courseName}       ${sourseDesc}       ${courseIndex}
    #确保在课程页面操作
    click element    css=a[href="#/"]
    sleep   1
    #添加课程
    Click Button    css=button[ng-click="showAddOne=true"]
    Input Text      css=input[ng-model="addData.name"]    ${courseName}
    Input Text      css=textarea[ng-model="addData.desc"]   ${sourseDesc}
    Input Text      css=input[ng-model="addData.display_idx"]   ${courseIndex}
    Click Button    css=button[ng-click="addOne()"]

getCourseList
    #确保在课程页面操作
    click element    css=a[href="#/"]
    sleep  1
    #判断
    ${courseList}   create list
    ${eles}   Get Webelements    css=tr>td:nth-child(2)
    :FOR    ${ele}  IN  @{eles}
    \       ${ret}  get text  ${ele}
    \       Append To List      ${courseList}       ${ret}
    [Return]  ${courseList}

deleteAllCourse
#    loginSystem     &{database}[name]    &{database}[pw]
    #确保在课程页面操作
    click element    css=a[href="#/"]
    sleep   1
    set selenium implicit wait  1
    :FOR    ${one}  IN RANGE    9999
    \       ${eles}     Get Webelements     css=button[ng-click="delOne(one)"]
#    \       log to console  ${eles}
    \       exit for loop if   $eles==[]
#    \       ${ele}     evaluate     $eles[0]
#    \       click element     ${ele}
    \       click button        @{eles}[0]
    \       Click button        css=button[class="btn btn-primary"]
    \       sleep  2
    set selenium implicit wait  10

delete AllTeacher

    click element   css=a[href="#/teacher"]
    sleep   1
    set selenium implicit wait  1
    :FOR    ${one}  IN RANGE    9999
    \       ${eles}     Get Webelements     css=button[ng-click="delOne(one)"]
#   \       log to console  ${eles}
    \       exit for loop if   $eles==[]
#   \       ${ele}     evaluate     $eles[0]
#   \       Click Element     ${ele}
    \       Click Element       @{eles}[0]
    \       Click Element     css=button[class="btn btn-primary"]
    \       sleep  1
    set selenium implicit wait  10

#增加老师的操作步骤用RF来写就比较的麻烦了！！！！！！
addTeacher
    [Arguments]     ${teacherName}    ${teacherUserName}    ${teacherDesc}  ${teacherIndex}    ${teachCourse}

    #确保在老师页面操作
    click element   css=a[href="#/teacher"]
    sleep   1
    click element   css=button[ng-click="showAddOne=true"]
    Input Text      css=input[ng-model="addEditData.realname"]      ${teacherName}
    Input Text      css=input[ng-model="addEditData.username"]      ${teacherUserName}
    Input Text      css=textarea[ng-model="addEditData.desc"]       ${teacherDesc}
    Input Text      css=input[ng-model="addEditData.display_idx"]   ${teacherIndex}


    set selenium implicit wait  1
    :FOR    ${one}  IN RANGE    9999
    \       ${eles}=    Get Webelements     css=button[ng-click="addEditData.delTeachCourse(course)"]
    \       exit for loop if  $eles==[]
    \       click element   @{eles}[0]
    set selenium implicit wait  10

    :FOR  ${one}  IN    @{teachCourse}
    \     select from list by label  css=select[ng-model="$parent.courseSelected"]    @{teachCourse}
    \     click element   css=i[class="fa fa-plus"]
    \     click element  css=button[ng-click="addOne()"]



get teacher list
    click element       css=a[href="#/teacher"]
    sleep   2
    #列出课程
    ${eles}     get webelements     css=tr>td:nth-child(2
    ${teachers}  create list
    :FOR    ${ele}  IN  @{eles}
#    \   log to console  ${ele.text}
    \   append to list  ${teachers}  ${ele.text}
    [Return]  ${teachers}
