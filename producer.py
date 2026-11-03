import sqlite3
import sys
import uuid

DB_PATH = "tasks.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                task_name TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """
        )
        conn.commit()


def add_task():
    init_db()
    task_id = str(uuid.uuid4())[:8]
    task_name = f"Rozmowa telefoniczna {task_id}"

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (id, task_name, status) VALUES (?, ?, ?)",
            (task_id, task_name, "pending"),
        )
        conn.commit()
    print(f"[Producer] Dodano zadanie: {task_id} ze statusem 'pending'")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for _ in range(count):
        add_task()
