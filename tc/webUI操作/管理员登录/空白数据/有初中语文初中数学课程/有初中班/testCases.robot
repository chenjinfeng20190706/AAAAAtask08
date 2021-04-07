*** Settings ***
Library     pyLib.WebAdmin
Variables   cfg.py
*** Test Cases ***
用例4:添加培训班期
    [Setup]    deleteList      schedule

    addTrainingSchedule     python培训班01期    python培训班01期描述      1       ${belongClass}

    ${trainingScheduleList}=    listTrainingScheduleList

    should be true  $trainingScheduleList==["python培训班01期"]

    [Teardown]   deleteList      schedule