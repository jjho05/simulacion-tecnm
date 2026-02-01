"""
U1: Ejemplo de Lógica de Eventos Discretos
Este script demuestra conceptualmente cómo funciona un sistema de simulación (1.6)
Identificando eventos de llegada y servicio.
"""

import random

def simular_fila_basica(tiempo_limite):
    reloj = 0
    cola = 0
    eventos = [] # Lista de eventos futuros: (tiempo, tipo)
    
    # Programar primera llegada
    eventos.append((random.uniform(1, 5), "LLEGADA"))
    
    print(f"{'Tiempo':<10} | {'Evento':<15} | {'Cola':<5}")
    print("-" * 35)

    while eventos and reloj < tiempo_limite:
        # Ordenar eventos por tiempo y tomar el más próximo
        eventos.sort()
        tiempo_evento, tipo = eventos.pop(0)
        reloj = tiempo_evento
        
        if tipo == "LLEGADA":
            cola += 1
            # Programar siguiente llegada
            eventos.append((reloj + random.uniform(2, 6), "LLEGADA"))
            # Si el servidor estaba libre, programar fin de servicio
            if cola == 1:
                eventos.append((reloj + random.uniform(1, 4), "FIN_SERVICIO"))
        
        elif tipo == "FIN_SERVICIO":
            cola -= 1
            # Si hay alguien más, programar su fin de servicio
            if cola > 0:
                eventos.append((reloj + random.uniform(1, 4), "FIN_SERVICIO"))
        
        print(f"{reloj:<10.2f} | {tipo:<15} | {cola:<5}")

if __name__ == "__main__":
    print("Iniciando simulación conceptual de Unidad 1...\n")
    simular_fila_basica(20)
    print("\nSimulación finalizada.")
