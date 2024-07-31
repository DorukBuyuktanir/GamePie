@echo off
title GamePie
color 0e
echo Welcome to the Game Pie. Please be sure that you open the file on its location!!!

rem Imports
set "imports=GamePie\ConsoleCommands\Imports.bat"

rem Installing Packages
CALL %imports% :PipInstall PyExecJS
CALL %imports% :PipInstall cffi

rem Settings Stuff
set filePath=%~dp0
CALL :BuildInfo
echo You can write commands now. Write help if you need...
pause

rem Main Code
:commandPrompt
set /p command=
if "%command%" equ "" goto commandPrompt

echo {"currentState": "unprocessed", "message": "%command%"} > "GamePie\TerminalStuff\commands.json"
CALL %imports% :runPyScript "GamePie\TerminalStuff\commands.py"
goto commandPrompt

rem Functions
:BuildInfo
 setlocal
 set "infoFile=GamePie\buildInfo.py"
 (
   echo buildInfo = {
   echo   "platform": "windows",
   echo   "path": "%filePath%\"
   echo }
 ) > "%infoFile%"
 endlocal
goto :eof
