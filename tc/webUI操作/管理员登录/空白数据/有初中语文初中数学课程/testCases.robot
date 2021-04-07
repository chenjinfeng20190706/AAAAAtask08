*** Settings ***
Library  pyLib.WebAdmin

*** Test Cases ***
用例3:添加培训班
    [Setup]     deleteList  class

    ${containCourse}    evaluate    ["初中语文","初中数学"]
    addClass    python培训班(初中班)      python培训班(初中班)详情描述      1    ${containCourse}

    ${classList}=   listTrainingCourseList

    log to console  ${classList}

    ${classListExcepted}=   evaluate   ["python培训班(初中班)"]

    should be true  $classListExcepted==$classList

    [Teardown]  deleteList  class

添加老师功能1
    [Setup]     deleteList      teacher


    ${teachCourseList1}      evaluate    ["初中语文"]
    addTeacher      陈玉平     chenyuping      tony老师      2   ${teachCourseList1}

    ${retTeacherList}=      listTeacher
    ${exceptedTeacher}      evaluate    ["陈玉平"]
    should be true      $retTeacherList==$exceptedTeacher

    [Teardown]     deleteList      teacher



添加老师功能2
    [Setup]         deleteList      teacher


    ${teachCourseList1}      evaluate    ["初中语文"]
    addTeacher      陈玉平     chenyuping      tony老师      2   ${teachCourseList1}
    ${teachCourseList2}      evaluate    ["初中数学"]
    addTeacher      伍长连     wuzhanglian     mary老师      1   ${teachCourseList2}

    ${retTeacherList}=      listTeacher
    ${exceptedTeacher}      evaluate    ["伍长连","陈玉平"]
    should be true      $retTeacherList==$exceptedTeacher

    [Teardown]   deleteList      teacher