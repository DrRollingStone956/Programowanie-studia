import json
import os
import time
import pika

RABBITMQ_HOST = "localhost"
QUEUE_NAME = "tasks_queue"


def callback(ch, method, properties, body):
    task = json.loads(body.decode("utf-8"))
    task_id = task["id"]
    task_name = task["task_name"]

    print(
        f"[Consumer {os.getpid()}] Began: {task_name} "
        f"(ID: {task_id}) - status: in_progress"
    )

    time.sleep(30)

    print(
        f"[Consumer {os.getpid()}] Done: {task_name} "
        f"(ID: {task_id}) - status: done"
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(
        queue=QUEUE_NAME,
        on_message_callback=callback,
        auto_ack=False,
    )

    print(f"[Consumer {os.getpid()}] Started. Awaiting...")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(f"\n[Consumer {os.getpid()}] Stopping...")
        channel.stop_consuming()
    finally:
        connection.close()


if __name__ == "__main__":
    main()