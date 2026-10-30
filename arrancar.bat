@echo off
title Voluntariado Activo
cd /d "%~dp0"

rem abre el navegador cuando el servidor ya este arrancado
start "" cmd /c "timeout /t 3 >nul & start http://127.0.0.1:8000/"

echo Arrancando el servidor... (Ctrl + C para pararlo)
py manage.py runserver

pause
