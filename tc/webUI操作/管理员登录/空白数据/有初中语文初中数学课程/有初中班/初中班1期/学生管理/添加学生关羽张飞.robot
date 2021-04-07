*** Settings ***
Library     pyLib.WebAdmin
Variables   cfg.py

*** Test Cases ***
添加学生关羽张飞
    [Setup]     deleteList      student

    addStudent      关羽      guanyu      青龙偃月刀         ${belongclass}   ${belongschedule}
    addStudent      张飞      zhangfei    丈八蛇矛          ${belongclass}   ${belongschedule}

    ${studentList}=     listStudentList
    should be true      $studentList==["张飞","关羽"]

    [Teardown]  deleteList      student