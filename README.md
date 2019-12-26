# Sample application to save exported data from EdgeX Foundry to MongoDB

## MQTT subscriber

The python application `mqtt/rest_to_mongodb.py` does:

1. Subscribe specified MQTT broker and its topic.
1. Save incoming values to specified MongoDB.

## RESTAPI endpoint

The python application `mqtt/rest_to_mongodb.py` does

1. Wait HTTP POST using Flask.
1. Save POSTed values to specified MongoDB.
