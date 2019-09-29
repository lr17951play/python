from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(group_id='123456', bootstrap_servers=['10.43.35.25:4531'])
consumer.subscribe(topics=('test_rhj',))

index = 0
while True:
    msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
    print(msg)
    time.sleep(2)
    index += 1
    print('--------poll index is %s----------' % index)