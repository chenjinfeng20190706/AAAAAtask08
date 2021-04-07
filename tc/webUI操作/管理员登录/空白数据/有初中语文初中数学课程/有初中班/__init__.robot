*** Settings ***
Library     pyLib.WebAdmin
Variables   cfg.py
Suite Setup     run keywords    deleteList      class
                ...      AND    addClass    初中班     初中班描述   1   ${containCourse}
Suite Teardown  deleteList      class
