# FocusTime

GUI 기반의 Pomodoro 타이머입니다. 사용자가 집중 시간과 휴식 시간을 설정하고, 이를 반복하며 집중력을 향상시킬 수 있도록 도와줍니다.  
특히 시험 기간에 유용하고 각 집중 세션은 자동으로 CSV 파일에 로그됩니다.

FocusTime is a GUI-based Pomodoro timer that helps users enhance their concentration by repeating a set of focus and break periods.  
It is especially useful during exam preparation. Each completed focus session is automatically logged to a CSV file.

---

## Authors / 작성자

202321202 박소현 (2025.06.20)

---

## 프로젝트 개요 (Synopsis) / Project Overview

이 프로그램은 다음과 같은 기능을 포함합니다:  
This program includes the following features:

- 세션 이름, 집중 시간, 휴식 시간, 반복 횟수를 사용자가 입력  
  User inputs the session name, focus time, break time, and number of repetitions
- GUI 화면에 실시간으로 타이머 표시  
  Real-time timer is displayed on the GUI
- 집중 시간 종료 시 자동으로 `focus_log.csv` 파일에 기록 저장  
  After each focus session ends, the session is automatically logged to a `focus_log.csv` file

사용된 기술 / Technologies used:
- `tkinter`: GUI 구성 / for GUI construction
- `csv`: 로그 파일 저장 / for logging data
- `threading`: 타이머 동작 중 GUI 멈춤 방지 / to prevent GUI freezing
- `dataclasses`: 사용자 정의 예외 처리 / for custom exception handling

---

## 설치 방법 (How to Install)

- Python 3.10 이상이 필요합니다.  
  Requires Python 3.10 or higher
- 표준 라이브러리만 사용하기에 추가 라이브러리는 필요하지 않습니다.  
  No external libraries are required (only standard library is used)

---

## 사용 방법 (How to Use)

### 요구 환경 / System Requirements
- OS: Windows 11 (또는 macOS, Linux)  
  OS: Windows 11 (also compatible with macOS and Linux)
- Python 버전: 3.10 이상  
  Python version: 3.10 or later
- GUI 환경이 실행 가능한 시스템  
  A system capable of running GUI applications

### 실행 방법 / Execution Steps
1. 터미널 또는 명령 프롬프트(cmd)에서 다음 명령어 입력:  
   Run the following command in terminal:
```
python focustime_gui.py
```

2. 실행하면 GUI 창이 나타납니다.  
   A GUI window will appear.

3. 아래 항목을 입력합니다:  
   Enter the following:
   - **세션 이름 (Session Name)**: 기록에 남길 이름 (예: `기말고사 공부`)  
     Name to be recorded in the log (e.g., `Exam Prep`)
   - **집중 시간 (Focus Time)**: 분 단위 (예: `25`)  
     Duration of one focus session in minutes (e.g., `25`)
   - **휴식 시간 (Break Time)**: 분 단위 (예: `5`)  
     Duration of break between sessions in minutes (e.g., `5`)
   - **반복 횟수 (Repeat Count)**: 반복 횟수 (예: `4`)  
     Number of focus/break repetitions (e.g., `4`)

4. "타이머 시작" 버튼 클릭 시 다음과 같은 순서로 진행됩니다:  
   Click the “Start Timer” button to begin. The program will:
   - 집중 타이머 카운트다운  
     Run a countdown for the focus session
   - 종료 후 로그 저장  
     Save a log entry when the session ends
   - 휴식 타이머 진행  
     Start a break timer
   - 지정한 횟수만큼 반복  
     Repeat until the specified number of sessions is completed

5. 집중 세션이 끝날 때마다 자동으로 `focus_log.csv` 파일에 로그가 저장됩니다.  
   Each completed focus session is saved to `focus_log.csv`.

---

## 실행 예시 / Example Execution

```
[1/2] 집중 시간 시작 / Focus session started
타이머: 00:06
집중 종료, 로그 저장 중... / Focus ended, saving log...
휴식 시간 시작 / Break started
타이머: 00:01

[2/2] 집중 시간 시작
...
모든 세션이 완료되었습니다. / All sessions completed.
```

### 생성된 CSV 파일 예시 (`focus_log.csv`) / Example CSV Output

```
2025-06-20 15:10:00,기말고사 공부,0.1
2025-06-20 15:11:00,기말고사 공부,0.1
```

---

## 라이선스 (License)

이 프로젝트는 MIT License 하에 배포됩니다.  
This project is licensed under the MIT License.
