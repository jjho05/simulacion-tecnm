"""
Unidad 5: Proyecto Integrador - Template Completo
Sistema: Línea de Producción de Laptops

Este es un ejemplo completo de proyecto de simulación siguiendo
la metodología de 7 fases del curso.

Autor: Template para estudiantes TecNM
Materia: Simulación (SCD-1022)
"""

import simpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# ============================================================================
# FASE 1: DEFINICIÓN DEL PROBLEMA
# ============================================================================

"""
PROBLEMA:
- Sistema: Línea de ensamble de laptops
- Situación actual: Producción de 80 unidades/día
- Meta: Alcanzar 100 unidades/día
- Pregunta: ¿Dónde está el cuello de botella?

OBJETIVOS:
1. Identificar estación limitante
2. Evaluar impacto de agregar 1 operador
3. Determinar configuración óptima

ALCANCE:
- Incluye: 5 estaciones de ensamble, 2 inspecciones
- Excluye: Almacén de materias primas, empaque final
- Horizonte: 8 horas (1 turno)
"""

# ============================================================================
# FASE 2: DATOS RECOLECTADOS (Simulados para este ejemplo)
# ============================================================================

# Datos de tiempos de proceso (en minutos)
# Normalmente estos vendrían de observación directa
DATOS_REALES = {
    'estacion1': {'media': 7.5, 'std': 1.2},
    'estacion2': {'media': 6.8, 'std': 1.0},
    'estacion3': {'media': 8.2, 'std': 1.5},  # Posible cuello de botella
    'estacion4': {'media': 5.5, 'std': 0.8},
    'estacion5': {'media': 6.0, 'std': 1.1},
    'inspeccion1': {'media': 3.2, 'std': 0.5},
    'inspeccion2': {'media': 2.8, 'std': 0.4},
}

TIEMPO_ENTRE_ORDENES = 6.0  # minutos (determinístico)

# ============================================================================
# FASE 3: MODELO DE SIMULACIÓN
# ============================================================================

class LineaProduccion:
    """Modelo de simulación de línea de producción"""
    
    def __init__(self, env, config='baseline'):
        self.env = env
        self.config = config
        
        # Recursos (estaciones)
        self.estacion1 = simpy.Resource(env, capacity=1)
        self.estacion2 = simpy.Resource(env, capacity=1)
        
        # Configuración de escenarios
        if config == 'est3_extra':
            self.estacion3 = simpy.Resource(env, capacity=2)  # +1 operador
        else:
            self.estacion3 = simpy.Resource(env, capacity=1)
        
        self.estacion4 = simpy.Resource(env, capacity=1)
        self.estacion5 = simpy.Resource(env, capacity=1)
        self.inspector1 = simpy.Resource(env, capacity=1)
        self.inspector2 = simpy.Resource(env, capacity=1)
        
        # Estadísticas
        self.unidades_producidas = 0
        self.tiempos_ciclo = []
        self.tiempos_por_estacion = {f'est{i}': [] for i in range(1, 6)}
        self.tiempos_espera = []
        
    def proceso_orden(self, orden_id):
        """Proceso completo de una orden"""
        llegada = self.env.now
        tiempo_espera_total = 0
        
        # Estación 1
        with self.estacion1.request() as req:
            inicio_espera = self.env.now
            yield req
            tiempo_espera_total += self.env.now - inicio_espera
            
            tiempo_proceso = np.random.normal(
                DATOS_REALES['estacion1']['media'],
                DATOS_REALES['estacion1']['std']
            )
            self.tiempos_por_estacion['est1'].append(tiempo_proceso)
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Estación 2
        with self.estacion2.request() as req:
            inicio_espera = self.env.now
            yield req
            tiempo_espera_total += self.env.now - inicio_espera
            
            tiempo_proceso = np.random.normal(
                DATOS_REALES['estacion2']['media'],
                DATOS_REALES['estacion2']['std']
            )
            self.tiempos_por_estacion['est2'].append(tiempo_proceso)
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Inspección 1
        with self.inspector1.request() as req:
            yield req
            tiempo_proceso = np.random.normal(
                DATOS_REALES['inspeccion1']['media'],
                DATOS_REALES['inspeccion1']['std']
            )
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Estación 3 (posible cuello de botella)
        with self.estacion3.request() as req:
            inicio_espera = self.env.now
            yield req
            tiempo_espera_total += self.env.now - inicio_espera
            
            tiempo_proceso = np.random.normal(
                DATOS_REALES['estacion3']['media'],
                DATOS_REALES['estacion3']['std']
            )
            self.tiempos_por_estacion['est3'].append(tiempo_proceso)
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Estación 4
        with self.estacion4.request() as req:
            inicio_espera = self.env.now
            yield req
            tiempo_espera_total += self.env.now - inicio_espera
            
            tiempo_proceso = np.random.normal(
                DATOS_REALES['estacion4']['media'],
                DATOS_REALES['estacion4']['std']
            )
            self.tiempos_por_estacion['est4'].append(tiempo_proceso)
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Estación 5
        with self.estacion5.request() as req:
            inicio_espera = self.env.now
            yield req
            tiempo_espera_total += self.env.now - inicio_espera
            
            tiempo_proceso = np.random.normal(
                DATOS_REALES['estacion5']['media'],
                DATOS_REALES['estacion5']['std']
            )
            self.tiempos_por_estacion['est5'].append(tiempo_proceso)
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Inspección 2
        with self.inspector2.request() as req:
            yield req
            tiempo_proceso = np.random.normal(
                DATOS_REALES['inspeccion2']['media'],
                DATOS_REALES['inspeccion2']['std']
            )
            yield self.env.timeout(max(0, tiempo_proceso))
        
        # Completado
        tiempo_total = self.env.now - llegada
        self.tiempos_ciclo.append(tiempo_total)
        self.tiempos_espera.append(tiempo_espera_total)
        self.unidades_producidas += 1
    
    def generador_ordenes(self):
        """Genera órdenes de producción"""
        orden_id = 0
        while True:
            yield self.env.timeout(TIEMPO_ENTRE_ORDENES)
            orden_id += 1
            self.env.process(self.proceso_orden(orden_id))

# ============================================================================
# FASE 4: VERIFICACIÓN
# ============================================================================

def verificar_modelo():
    """Verificar que el modelo funciona correctamente"""
    print("="*60)
    print("FASE 4: VERIFICACIÓN DEL MODELO")
    print("="*60)
    
    # Ejecutar simulación corta
    env = simpy.Environment()
    linea = LineaProduccion(env, config='baseline')
    env.process(linea.generador_ordenes())
    env.run(until=60)  # Solo 1 hora
    
    print(f"\n✓ Órdenes procesadas: {linea.unidades_producidas}")
    print(f"✓ Tiempo de ciclo promedio: {np.mean(linea.tiempos_ciclo):.2f} min")
    print(f"✓ Modelo funciona correctamente\n")

# ============================================================================
# FASE 5: VALIDACIÓN
# ============================================================================

def validar_modelo():
    """Validar que el modelo representa el sistema real"""
    print("="*60)
    print("FASE 5: VALIDACIÓN DEL MODELO")
    print("="*60)
    
    # Ejecutar múltiples réplicas
    resultados = []
    for rep in range(30):
        env = simpy.Environment()
        linea = LineaProduccion(env, config='baseline')
        env.process(linea.generador_ordenes())
        env.run(until=480)  # 8 horas
        resultados.append({
            'produccion': linea.unidades_producidas,
            'tiempo_ciclo': np.mean(linea.tiempos_ciclo)
        })
    
    df = pd.DataFrame(resultados)
    
    # Datos "reales" (simulados para este ejemplo)
    produccion_real = 80
    tiempo_ciclo_real = 42.5
    
    # Comparar
    produccion_sim = df['produccion'].mean()
    tiempo_ciclo_sim = df['tiempo_ciclo'].mean()
    
    print(f"\nProducción:")
    print(f"  Real:     {produccion_real} unidades/día")
    print(f"  Simulado: {produccion_sim:.1f} unidades/día")
    print(f"  Error:    {abs(produccion_sim - produccion_real)/produccion_real*100:.1f}%")
    
    print(f"\nTiempo de ciclo:")
    print(f"  Real:     {tiempo_ciclo_real:.2f} min")
    print(f"  Simulado: {tiempo_ciclo_sim:.2f} min")
    print(f"  Error:    {abs(tiempo_ciclo_sim - tiempo_ciclo_real)/tiempo_ciclo_real*100:.1f}%")
    
    # Prueba t
    t_stat, p_value = stats.ttest_1samp(df['produccion'], produccion_real)
    print(f"\nPrueba t: p-value = {p_value:.4f}")
    if p_value > 0.05:
        print("✓ MODELO VÁLIDO (no hay diferencia significativa)\n")
    else:
        print("✗ Modelo requiere ajustes\n")

# ============================================================================
# FASE 6: EXPERIMENTACIÓN
# ============================================================================

def experimentar_escenarios():
    """Evaluar diferentes escenarios de mejora"""
    print("="*60)
    print("FASE 6: EXPERIMENTACIÓN")
    print("="*60)
    
    escenarios = [
        ('Baseline', 'baseline', 0),
        ('+1 Op Est3', 'est3_extra', 25*8),  # $25/hora × 8 horas
    ]
    
    resultados = []
    
    for nombre, config, costo in escenarios:
        print(f"\nEvaluando: {nombre}...")
        
        # Ejecutar 30 réplicas
        producciones = []
        for rep in range(30):
            env = simpy.Environment()
            linea = LineaProduccion(env, config=config)
            env.process(linea.generador_ordenes())
            env.run(until=480)
            producciones.append(linea.unidades_producidas)
        
        produccion_media = np.mean(producciones)
        produccion_std = np.std(producciones)
        
        # Análisis económico
        beneficio = (produccion_media - 80) * 50  # $50 utilidad/unidad
        beneficio_neto = beneficio - costo
        
        resultados.append({
            'escenario': nombre,
            'produccion': produccion_media,
            'std': produccion_std,
            'costo': costo,
            'beneficio': beneficio,
            'beneficio_neto': beneficio_neto
        })
    
    # Mostrar resultados
    df_resultados = pd.DataFrame(resultados)
    print("\n" + "="*60)
    print("RESULTADOS DE EXPERIMENTACIÓN")
    print("="*60)
    print(df_resultados.to_string(index=False))
    
    # Encontrar mejor escenario
    mejor = df_resultados.loc[df_resultados['beneficio_neto'].idxmax()]
    print(f"\n✓ MEJOR ESCENARIO: {mejor['escenario']}")
    print(f"  Producción: {mejor['produccion']:.1f} unidades/día")
    print(f"  Beneficio neto: ${mejor['beneficio_neto']:.2f}/día")
    
    return df_resultados

# ============================================================================
# FASE 7: VISUALIZACIÓN Y REPORTE
# ============================================================================

def generar_visualizaciones(df_resultados):
    """Generar gráficos para el reporte"""
    print("\n" + "="*60)
    print("FASE 7: GENERANDO VISUALIZACIONES")
    print("="*60)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Producción por escenario
    ax = axes[0]
    ax.bar(df_resultados['escenario'], df_resultados['produccion'])
    ax.axhline(y=100, color='r', linestyle='--', linewidth=2, label='Meta (100)')
    ax.set_ylabel('Unidades Producidas/Día')
    ax.set_title('Producción por Escenario')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Gráfico 2: Beneficio neto
    ax = axes[1]
    colors = ['green' if x > 0 else 'red' for x in df_resultados['beneficio_neto']]
    ax.bar(df_resultados['escenario'], df_resultados['beneficio_neto'], color=colors)
    ax.set_ylabel('Beneficio Neto ($/día)')
    ax.set_title('Análisis Económico')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('resultados_proyecto.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: resultados_proyecto.png")
    plt.show()

# ============================================================================
# MAIN: EJECUTAR PROYECTO COMPLETO
# ============================================================================

def main():
    """Ejecutar proyecto completo de simulación"""
    print("\n" + "="*60)
    print("PROYECTO DE SIMULACIÓN: LÍNEA DE PRODUCCIÓN")
    print("="*60 + "\n")
    
    # Fase 4: Verificación
    verificar_modelo()
    
    # Fase 5: Validación
    validar_modelo()
    
    # Fase 6: Experimentación
    df_resultados = experimentar_escenarios()
    
    # Fase 7: Visualización
    generar_visualizaciones(df_resultados)
    
    print("\n" + "="*60)
    print("PROYECTO COMPLETADO")
    print("="*60)
    print("\nPróximos pasos:")
    print("1. Revisar gráfico generado")
    print("2. Preparar presentación")
    print("3. Documentar supuestos y limitaciones")
    print("4. Preparar respuestas a preguntas\n")

if __name__ == "__main__":
    main()
