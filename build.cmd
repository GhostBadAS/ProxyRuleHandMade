@echo off
REM 批处理：先运行 Python 脚本，把所有 .list 转换成 .json
REM 再遍历目录下所有 .json 文件，生成对应的 .srs 文件

setlocal enabledelayedexpansion

REM Python 脚本文件名（必须和本批处理放同目录）
set PYTHON_SCRIPT=规则转换.py

REM sing-box.exe 路径（如果已在同目录，不用改）
set SINGBOX=sing-box.exe

REM 先执行 Python 脚本（需要系统已安装 Python）
echo 正在运行规则转换脚本 %PYTHON_SCRIPT% ...
python "%PYTHON_SCRIPT%"
if errorlevel 1 (
    echo ? Python 脚本执行失败，请检查是否安装 Python。
    pause
    exit /b
)

REM 遍历当前目录的所有 json 文件并编译成 srs
for %%f in (*.json) do (
    echo 正在编译 %%f ...
    %SINGBOX% rule-set compile --output "%%~nf.srs" "%%f"
)

echo.
echo ? 所有 list 已转换为 json 并编译为 srs

@REM .\build.cmd