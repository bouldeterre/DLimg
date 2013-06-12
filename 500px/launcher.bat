@echo off

set debug=true

if "%debug%"=="true" (
    python 500pxDLimg.py seoul
) else (

echo "What do you want to dl?"
echo "[img] test "

set default=false
set INPUT=
set URL=
set /P INPUT= :


    if "%INPUT%"=="img" set res=true
    if "%INPUT%"=="" set res=true
    if "%res%"=="true"  (
        echo    "URL site=>img?"
    ) else if "%INPUT%"=="test" (
        echo "URL site=>test?"
    ) else (
        echo input not valid
        pause
        exit
    )

    ::if "%debug%"=="true" (
     ::   "%INPUT%"= http://91.121.132.199/SeriousO
    ::)
    ::else (
     ::   set /P URL= : 
    ::)

    if "%INPUT%"=="img" set res=true
    if "%INPUT%"=="" set res=true
    if "%res%"=="true"  (
        python DLimg.py %URL%
    ) else if "%INPUT%"=="test" (
        python testpython.py
    )
)

pause