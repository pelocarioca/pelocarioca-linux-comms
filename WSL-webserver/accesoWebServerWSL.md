### Arreglar el problema cuando se quiere acceder a un servidor en WSL2

Se abre el "Firewall de Windows con seguridad avanzada", allí:

1. Se crea una __norma de entrada__.
2. Se selecciona el puerto de acceso (80/8080/443).
3. Se __permite la entrada__.
4. Se seleccionan las tres opciones __dominio, privada y pública__.
5. Se le añade un nombre adecuado y una descripción.


Una vez creada la norma se debería poder acceder al servidor apache desde el navegador, escribiendo en la barra de búsqueda ip:port (por ejemplo 172.19.152.209:8080).

Para instalar el servidor apache se ejecuta en el WSL:

`# apt update`

`# apt install apache2`

`# apache2`

Se comprueba con:

`# curl 127.0.0.1`

En caso de que de error el último comando se comprueba el firewall (__ufw__).

En caso de que falle el comando apache2 con el error _[core:warn] [pid 76] AH00111: Config variable ${APACHE_RUN_DIR} is not defined apache2: Syntax error on line 80 of /etc/apache2/apache2.conf: DefaultRuntimeDir must be a valid directory, absolute or relative to ServerRoot_ se ejecuta esto:

`# mkdir /var/run/apache2`

Por último, para acceder a los archivos del servidor desde Windows se debe:

1. Pulsar __WIN + R__.
2. Ejecutar __\\wsl$__.

Se abrirá el explorador de archivos de red, en el que se encontrará el sistema de archivos del WSL2.
