@echo off
:ImportsMain

goto :eof

:runPyScript
 where python >nul 2>nul
 if %errorlevel% neq 0 (
     echo Python is not installed. Please install Python and try again.
     exit /b 1
 )

 python %1
goto :eof

:importJsonFile
 for /f "tokens=1,2 delims=:{} " %%A in (%1) do (
     if "%%~B" equ "Dev" echo (%%~A=%%~B^)
 )
goto :eof

:PipInstall
 setlocal
 set "packageName=%1"
 python -m pip --version
 if %errorlevel% neq 0 CALL :InstallPip
 echo asasa
 pip install %packageName%

 endlocal
goto :eof

:InstallPip
 echo Pip isn't installed. We need to install it for GamePie.
 echo Do you want to install [Y/N]? (You can't use GamePie without it)
 set /p confirm=
 if /i "%confirm%" equ "N" exit /b 1
 if /i "%confirm%" equ "n" exit /b 1

 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
 python get-pip.py
 del get-pip.py
goto :eof