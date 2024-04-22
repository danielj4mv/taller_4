# Entrega Taller 4
## Guía para desplegar 
1. **Clonar el repositorio en la carpeta desde la que se quiere ejecutar el notebook**
   ```console
   git clone https://github.com/danielj4mv/taller_4.git
   ```
2. **Ingresar desde la terminal en la carpeta con el repositorio**
   ```docker
   cd taller_4
   ```
3. **Crear red para comunicar los servicios de ambos docker-compose**
   ```console
   docker network create p2_default
   ```
4. **Crear contenedor del servicio de inferencia**
   ```console
   docker compose up -d
   ```
5. **Construir imágenes y contenedores de los servicios de locust**

   ```docker
   docker compose -f docker-compose-pruebas.yaml build
   docker compose -f docker-compose-pruebas.yaml up
   ```

6. **Ingresar a la interfaz de locust desde su navegador en el puerto 8089**
   
   Si es desde su maquina local sería desde el localhost, si es desde un máquina virtual seria en:
   ```
   http://ip_de_la_mv:8089/
   ```
6. **Crear una nueva prueba de carga con los siguientes valores:**
   
   ![prueba](/images/res.png)
   
  Al presionar START comenzará la prueba de carga la cual podrá obsevar desde la interfaz de locust

