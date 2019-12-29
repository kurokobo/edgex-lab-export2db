import json
import os
from datetime import datetime, timedelta, timezone
from os.path import dirname, join

import paho.mqtt.client as mqtt
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file
DOTENV_PATH = join(dirname(__file__), ".env")
load_dotenv(DOTENV_PATH)

# Initial configuration
jst = timezone(timedelta(hours=+9), "JST")


def setup_db():
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_PORT = os.getenv("MONGODB_PORT")
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_DB = os.getenv("MONGODB_DB")
    MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

    mongodb = pymongo.MongoClient(
        "mongodb://%s:%s@%s:%s/%s?retryWrites=false"
        % (MONGODB_USERNAME, MONGODB_PASSWORD, MONGODB_HOST, MONGODB_PORT, MONGODB_DB)
    )[MONGODB_DB][MONGODB_COLLECTION]

    return mongodb


def update_db(db, device, type, value):
    data = {
        "timestamp": str(datetime.now(jst)),
        "device": device,
        "type": type,
        "value": value,
    }
    print(data)
    db.insert_one(data)


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
