"""
Unidad 1 - Ejemplo 1: Simulación Básica de Cola M/M/1
Demuestra los conceptos fundamentales de simulación de eventos discretos
"""

import random
import statistics

class SimulacionCola:
    """Simulación simple de cola M/M/1 sin librerías externas"""
    
    def __init__(self, tasa_llegada, tasa_servicio, tiempo_simulacion):
        self.tasa_llegada = tasa_llegada  # λ (clientes/hora)
        self.tasa_servicio = tasa_servicio  # μ (clientes/hora)
        self.tiempo_simulacion = tiempo_simulacion
        
        # Estadísticas
        self.tiempos_espera = []
        self.tiempos_sistema = []
        self.clientes_atendidos = 0
        
    def tiempo_exponencial(self, tasa):
        """Genera tiempo aleatorio con distribución exponencial"""
        return -1 / tasa * random.log(random.random())
    
    def simular(self):
        """Ejecuta la simulación"""
        tiempo_actual = 0
        tiempo_proximo_llegada = self.tiempo_exponencial(self.tasa_llegada)
        tiempo_fin_servicio = float('inf')
        
        cola = []
        servidor_ocupado = False
        
        while tiempo_actual < self.tiempo_simulacion:
            # Determinar próximo evento
            if tiempo_proximo_llegada < tiempo_fin_servicio:
                # Evento: Llegada
                tiempo_actual = tiempo_proximo_llegada
                
                if not servidor_ocupado:
                    # Servidor libre, atender inmediatamente
                    servidor_ocupado = True
                    tiempo_servicio = self.tiempo_exponencial(self.tasa_servicio)
                    tiempo_fin_servicio = tiempo_actual + tiempo_servicio
                    self.tiempos_espera.append(0)
                    self.tiempos_sistema.append(tiempo_servicio)
                else:
                    # Servidor ocupado, agregar a cola
                    cola.append(tiempo_actual)
                
                # Programar próxima llegada
                tiempo_proximo_llegada = tiempo_actual + self.tiempo_exponencial(self.tasa_llegada)
            
            else:
                # Evento: Fin de servicio
                tiempo_actual = tiempo_fin_servicio
                self.clientes_atendidos += 1
                
                if cola:
                    # Hay clientes en cola
                    tiempo_llegada_cliente = cola.pop(0)
                    tiempo_espera = tiempo_actual - tiempo_llegada_cliente
                    tiempo_servicio = self.tiempo_exponencial(self.tasa_servicio)
                    
                    self.tiempos_espera.append(tiempo_espera)
                    self.tiempos_sistema.append(tiempo_espera + tiempo_servicio)
                    
                    tiempo_fin_servicio = tiempo_actual + tiempo_servicio
                else:
                    # No hay clientes, servidor queda libre
                    servidor_ocupado = False
                    tiempo_fin_servicio = float('inf')
    
    def mostrar_resultados(self):
        """Muestra estadísticas de la simulación"""
        print("="*60)
        print("RESULTADOS DE LA SIMULACIÓN M/M/1")
        print("="*60)
        print(f"\nParámetros:")
        print(f"  λ (tasa llegada): {self.tasa_llegada} clientes/hora")
        print(f"  μ (tasa servicio): {self.tasa_servicio} clientes/hora")
        print(f"  ρ (utilización): {self.tasa_llegada/self.tasa_servicio:.2%}")
        
        print(f"\nResultados simulados:")
        print(f"  Clientes atendidos: {self.clientes_atendidos}")
        print(f"  Tiempo promedio en cola: {statistics.mean(self.tiempos_espera):.2f} horas")
        print(f"  Tiempo promedio en sistema: {statistics.mean(self.tiempos_sistema):.2f} horas")
        
        # Comparar con teoría
        rho = self.tasa_llegada / self.tasa_servicio
        Wq_teorico = rho / (self.tasa_servicio * (1 - rho))
        W_teorico = 1 / (self.tasa_servicio - self.tasa_llegada)
        
        print(f"\nComparación con teoría:")
        print(f"  Wq teórico: {Wq_teorico:.2f} horas")
        print(f"  W teórico: {W_teorico:.2f} horas")
        
        error_wq = abs(statistics.mean(self.tiempos_espera) - Wq_teorico) / Wq_teorico * 100
        print(f"  Error Wq: {error_wq:.1f}%")

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración
    random.seed(42)  # Para reproducibilidad
    
    # Crear y ejecutar simulación
    sim = SimulacionCola(
        tasa_llegada=3,      # 3 clientes/hora
        tasa_servicio=4,     # 4 clientes/hora
        tiempo_simulacion=1000  # 1000 horas
    )
    
    print("Ejecutando simulación...")
    sim.simular()
    sim.mostrar_resultados()
