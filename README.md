# TFM-UNIR - Gestión de Infraestructura en la Nube con Terraform y CDKTF

Este repositorio contiene el proyecto desarrollado para mi Trabajo de Fin de Máster (TFM) en la Universidad Internacional de La Rioja (UNIR). El proyecto se enfoca en la implementación y gestión de infraestructura en la nube utilizando CDK para Terraform (CDKTF).

## Descripción

El objetivo principal de este proyecto es demostrar la eficiencia y eficacia de la Infraestructura como Código (IaC) en la gestión de recursos en la nube. Se utilizan tecnologías como AWS, Terraform y CDKTF para automatizar la creación y configuración de instancias EC2, así como para gestionar la seguridad y la red en un entorno AWS.

## Requisitos Previos

- **Configuración de la Cuenta AWS**: Asegúrate de tener configurada tu cuenta de AWS con las credenciales apropiadas. Puedes encontrar las instrucciones de instalación en [Configurar AWS-CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
- **Node.js**: Este proyecto utiliza Node.js versión `18.18.2`. Se recomienda usar `nvm` para gestionar las versiones de Node.js. Hay un archivo `.nvmrc` incluido en el repositorio.
- **CDK para Terraform**: Necesitas tener CDKTF instalado. Puedes encontrar las instrucciones de instalación en [Instalar CDKTF](https://developer.hashicorp.com/terraform/tutorials/cdktf/cdktf-install).

## Estructura del Proyecto

- `main.ts`: Archivo principal que contiene la definición de la infraestructura utilizando CDKTF.
- `cdktf.json`: Configuración para CDKTF.
- `package.json`: Define los scripts de utilidad para ejecutar comandos de Terraform a través de CDKTF.

## Cómo Utilizar

Para desplegar la infraestructura definida en este proyecto, sigue estos pasos:

1. Clona el repositorio.
2. Instala las dependencias con `npm install`.
3. Ejecuta `npm run plan` para revisar los cambios de infraestructura propuestos.
4. Ejecuta `npm run deploy` para desplegar la infraestructura en AWS.

## Scripts de Utilidad
En la carpeta `scripts` se incluyen algunos scripts de utilidad para probar la infraestructura desplegada. Estos scripts estan escritos en Python, las dependencias se pueden instalar con `pip install -r requirements.txt`. que se encuentran en la carpeta `scripts`.

Para ejecutar los scripts, es necesario hacer ssh a la instancia EC2 desplegada y ejecutarlos desde allí ya que se conectan a Kafka a través de la red privada a su vez es necesario crear un topic de Kafka con el nombre `michigan-lake-topic` para poder enviar y consumir mensajes.

En total hay 2 scripts:

*  `consumer.py`: Script que consume mensajes de un topic de Kafka.
* `producer.py`: Script que produce mensajes en un topic de Kafka.

### Productor de Kafka

El script `producer.py` lee un archivo csv con datos de `input.csv` más detalles de este dataset en [Beach Weather Stations - Automated Sensors](https://data.cityofchicago.org/Parks-Recreation/Beach-Weather-Stations-Automated-Sensors/k7hf-8y75/about_data) y los envía a un topic de Kafka. Al procesar el archivo ordena los registros por timestamps y los envía al topic de Kafka con un delay de 1 segundo entre cada mensaje (este delay se puede modificar en el script).

### Consumidor de Kafka

El script `consumer.py` consume los mensajes de Kafka los procesa y los guarda en una base de datos PostgreSQL. Para ello, crea una tabla en la base de datos con el siguiente esquema:

```sql
weather_data (
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
    );
```

Por temas de seguridad, las credenciales de la base de datos no se incluyen en el script, por lo que es necesario modificar el script para incluir las credenciales actualizadas.

Con estos scripts se puede probar la infraestructura desplegada y comprobar que funciona correctamente enviando y consumiendo mensajes desde un topic de Kafka.


## Contribuciones y Feedback

Cualquier feedback o contribuciones al proyecto son bienvenidos. Si deseas contribuir, por favor, envía un pull request o abre un issue.

## Autor

- Ivan Marriott
