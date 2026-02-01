"""
Unidad 4 - Ejemplo 1: SimPy Básico
Introducción a SimPy con ejemplo M/M/1
"""
try:
    import simpy
    import random
    
    def cliente(env, nombre, servidor):
        llegada = env.now
        with servidor.request() as req:
            yield req
            espera = env.now - llegada
            yield env.timeout(random.expovariate(1/5))
            print(f"{nombre}: esperó {espera:.1f} min")
    
    def generador(env, servidor):
        for i in range(10):
            yield env.timeout(random.expovariate(1/6))
            env.process(cliente(env, f'Cliente {i+1}', servidor))
    
    env = simpy.Environment()
    servidor = simpy.Resource(env, capacity=1)
    env.process(generador(env, servidor))
    env.run()
    print("\n✓ Simulación completada")
    
except ImportError:
    print("SimPy no instalado. Ejecutar: pip install simpy")
