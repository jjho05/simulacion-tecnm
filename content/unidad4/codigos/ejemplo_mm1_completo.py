"""
U4: Ejemplo Completo de Simulación de Cola M/M/1 con SimPy
Demuestra los conceptos de la Unidad 4: lenguajes, casos prácticos y validación.
"""

import simpy
import random
import statistics

class SistemaMMI:
    def __init__(self, env, lambd, mu):
        self.env = env
        self.lambd = lambd  # Tasa de llegada
        self.mu = mu        # Tasa de servicio
        self.servidor = simpy.Resource(env, capacity=1)
        self.tiempos_espera = []
        self.tiempos_sistema = []
        
    def cliente(self, nombre, tiempo_llegada):
        """Proceso que representa el comportamiento de un cliente"""
        llegada = self.env.now
        
        with self.servidor.request() as req:
            yield req  # Esperar por el servidor
            
            inicio_servicio = self.env.now
            tiempo_espera = inicio_servicio - llegada
            self.tiempos_espera.append(tiempo_espera)
            
            # Tiempo de servicio exponencial
            tiempo_servicio = random.expovariate(self.mu)
            yield self.env.timeout(tiempo_servicio)
            
            salida = self.env.now
            tiempo_total = salida - llegada
            self.tiempos_sistema.append(tiempo_total)
            
    def generador_llegadas(self, num_clientes):
        """Genera llegadas de clientes según proceso Poisson"""
        for i in range(num_clientes):
            # Tiempo entre llegadas exponencial
            tiempo_entre_llegadas = random.expovariate(self.lambd)
            yield self.env.timeout(tiempo_entre_llegadas)
            
            # Crear nuevo cliente
            self.env.process(self.cliente(f'Cliente_{i+1}', self.env.now))

def calcular_metricas_teoricas(lambd, mu):
    """Calcula métricas teóricas M/M/1"""
    rho = lambd / mu
    if rho >= 1:
        return None  # Sistema inestable
    
    L = rho / (1 - rho)
    Lq = (rho ** 2) / (1 - rho)
    W = 1 / (mu - lambd)
    Wq = rho / (mu - lambd)
    
    return {
        'rho': rho,
        'L': L,
        'Lq': Lq,
        'W': W,
        'Wq': Wq
    }

def simular_mm1(lambd, mu, num_clientes=1000, semilla=42):
    """Ejecuta una simulación M/M/1"""
    random.seed(semilla)
    env = simpy.Environment()
    sistema = SistemaMMI(env, lambd, mu)
    
    env.process(sistema.generador_llegadas(num_clientes))
    env.run()
    
    # Calcular estadísticas de la simulación
    Wq_sim = statistics.mean(sistema.tiempos_espera)
    W_sim = statistics.mean(sistema.tiempos_sistema)
    
    return {
        'Wq': Wq_sim,
        'W': W_sim,
        'tiempos_espera': sistema.tiempos_espera
    }

if __name__ == "__main__":
    print("=== Simulación de Sistema M/M/1 ===\n")
    
    # Parámetros del sistema
    lambd = 0.8  # 0.8 clientes por minuto
    mu = 1.0     # 1 cliente por minuto
    
    print(f"Parámetros:")
    print(f"  λ (tasa de llegada) = {lambd} clientes/min")
    print(f"  μ (tasa de servicio) = {mu} clientes/min")
    print(f"  ρ (utilización) = {lambd/mu:.2f}")
    
    # Métricas teóricas
    print("\n--- Resultados Teóricos (Fórmulas M/M/1) ---")
    teoricas = calcular_metricas_teoricas(lambd, mu)
    if teoricas:
        print(f"  Wq (tiempo en cola) = {teoricas['Wq']:.4f} min")
        print(f"  W (tiempo en sistema) = {teoricas['W']:.4f} min")
        print(f"  Lq (clientes en cola) = {teoricas['Lq']:.4f}")
        print(f"  L (clientes en sistema) = {teoricas['L']:.4f}")
    
    # Simulación
    print("\n--- Resultados de Simulación ---")
    resultados = simular_mm1(lambd, mu, num_clientes=1000)
    print(f"  Wq (tiempo en cola) = {resultados['Wq']:.4f} min")
    print(f"  W (tiempo en sistema) = {resultados['W']:.4f} min")
    
    # Validación
    print("\n--- Validación (Comparación) ---")
    error_Wq = abs(resultados['Wq'] - teoricas['Wq']) / teoricas['Wq'] * 100
    error_W = abs(resultados['W'] - teoricas['W']) / teoricas['W'] * 100
    print(f"  Error en Wq: {error_Wq:.2f}%")
    print(f"  Error en W: {error_W:.2f}%")
    
    if error_Wq < 10 and error_W < 10:
        print("\n✓ El modelo de simulación está VALIDADO (error < 10%)")
    else:
        print("\n✗ Revisar el modelo (error > 10%)")
