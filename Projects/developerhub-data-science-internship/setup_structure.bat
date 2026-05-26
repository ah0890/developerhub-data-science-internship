@echo off
:: ============================================================
::  Data Science Internship — Folder Structure Setup
::  Run this file from inside your Data_Science_Internship dir
::  or from anywhere; it creates the folder next to this script.
:: ============================================================

setlocal EnableDelayedExpansion

:: Determine the root = folder where this .bat lives
set "ROOT=%~dp0"
:: Remove trailing backslash
if "%ROOT:~-1%"=="\" set "ROOT=%ROOT:~0,-1%"

echo.
echo  =====================================================
echo   Data Science Internship - Structure Generator
echo  =====================================================
echo   Root : %ROOT%
echo.

:: ── Top-level assignment folders ─────────────────────────
for %%A in (Assignment_1 Assignment_2 Assignment_3 Assignment_4 Assignment_5) do (
    if not exist "%ROOT%\%%A" (
        mkdir "%ROOT%\%%A"
        echo  [+] Created  %%A\
    ) else (
        echo  [=] Exists   %%A\
    )
)

:: ── Assignment_4 sub-structure (Medical Insurance Project) ─
set "A4=%ROOT%\Assignment_4"

for %%D in (data notebooks charts models) do (
    if not exist "%A4%\%%D" (
        mkdir "%A4%\%%D"
        echo  [+] Created  Assignment_4\%%D\
    ) else (
        echo  [=] Exists   Assignment_4\%%D\
    )
)

:: ── Placeholder README files for empty assignments ────────
for %%A in (Assignment_1 Assignment_2 Assignment_3 Assignment_5) do (
    if not exist "%ROOT%\%%A\README.md" (
        echo # %%A > "%ROOT%\%%A\README.md"
        echo Add your project files here. >> "%ROOT%\%%A\README.md"
        echo  [+] Created  %%A\README.md
    )
)

:: ── Assignment_4 README (if missing) ─────────────────────
if not exist "%A4%\README.md" (
    echo # Assignment_4 - Medical Insurance Claim Prediction > "%A4%\README.md"
    echo Place medical_cost.csv in the data\ folder, then run run_pipeline.py >> "%A4%\README.md"
    echo  [+] Created  Assignment_4\README.md
)

echo.
echo  =====================================================
echo   Setup complete. Final structure:
echo  =====================================================
tree "%ROOT%" /F /A 2>nul || dir "%ROOT%" /s /b
echo.
echo  Place your medical_cost.csv in:
echo  %A4%\data\
echo.
pause
