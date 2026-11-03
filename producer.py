import csv
import os
import sys
import uuid
from filelock import FileLock

FILE_PATH = "tasks.csv"
LOCK_PATH = "tasks.csv.lock"


def add_task():
    file_exists = os.path.exists(FILE_PATH)

    lock = FileLock(LOCK_PATH)
    with lock:
        with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["id", "task_name", "status"])

            task_id = str(uuid.uuid4())[:8]
            writer.writerow(
                [task_id, f"Rozmowa telefoniczna {task_id}", "pending"]
                )
            print(
                f"[Producer] Dodano zadanie:"
                f"{task_id} ze statusem 'pending'"
                )


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for _ in range(count):
        add_task()
