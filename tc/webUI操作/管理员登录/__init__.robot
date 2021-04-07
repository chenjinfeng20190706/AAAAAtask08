*** Settings ***
Library     pyLib.WebAdmin
Variables   cfg.py
Suite Setup      loginSystem     &{database}[name]    &{database}[pw]