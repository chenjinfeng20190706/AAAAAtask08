*** Settings ***
Library    pyLib.WebAdmin
Variables  cfg.py

Suite Setup     addTrainingSchedule     初中班1期       初中班1期描述     1   ${belongClass}
Suite Teardown  deleteList      schedule