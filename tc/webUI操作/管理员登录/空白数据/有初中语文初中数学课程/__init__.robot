*** Settings ***
Library     pyLib.WebAdmin

Suite Setup     run keywords    deleteList      course
                ...      AND    addCourse       初中语文    初中语文描述     1
                ...      AND    addCourse       初中数学    初中数学描述     2
Suite Teardown  deleteList      course