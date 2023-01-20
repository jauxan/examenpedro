Hola, esto es el ejercicio 3 del examen de pedro creado por Jaume.

Para realizar una conexión ssh a un servidor es necesario tener instalado el ssh (tanto tu como el servidor).
Instalar SSH:
- sudo apt update
- sudo apt install openssh-server


Para crear un usuario llamado "admin":
- sudo adduser admin
Rellenamos sus datos y ponemos 2 veces la contraseña.


Para evitar que el usuario root pueda acceder via SSH es necesario modificar /etc/ssh/sshd_config
Modificamos la línea "PermitRootLogin":
- PermitRootLogin no
