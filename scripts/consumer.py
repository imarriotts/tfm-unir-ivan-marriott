from kafka import KafkaConsumer
import json
import psycopg2
import logging

# configuración de logging
logging.basicConfig(level=logging.INFO)

# inicializar consumidor de kafka
consumer = KafkaConsumer('michigan-lake-topic',
                         bootstrap_servers=['kafka1:9092','kafka2:9092','kafka3:9092'],
                        #auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# inicializar conexión a base de datos
conn = psycopg2.connect(
    host="somehost",
    dbname="tfm",
    user="ivan",
    password="somepassword"
)
cur = conn.cursor()

# por temas de pruebas, se borra la tabla si existe
# cur.execute("DROP TABLE IF EXISTS weather_data")

# crear tabla
cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        station_name VARCHAR(255),
        measurement_timestamp TIMESTAMP,
        air_temperature FLOAT,
        wet_bulb_temperature FLOAT,
        humidity INT,
        rain_intensity FLOAT,
        interval_rain FLOAT,
        total_rain FLOAT,
        precipitation_type INT,
        wind_direction INT,
        wind_speed FLOAT,
        maximum_wind_speed FLOAT,
        barometric_pressure FLOAT,
        solar_radiation INT,
        heading INT,
        battery_life FLOAT,
        measurement_timestamp_label VARCHAR(255),
        measurement_id VARCHAR(255) PRIMARY KEY
    )
""")
conn.commit()

def get_float_value(value):
    """Convierte un string a float. Devuelve None si el string está vacío o es None."""
    try:
        return float(value) if value != '' else None
    except ValueError:
        return None

def get_int_value(value):
    """Convierte un string a int. Devuelve None si el string está vacío o es None."""
    try:
        return int(value) if value != '' else None
    except ValueError:
        return None


# Leer mensajes de kafka
for message in consumer:
    data = message.value

    # Convertir los valores a los tipos de datos correctos
    air_temperature = get_float_value(data['Air Temperature'])
    wet_bulb_temperature = get_float_value(data['Wet Bulb Temperature'])
    rain_intensity = get_float_value(data['Rain Intensity'])
    interval_rain = get_float_value(data['Interval Rain'])
    total_rain = get_float_value(data['Total Rain'])
    wind_speed = get_float_value(data['Wind Speed'])
    maximum_wind_speed = get_float_value(data['Maximum Wind Speed'])
    barometric_pressure = get_float_value(data['Barometric Pressure'])
    solar_radiation = get_float_value(data['Solar Radiation'])
    battery_life = get_float_value(data['Battery Life'])
    humidity = get_int_value(data['Humidity'])
    precipitation_type = get_int_value(data['Precipitation Type'])
    wind_direction = get_int_value(data['Wind Direction'])
    heading = get_int_value(data['Heading'])

    # Upsert en la base de datos
    cur.execute("""
        INSERT INTO weather_data (
            station_name, measurement_timestamp, air_temperature, wet_bulb_temperature, humidity,
            rain_intensity, interval_rain, total_rain, precipitation_type, wind_direction,
            wind_speed, maximum_wind_speed, barometric_pressure, solar_radiation, heading,
            battery_life, measurement_timestamp_label, measurement_id
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        ) ON CONFLICT (measurement_id) DO UPDATE SET
            station_name = EXCLUDED.station_name,
            measurement_timestamp = EXCLUDED.measurement_timestamp,
            air_temperature = EXCLUDED.air_temperature,
            wet_bulb_temperature = EXCLUDED.wet_bulb_temperature,
            humidity = EXCLUDED.humidity,
            rain_intensity = EXCLUDED.rain_intensity,
            interval_rain = EXCLUDED.interval_rain,
            total_rain = EXCLUDED.total_rain,
            precipitation_type = EXCLUDED.precipitation_type,
            wind_direction = EXCLUDED.wind_direction,
            wind_speed = EXCLUDED.wind_speed,
            maximum_wind_speed = EXCLUDED.maximum_wind_speed,
            barometric_pressure = EXCLUDED.barometric_pressure,
            solar_radiation = EXCLUDED.solar_radiation,
            heading = EXCLUDED.heading,
            battery_life = EXCLUDED.battery_life,
            measurement_timestamp_label = EXCLUDED.measurement_timestamp_label
        """, (
        data['Station Name'], data['Measurement Timestamp'], air_temperature,
        wet_bulb_temperature, humidity, rain_intensity,
        interval_rain, total_rain, precipitation_type,
        wind_direction, wind_speed, maximum_wind_speed,
        barometric_pressure, solar_radiation, heading,
        battery_life, data['Measurement Timestamp Label'], data['Measurement ID']
    ))
    conn.commit()
    logging.info(f"Inserted: {data['Measurement ID']}")

cur.close()
conn.close()