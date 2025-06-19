import tkinter as tk
import threading
import time
import csv
from datetime import datetime
from dataclasses import dataclass

# 사용자 정의 예외
@dataclass
class EmptyInputError(Exception):
    message: str

@dataclass
class InvalidTimeError(Exception):
    value: str

# 세션 로그 저장
def save_session_log(session_name, focus_minutes):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("focus_log.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([now, session_name, focus_minutes])

# 타이머 동작
def run_timer(minutes, update_func, done_callback):
    seconds = int(float(minutes) * 60)
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        update_func(text=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
        seconds -= 1
    done_callback()

# 타이머 시작
def start_focus():
    try:
        session_name = entry_name.get().strip()
        focus_time = entry_focus.get().strip()
        break_time = entry_break.get().strip()
        repeat_count = entry_repeat.get().strip()

        # 입력값 체크
        if not session_name or not focus_time or not break_time or not repeat_count:
            raise EmptyInputError("모든 입력 필드를 채워야 합니다.")

        try:
            focus_minutes = float(focus_time)
            break_minutes = float(break_time)
            repeats = int(repeat_count)
        except ValueError:
            raise InvalidTimeError("숫자가 아닌 값이 입력되었습니다.")

        btn_start.config(state=tk.DISABLED)

        def session_loop(i):
            if i >= repeats:
                lbl_status.config(text="모든 세션이 완료되었습니다.")
                btn_start.config(state=tk.NORMAL)
                return

            lbl_status.config(text=f"[{i+1}/{repeats}] 집중 시간 시작")
            run_timer(
                focus_minutes,
                lbl_timer.config,
                lambda: after_focus(i)
            )

        def after_focus(i):
            lbl_status.config(text="집중 종료, 로그 저장 중...")
            save_session_log(session_name, focus_minutes)
            time.sleep(1)
            lbl_status.config(text="휴식 시간 시작")
            run_timer(
                break_minutes,
                lbl_timer.config,
                lambda: session_loop(i + 1)
            )

        threading.Thread(target=lambda: session_loop(0), daemon=True).start()

    except EmptyInputError as e:
        lbl_status.config(text=f"입력 오류: {e.message}")
    except InvalidTimeError as e:
        lbl_status.config(text=f"시간 입력 오류: {e.value}")

# GUI 구성
root = tk.Tk()
root.title("FocusTime 타이머")

tk.Label(root, text="세션 이름:").grid(row=0, column=0, sticky='e')
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="집중 시간 (분):").grid(row=1, column=0, sticky='e')
entry_focus = tk.Entry(root)
entry_focus.insert(0, "25")
entry_focus.grid(row=1, column=1)

tk.Label(root, text="휴식 시간 (분):").grid(row=2, column=0, sticky='e')
entry_break = tk.Entry(root)
entry_break.insert(0, "5")
entry_break.grid(row=2, column=1)

tk.Label(root, text="반복 횟수:").grid(row=3, column=0, sticky='e')
entry_repeat = tk.Entry(root)
entry_repeat.insert(0, "4")
entry_repeat.grid(row=3, column=1)

btn_start = tk.Button(root, text="타이머 시작", command=start_focus)
btn_start.grid(row=4, column=0, columnspan=2, pady=10)

lbl_timer = tk.Label(root, text="00:00", font=("Helvetica", 24))
lbl_timer.grid(row=5, column=0, columnspan=2, pady=10)

lbl_status = tk.Label(root, text="대기 중입니다.")
lbl_status.grid(row=6, column=0, columnspan=2)

root.mainloop()
