"""
Unidad 1 - Ejemplo 2: Simulador de Eventos Discretos (DES)
Implementación de un simulador DES completo desde cero
"""

import heapq
from collections import namedtuple

# Definir estructura de evento
Evento = namedtuple('Evento', ['tiempo', 'tipo', 'datos'])

class SimuladorDES:
    """Simulador de Eventos Discretos genérico"""
    
    def __init__(self):
        self.tiempo_actual = 0
        self.lista_eventos = []  # Min-heap por tiempo
        self.estadisticas = {}
        
    def programar_evento(self, tiempo, tipo, datos=None):
        """Agregar evento a la lista de eventos futuros"""
        evento = Evento(tiempo, tipo, datos)
        heapq.heappush(self.lista_eventos, evento)
    
    def ejecutar(self, hasta_tiempo):
        """Ejecutar simulación hasta tiempo especificado"""
        while self.lista_eventos and self.tiempo_actual < hasta_tiempo:
            # Obtener próximo evento
            evento = heapq.heappop(self.lista_eventos)
            
            # Avanzar reloj
            self.tiempo_actual = evento.tiempo
            
            if self.tiempo_actual > hasta_tiempo:
                break
            
            # Procesar evento
            self.procesar_evento(evento)
    
    def procesar_evento(self, evento):
        """Procesar un evento (debe ser sobrescrito)"""
        raise NotImplementedError("Debe implementar procesar_evento()")

# Ejemplo: Banco con 2 cajeros
class SimuladorBanco(SimuladorDES):
    """Simulación de banco con múltiples cajeros"""
    
    def __init__(self, num_cajeros, tasa_llegada, tasa_servicio):
        super().__init__()
        self.num_cajeros = num_cajeros
        self.cajeros_libres = num_cajeros
        self.cola = []
        self.tasa_llegada = tasa_llegada
        self.tasa_servicio = tasa_servicio
        
        # Estadísticas
        self.clientes_atendidos = 0
        self.tiempos_espera = []
        self.longitud_cola_historico = []
        
    def tiempo_exponencial(self, tasa):
        """Genera tiempo exponencial"""
        import random
        return -1 / tasa * random.log(random.random())
    
    def procesar_evento(self, evento):
        """Procesar eventos del banco"""
        if evento.tipo == 'LLEGADA':
            self.procesar_llegada(evento)
        elif evento.tipo == 'FIN_SERVICIO':
            self.procesar_fin_servicio(evento)
    
    def procesar_llegada(self, evento):
        """Procesar llegada de cliente"""
        cliente_id = evento.datos
        
        # Registrar longitud de cola
        self.longitud_cola_historico.append((self.tiempo_actual, len(self.cola)))
        
        if self.cajeros_libres > 0:
            # Hay cajero libre
            self.cajeros_libres -= 1
            tiempo_servicio = self.tiempo_exponencial(self.tasa_servicio)
            
            # Programar fin de servicio
            self.programar_evento(
                self.tiempo_actual + tiempo_servicio,
                'FIN_SERVICIO',
                {'cliente_id': cliente_id, 'tiempo_llegada': self.tiempo_actual}
            )
            
            # Tiempo de espera = 0
            self.tiempos_espera.append(0)
        else:
            # Todos los cajeros ocupados, agregar a cola
            self.cola.append({
                'cliente_id': cliente_id,
                'tiempo_llegada': self.tiempo_actual
            })
        
        # Programar próxima llegada
        tiempo_proxima_llegada = self.tiempo_exponencial(self.tasa_llegada)
        self.programar_evento(
            self.tiempo_actual + tiempo_proxima_llegada,
            'LLEGADA',
            cliente_id + 1
        )
    
    def procesar_fin_servicio(self, evento):
        """Procesar fin de servicio"""
        self.clientes_atendidos += 1
        
        if self.cola:
            # Hay clientes en cola
            cliente = self.cola.pop(0)
            tiempo_espera = self.tiempo_actual - cliente['tiempo_llegada']
            self.tiempos_espera.append(tiempo_espera)
            
            # Iniciar servicio
            tiempo_servicio = self.tiempo_exponencial(self.tasa_servicio)
            self.programar_evento(
                self.tiempo_actual + tiempo_servicio,
                'FIN_SERVICIO',
                {'cliente_id': cliente['cliente_id'], 'tiempo_llegada': cliente['tiempo_llegada']}
            )
        else:
            # No hay clientes, cajero queda libre
            self.cajeros_libres += 1
    
    def mostrar_resultados(self):
        """Mostrar estadísticas"""
        import statistics
        
        print("="*60)
        print("SIMULADOR DE EVENTOS DISCRETOS - BANCO")
        print("="*60)
        print(f"\nConfiguración:")
        print(f"  Cajeros: {self.num_cajeros}")
        print(f"  Tasa de llegada: {self.tasa_llegada} clientes/hora")
        print(f"  Tasa de servicio: {self.tasa_servicio} clientes/hora")
        
        print(f"\nResultados:")
        print(f"  Clientes atendidos: {self.clientes_atendidos}")
        print(f"  Tiempo promedio de espera: {statistics.mean(self.tiempos_espera):.2f} horas")
        print(f"  Tiempo máximo de espera: {max(self.tiempos_espera):.2f} horas")
        print(f"  Longitud promedio de cola: {statistics.mean([l for t, l in self.longitud_cola_historico]):.2f}")

# Ejemplo de uso
if __name__ == "__main__":
    import random
    random.seed(42)
    
    # Crear simulador
    banco = SimuladorBanco(
        num_cajeros=2,
        tasa_llegada=10,  # 10 clientes/hora
        tasa_servicio=6   # 6 clientes/hora por cajero
    )
    
    # Programar primera llegada
    banco.programar_evento(0, 'LLEGADA', cliente_id=1)
    
    # Ejecutar simulación
    print("Ejecutando simulación de banco...")
    banco.ejecutar(hasta_tiempo=100)  # 100 horas
    
    # Mostrar resultados
    banco.mostrar_resultados()
