*** Settings ***
Library  SeleniumLibrary
Library  pyLib.WebAdmin

*** Test Cases ***
检查添加课程功能
     [Setup]    deleteList  course

    #1添加python课程
    addCourse  python  python课程    2

    #2添加java课程
    addCourse  java  java课程    1

    #3进行检查
    ${exceptedCourse}   evaluate  ["java","python"]
    ${courseList}       listCourse
    should be true      $courseList==$exceptedCourse
    [Teardown]  deleteList  course