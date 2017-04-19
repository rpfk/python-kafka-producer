# Example Kafka Producer

An easy way to produce dummy messages on Kafka using a Docker container.

## Kafka Settings

The only thing the Kafka Producer needs is the Kafka address. The address can be defined as an environment variable called `KAFKA_ADDRESS`. The Kafka address is the ip address and port that the Kafka platform listens to. In the Kafka configuration it is referred to as `advertised.listeners`. 

The easiest way to get Kafka up and running is to use the [spotify/docker-kafka](https://github.com/spotify/docker-kafka) container. An example can be found below. The default Kafka address matches the advertised host and port below, so when using the spotify/docker-kafka container, it is not necessary to specify the Kafka address.

```sh
docker run -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=192.168.21.21 --env ADVERTISED_PORT=9092 spotify/kafka
```

## Producer Settings

The producer puts messages on the Kafka bus using factories. These factories produce messages described by a script called the assignment. This assignment described where and when to publish. Currently, the assignment is obtained via a http request, therefore the assignment should be specified as URL using the the environment variable `ASSIGNMENT_URL`.

The assignment itself is a JSON file. It should specify the total duration of publishing in seconds. Furthermore the assignment file should have one or more factories specified. Each factory should specify the topics to publish on. This can be scripted using topic mapping. The attribute should be a number as string e.g. "0", "5". The attribute of an object in the topic mapping can be considered as the time at which this mapping should be active. If the , products, product weights, production rates and a topic mapping.  

### Factories

The assignment can consist of one or more factories. Each factory can be considered as a single production line that produces Kafka messages. A factory publishes messages of predefined types over predefined topics. More on topics and products can be found below. 

### Topics and Topic Mapping

Each factory has an object attribute called topics. This attribute consists of a list with the names of the Kafka topics to publish on.

To simulate dynamic behaviour, the messages are only published if they pass the topic mapping. A topic map is a boolean list with the same length as topics. If the mapping value is true, the result of the factory is published to the topic with the same index. If the mapping is false, the message is not published on the topic of that index.

Topic mapping consists of a list of attributes, which should all be a number as string e.g. "0", "5". The attribute of an object in the topic mapping can be considered as the time at which this mapping should be active. If the factory starts, time is 0, therefore topic mapping should always have an attribute "0". In the example the topic mapping at time "0" is valid up to time "5". After 5 seconds, the factory uses topic mapping "5".

### Products, Product Weights and Production Rate

Products can be considered as message types. A product specifies the value and key of a Kafka message. The currently supported Products can be found in [Factory/Product.py](https://github.com/rpfk/python-kafka-producer/blob/master/Factory/Product.py). It uses the Python package Faker to generate random data. 

The attribute product weights allows the factory to publish multiple types of messages based on a predefined distribution in the form of weights. Product weights should have the same length as the list of products. Since the product weight is the chance of producing that product on this production line, the product weights of all products should add up to 1. Furthermore, using weights is not a guarantee for a perfect mix (similar to the predefined weights) of products in the end.   

The number of messages per second can be specified in the production rate attribute. Similar to topic mapping, it has attributes which specify times at which a certain setting should be activated.

### Example Assignment

```json
{
  "time": 10,
  "factories": [
    {
      "topics": [
        "Topic1",
        "Topic3"
      ],
      "products": [
        "Text",
        "Address",
        "Name"
      ],
      "product_weights": [
        0.5,
        0.2,
        0.3
      ],
      "production_rate": {
        "0": 2,
        "12": 5
      },
      "topic_mapping": {
        "0": [
          true,
          true
        ],
        "5": [
          false,
          false
        ]
      }
    },
    {
      "topics": [
        "Topic1",
        "Topic2",
        "Topic2.1"
      ],
      "products": [
        "Address",
        "Name"
      ],
      "product_weights": [
        1,
        0
      ],
      "production_rate": {
        "0": 1,
        "12": 5
      },
      "topic_mapping": {
        "0": [
          true,
          true,
          true
        ],
        "5": [
          false,
          true,
          false
        ]
      }
    }
  ]
}
```

## Run the Kafka Producer

This repository is build and published automatically using the Docker Hub. Assuming that you have a working Docker installation, the producer can be started with the following command.

```sh
docker run rpfk/python-kafka-producer
```

Or with a Kafka address and assignment specified:

```sh
docker run --env KAFKA_ADDRESS=192.168.21.21:9092 --env ASSIGNMENT_URL='https://raw.githubusercontent.com/rpfk/python-kafka-producer-assignment/rpfk-test-600/assignment.json' rpfk/python-kafka-producer
```