import csv
import json
import os
import time
from kafka import KafkaProducer
import logging
from datetime import datetime

# configure logging
logging.basicConfig(level=logging.INFO)

# initialize kafka producer
producer = KafkaProducer(bootstrap_servers=['kafka1:9092','kafka2:9092','kafka3:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# valida si el fichero csv existe
if not os.path.isfile('input.csv'):
    logging.error("input.csv file does not exist")
    exit(1)

# lee el fichero csv y lo envía a kafka
with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sorted_rows = sorted(reader, key=lambda row: datetime.strptime(row['Measurement Timestamp Label'], '%m/%d/%Y %I:%M %p'))
    logging.info(f"rows were sorted, first date: {sorted_rows[0]['Measurement Timestamp Label']}, last date: {sorted_rows[-1]['Measurement Timestamp Label']}")
    for i, row in enumerate(sorted_rows, start=1):
        try:
            producer.send('michigan-lake-topic', row)
            logging.info(f"Row sent: {row}")
            time.sleep(5)
        except Exception as e:
            logging.error(f"Error sending row {i}: {e}")
            time.sleep(5)

producer.close()
