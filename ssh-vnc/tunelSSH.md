La sintaxis del comando es:

`ssh -L pLocal:hRemoto:pRemoto servSSH`

Donde:
 - __pLocal__ es el puerto al que se conecta el cliente.
 - __hRemoto__ es la dirección del host remoto DESDE el __servSSH__. Si el servidor SSH y el host remoto son el mismo, será `localhost`.
 - __pRemoto__ es el puerto remoto, el tiene en escucha el host remoto.
 - __servSSH__ es el servidor SSH remoto.

Ejemplo para conectar un cliente con un servidor VNC (escuchando al puerto `5900`) que tiene en funcionamiento su propio servidor SSH:

`ssh -L 5900:localhost:5900 cassio@pelocarioca.ddns.net`
