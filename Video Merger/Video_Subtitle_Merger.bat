@echo off
title Auto Merge Video + Audio + Subtitle (including .webm subs)
echo.
echo ==========================================
echo   AUTO MERGER (FFmpeg) - WebM subs OK
echo ==========================================
echo.

setlocal enabledelayedexpansion

set "video="
set "audio="
set "sub="

:: Detect video
for %%f in (*.mp4 *.mkv *.webm *.mov) do (
    if not defined video set "video=%%f"
)

:: Detect audio
for %%f in (*.m4a *.aac *.mp3 *.opus *.wav) do (
    if not defined audio set "audio=%%f"
)

:: Detect subtitle (including .webm)
for %%f in (*.srt *.vtt *.ass *.webm) do (
    if not defined sub set "sub=%%f"
)

echo Found files:
echo Video: %video%
echo Audio: %audio%
echo Subtitle: %sub%
echo.

if "%video%"=="" (
    echo ❌ No video file found!
    pause
    exit /b
)

echo Choose merge type:
echo [1] Embed subtitles (soft - selectable)
echo [2] Burn subtitles (hard - always visible)
set /p choice=Enter 1 or 2: 

if not "%audio%"=="" (
    set "mergeaudio=-i "%audio%""
) else (
    set "mergeaudio="
)

echo.
echo 🔄 Merging, please wait...

:: Soft subtitles
if "%choice%"=="1" (
    if "%sub%"=="" (
        ffmpeg -i "%video%" %mergeaudio% -c copy "merged_%video%"
        echo ⚠️ No subtitle found, merged video/audio only.
    ) else (
        ffmpeg -i "%video%" %mergeaudio% -i "%sub%" -c copy -c:s mov_text "merged_%~n1.mp4"
        echo ✅ Done! Created merged_%~n1.mp4
    )
) else if "%choice%"=="2" (
    :: Hard subtitles
    if "%sub%"=="" (
        ffmpeg -i "%video%" %mergeaudio% -c copy "merged_%~n1.mp4"
        echo ⚠️ No subtitle found, merged video/audio only.
    ) else (
        ffmpeg -i "%video%" %mergeaudio% -vf "subtitles=%sub%" -c:a copy "burned_%~n1.mp4"
        echo ✅ Done! Created burned_%~n1.mp4
    )
) else (
    echo ❌ Invalid choice.
)

pause
