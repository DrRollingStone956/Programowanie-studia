import csv
import os
import time
from filelock import FileLock

FILE_PATH = "tasks.csv"
LOCK_PATH = "tasks.csv.lock"


def process_task():
    if not os.path.exists(FILE_PATH):
        return False

    lock = FileLock(LOCK_PATH)

    task_to_do = None
    rows = []

    with lock:
        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            if not reader:
                return False

            header = reader[0]
            data = reader[1:]

        updated = False
        for row in data:
            if not updated and row[2] == "pending":
                row[2] = "in_progress"
                task_to_do = row
                updated = True
            rows.append(row)

        if updated:
            with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(rows)

    if not task_to_do:
        return False

    task_id, task_name, _ = task_to_do
    print(
        f"[Consumer {os.getpid()}] Rozpoczęto: {task_name}"
        f"(ID: {task_id}) - status: in_progress"
    )
    time.sleep(30)

    with lock:
        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))
            header = reader[0]
            data = reader[1:]

        new_rows = []
        for row in data:
            if row[0] == task_id:
                row[2] = "done"
            new_rows.append(row)

        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(new_rows)

    print(
        f"[Consumer {os.getpid()}] Zakończono: {task_name}"
        f"(ID: {task_id}) - status: done"
    )
    return True


def main():
    print(f"[Consumer {os.getpid()}] Uruchomiono. Oczekiwanie na zadania...")
    while True:
        executed = process_task()
        if not executed:
            time.sleep(5)


if __name__ == "__main__":
    main()
