from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'),
   bootstrap_servers='localhost:9092')

future = producer.send("topic1", value={"hello": "producer2"})
producer.flush()
result = future.get(timeout=60)
print(result)