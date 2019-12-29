# Store metrics from EdgeX Foundry in DBs


## Subscribe MQTT topic and then store in InfluxDB Cloud

The docker image build with `mqtt-influxdb/docker/Dockerfile` does:

1. Store values in InfluxDB using [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) with [MQTT Consumer](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/mqtt_consumer).

The prebuilt image available on Docker Hub [kurokobo/edgex-lab-telegraf](https://hub.docker.com/repository/docker/kurokobo/edgex-lab-telegraf).

But most cases you have to replace `telegraf.conf` with your own configuration because currently PWS does not support external volumes.

To run this on PWS, update your `telegraf.conf` and `vars.yml`, then invoke followings:

```sh
$ cd mqtt-influxdb/docker
$ docker build . -t <username>/edgex-lab-telegraf:1.13.0
$ docker push k<username>/edgex-lab-telegraf:1.13.0
$ cd ../
$ cf push --vars-file vars.yml 
```

To run this locally, update your `telegraf.conf` and `.env`, then invoke followings:

```sh
$ cd mqtt-influxdb/docker
$ docker build . -t <username>/edgex-lab-telegraf:1.13.0
$ docker run -d --env-file ../.env edgex-lab-telegraf:1.13.0
```


## Subscribe MQTT topic and then store in MongoDB

The python application `mqtt-mongodb/rest_to_mongodb.py` does:

1. Subscribe specified MQTT broker and its topic.
1. Store incoming values in specified MongoDB.

To run this on PWS, update your `vars.yml` and invoke followings:

```sh
$ cd mqtt-mongodb
$ cf push --vars-file vars.yml 
```

To run this locally, update your `.env` and invoke followings:

```sh
$ cd mqtt-mongodb
$ python mqtt_to_mongodb.py
```


## Listen as REST endpoint and then store in MongoDB

The python application `rest-mongodb/rest_to_mongodb.py` does:

1. Wait HTTP POST using Flask.
1. Store POSTed values in specified MongoDB.

To run this on PWS, update your `vars.yml` and invoke followings:

```sh
$ cd rest-mongodb
$ cf push --vars-file vars.yml 
```

To run this locally, update your `.env` and invoke followings:

```sh
$ cd rest-mongodb
$ python rest_to_mongodb.py
```


## Subscribe MQTT topic and then store in Redis

The python application `mqtt-redis/rest_to_redis.py` does:

1. Subscribe specified MQTT broker and its topic.
1. Store incoming values in specified MongoDB.

Prease note this application store only newest value of each sensor types. This behavior is completely different from other `mqtt-*` series in this repository.

To run this on PWS, update your `vars.yml` and invoke followings:

```sh
$ cd mqtt-redis
$ cf push --vars-file vars.yml 
```

To run this locally, update your `.env` and invoke followings:

```sh
$ cd mqtt-redis
$ python mqtt_to_redis.py
```
