from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(group_id='group-id', bootstrap_servers=['000.000.000.000:0000'], auto_offset_reset='earliest')
consumer.subscribe(topics=(['topic1', 'topic2']))

index = 0
while True:
    msg = consumer.poll(timeout_ms=5, max_records=10)  # 从kafka获取消息
    print(msg)
    time.sleep(2)
    index += 1
    print('--------poll index is %s----------' % index)
