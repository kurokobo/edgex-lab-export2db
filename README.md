# Sample application to save exported data from EdgeX Foundry to MongoDB


## MQTT subscriber

The python application `mqtt/rest_to_mongodb.py` does:

1. Subscribe specified MQTT broker and its topic.
1. Save incoming values to specified MongoDB.

To run this on PWS, update your `vars.yml` and invoke followings:

```sh
$ cd mqtt
$ cf push --vars-file vars.yml 
```

To run this on locally, update your `.env` and invoke followings:

```sh
$ cd mqtt
$ python mqtt_to_mongodb.py
```


## RESTAPI endpoint

The python application `mqtt/rest_to_mongodb.py` does

1. Wait HTTP POST using Flask.
1. Save POSTed values to specified MongoDB.

To run this on PWS, update your `vars.yml` and invoke followings:

```sh
$ cd rest
$ cf push --vars-file vars.yml 
```

To run this on locally, update your `.env` and invoke followings:

```sh
$ cd rest
$ python rest_to_mongodb.py
```