### Arreglar el problema E: No se pudo bloquear /var/lib/dpkg/lock-frontend - open (11: Recurso no disponible temporalmente)

```
$ sudo fuser -vki /var/lib/dpkg/lock

$ sudo rm -f /var/lib/dpkg/lock`

$ sudo dpkg --configure -a

$ sudo apt-get autoremove
```
