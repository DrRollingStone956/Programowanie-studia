import json
import sys
import uuid
import pika

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "tasks_queue"


def get_channel():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    return connection, channel


def add_tasks(count: int):
    connection, channel = get_channel()

    try:
        for _ in range(count):
            task_id = str(uuid.uuid4())[:8]
            task = {
                "id": task_id,
                "task_name": f"Phone call {task_id}",
            }

            channel.basic_publish(
                exchange="",
                routing_key=QUEUE_NAME,
                body=json.dumps(task),
                properties=pika.BasicProperties(
                    delivery_mode=pika.DeliveryMode.Persistent
                ),
            )
            print(f"[Producer] Added task to queue: {task_id}")
    finally:
        connection.close()


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    add_tasks(count)