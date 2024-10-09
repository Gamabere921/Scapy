# SCAPY

# Packet Sender Scripts

Este repositorio contiene dos scripts en Python que permiten enviar paquetes de red utilizando diferentes protocolos (ICMP, TCP, UDP) mediante la biblioteca **Scapy**. 

## Inspiración

Estos scripts fueron creados para facilitar el envío de paquetes de red con fines educativos o de prueba de **conectividad** o de **estres**. Permiten al usuario seleccionar el tipo de paquete a enviar y configurar tanto la interfaz de red como el número de paquetes.

## Objetivo

El objetivo de estos scripts es ofrecer una herramienta simple para el envío de paquetes con soporte para diferentes protocolos. En el caso de TCP y UDP, se puede elegir entre usar un puerto específico o generar puertos aleatorios automáticamente. Esto con el fin de poder analizar los paquetes que se envían o generar una prueba de estrés.

### Dato

Para la prueba de estrés se recomienda que se ejecute alguno de los dos scripts en 5 dispositivos al mismo tiempo para llegar a generar una saturación en la banda ancha de la red. Dependiendo del dispositivo y reglas de firewall implementados, puede tener resultados en 5 minutos o no debido a que tengan medidas en contra ataques DDoS

Estos Scripts fueron diseñados con fines educativos y de analisis, no me hago responsable de algun uso indebido.

## Recursos

- [Scapy](https://scapy.net)
- https://github.com/secdev/scapy
- [Ataques DDoS](https://latam.kaspersky.com/resource-center/threats/ddos-attacks?srsltid=AfmBOorDCuhyqzXk0F257KMirNrMXNevy25eW_0XV8wjrZuoDZC-AcWN)

## Forma de uso

### Ejecución

Para ejecutar cualquiera de los scripts, sigue estos pasos:

1. Clona este repositorio:
    
    ```bash
    git clone https://github.com/Gamabere921/Scapy.git
    cd Scapy
    
    ```
    
2. Instala las dependencias necesarias (asegúrate de tener `pip` instalado):
    
    ```bash
    pip install scapy
    or
    sudo apt install python3-scapy 
    
    ```
    
3. Ejecuta el script con el siguiente comando:
    
    ```bash
    sudo python3 random-packet.py <destino> <tipo_paquete> <numero_paquetes> [-i <iface>]
    
    ```
    
    Para el segundo script, donde se especifica un puerto para TCP/UDP:
    
    ```bash
    sudo python port-packet.py <destino> <tipo_paquete> <puerto> <numero_paquetes> [-i <iface>]
    
    ```
    

### Argumentos:

- `<destino>`: Dirección IP de destino.
- `<tipo_paquete>`: Tipo de paquete a enviar (ICMP, TCP, UDP).
- `<numero_paquetes>`: Número de paquetes a enviar.
- `<puerto>` (solo para TCP/UDP en el segundo script): Puerto específico a utilizar.
- `i <iface>`: (Opcional) Interfaz de red a utilizar. Por defecto es 'wlp11s0'.

## Ejemplo de uso

Para enviar 10 paquetes ICMP a la IP `192.168.1.1`:

```bash
sudo python3 random-packet.py 192.168.1.1 ICMP 10

```
