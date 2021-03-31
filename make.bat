@echo off

if not exist out\NUL md out
"C:\Program Files (x86)\FontForgeBuilds\bin\fontforge.exe" -script generate.py
