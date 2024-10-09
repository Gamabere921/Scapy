
import sys
import argparse
from scapy.all import IP, ICMP, TCP, UDP, sr1, conf

def enviar_paquete(destino, tipo_paquete, puerto, numero_paquetes, iface=None):
    """
    Envía un número especificado de paquetes a la dirección IP de destino y muestra el número total de paquetes enviados.

    Args:
    destino (str): Dirección IP de destino.
    tipo_paquete (str): Tipo de paquete ('ICMP', 'TCP', 'UDP').
    puerto (int): Puerto a utilizar (para TCP/UDP).
    numero_paquetes (int): Número de paquetes a enviar.
    iface (str): Interfaz de red a utilizar.
    """
    if iface:
        conf.iface = iface

    enviados = 0  # Contador para los paquetes enviados
    payload = b"A" * 1460  # Tamaño seguro de payload para evitar fragmentación

    for i in range(numero_paquetes):
        if tipo_paquete.upper() == "ICMP":
            paquete = IP(dst=destino)/ICMP()/payload
        elif tipo_paquete.upper() == "TCP":
            paquete = IP(dst=destino)/TCP(dport=puerto)/payload
        elif tipo_paquete.upper() == "UDP":
            paquete = IP(dst=destino)/UDP(dport=puerto)/payload
        else:
            print(f"Tipo de paquete no soportado: {tipo_paquete}")
            return

        respuesta = sr1(paquete, timeout=2, verbose=False)
        
        # Independientemente de si se recibe una respuesta, contar el paquete como enviado
        enviados += 1

    print(f"Se enviaron {enviados} paquetes a {destino} usando {tipo_paquete.upper()} en el puerto {puerto}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Envía paquetes de red (ICMP, TCP, UDP) a un destino especificado.')
    parser.add_argument('destino', type=str, help='Dirección IP de destino')
    parser.add_argument('tipo_paquete', type=str, choices=['ICMP', 'TCP', 'UDP'], help='Tipo de paquete a enviar')
    parser.add_argument('puerto', type=int, help='Puerto a utilizar (específico para TCP/UDP)')
    parser.add_argument('numero_paquetes', type=int, help='Número de paquetes a enviar')
    parser.add_argument('-i', '--iface', type=str, default='wlp11s0', help='Interfaz de red a utilizar (por defecto: wlp11s0)')
    
    args = parser.parse_args()
    
    enviar_paquete(args.destino, args.tipo_paquete, args.puerto, args.numero_paquetes, args.iface)
