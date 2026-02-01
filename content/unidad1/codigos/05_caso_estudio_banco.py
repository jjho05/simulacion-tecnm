"""
Unidad 1 - Ejemplo 5: Caso de Estudio Completo - Banco
Sistema real con análisis completo
"""
import random, statistics

class Banco:
    def __init__(self, cajeros, lambd, mu):
        self.cajeros_libres = cajeros
        self.cola, self.stats = [], {'espera': [], 'sistema': []}
        self.lambd, self.mu = lambd, mu
    
    def simular(self, tiempo_max):
        t, t_lleg, t_fin = 0, -1/self.lambd * random.log(random.random()), float('inf')
        while t < tiempo_max:
            if t_lleg < t_fin:
                t = t_lleg
                if self.cajeros_libres > 0:
                    self.cajeros_libres -= 1
                    t_fin = t - 1/self.mu * random.log(random.random())
                    self.stats['espera'].append(0)
                else:
                    self.cola.append(t)
                t_lleg = t - 1/self.lambd * random.log(random.random())
            else:
                t = t_fin
                if self.cola:
                    t_arr = self.cola.pop(0)
                    self.stats['espera'].append(t - t_arr)
                    t_fin = t - 1/self.mu * random.log(random.random())
                else:
                    self.cajeros_libres += 1
                    t_fin = float('inf')

if __name__ == "__main__":
    random.seed(42)
    b = Banco(cajeros=3, lambd=10, mu=4)
    b.simular(480)
    print(f"Banco: {len(b.stats['espera'])} clientes")
    print(f"Espera promedio: {statistics.mean(b.stats['espera']):.2f} min")
