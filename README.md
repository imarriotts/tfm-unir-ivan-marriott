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

## Contribuciones y Feedback

Cualquier feedback o contribuciones al proyecto son bienvenidos. Si deseas contribuir, por favor, envía un pull request o abre un issue.

## Autor

- Ivan Marriott
