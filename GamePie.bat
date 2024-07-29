@echo off
title GamePie
color 0e
echo Welcome to the Game Pie. Please be sure that you open the file on it's locatio!!!
set filePath=%~dp0
CALL :BuildInfo
echo You can write commands now. Write help if you need...
pause
:commandPromt
set /p command=
if command == "" Goto :commandPromt

echo {^"currentState^": ^"unproced^", ^"message^": ^"%command%^"} > "GamePie\commands.json"
CALL :runPyScript "GamePie\commands.py"
Goto :commandPromt

rem  functions
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

 :runPyScript

 where python >nul 2>nul
 if %errorlevel% neq 0 (
     echo Python yüklü değil. Lütfen Python'u yükleyin ve tekrar deneyin.
     exit /b 1
 )

 python %1
 pause
 goto :eof