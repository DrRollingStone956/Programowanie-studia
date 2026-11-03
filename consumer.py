import os
import sqlite3
import time

DB_PATH = "tasks.db"


def process_task():
    if not os.path.exists(DB_PATH):
        return False

    conn = sqlite3.connect(DB_PATH, timeout=20.0)
    cursor = conn.cursor()

    task_to_do = None

    try:
        cursor.execute("BEGIN IMMEDIATE")
        cursor.execute(
            "SELECT id, task_name FROM tasks WHERE status = 'pending' LIMIT 1"
        )
        row = cursor.fetchone()

        if row:
            task_id, task_name = row
            cursor.execute(
                "UPDATE tasks SET status = 'in_progress' WHERE id = ?",
                (task_id,)
            )
            conn.commit()
            task_to_do = (task_id, task_name)
        else:
            conn.rollback()
    except sqlite3.OperationalError as e:
        conn.rollback()
        return False
    finally:
        conn.close()

    if not task_to_do:
        return False

    task_id, task_name = task_to_do
    print(
        f"[Consumer {os.getpid()}] Rozpoczęto: {task_name}"
        f"(ID: {task_id}) - status: in_progress"
    )
    time.sleep(30)

    conn = sqlite3.connect(DB_PATH, timeout=20.0)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

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
