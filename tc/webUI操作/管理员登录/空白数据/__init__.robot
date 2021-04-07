*** Settings ***
Library     pyLib.WebAdmin

Suite Setup     run keywords    deleteList      student
                ...      AND    deleteList      schedule
                ...      AND    deleteList      class
                ...      AND    deleteList      teacher
                ...      AND    deleteList      course