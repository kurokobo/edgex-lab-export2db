import json
import os
from datetime import datetime, timedelta, timezone
from os.path import dirname, join

import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv

# Load environment variables from .env file
DOTENV_PATH = join(dirname(__file__), ".env")
load_dotenv(DOTENV_PATH)

# Initial configuration
jst = timezone(timedelta(hours=+9), "JST")


def setup_db():
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

    redisdb = redis.Redis(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True
    )
    return redisdb


def update_db(db, device, type, value):
    data = {
        "timestamp": str(datetime.now(jst)),
        "device": device,
        "type": type,
        "value": value,
    }
    print(data)
    db.set("sensor_" + type, json.dumps(data))


def on_message(client, userdata, message):
    data = json.loads(str(message.payload.decode("utf-8")))
    update_db(
        db=db,
        device=data["readings"][0]["device"],
        type=data["readings"][0]["name"],
        value=data["readings"][0]["value"],
    )


def main():
    MQTT_BROKER = os.getenv("MQTT_BROKER")
    MQTT_TOPIC = os.getenv("MQTT_TOPIC")
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER)
    client.subscribe(MQTT_TOPIC)
    client.loop_forever()


if __name__ == "__main__":
    db = setup_db()
    main()
