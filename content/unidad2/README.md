# Unidad 2: Números Pseudoaleatorios

## Descripción

Esta unidad cubre la generación y validación de números pseudoaleatorios, fundamentales para cualquier simulación estocástica. Incluye métodos de generación, pruebas estadísticas y aplicaciones del método Monte Carlo.

## Contenido

### [2.1 Métodos de generación de números pseudoaleatorios](2.1.md)
- Generador Congruencial Lineal (LCG)
- Generador Congruencial Multiplicativo
- Generadores modernos (Mersenne Twister, PCG)
- Implementación en Python

### [2.2 Pruebas de validación](2.2.md) *(Archivo padre)*
- Importancia de validar generadores
- Tipos de pruebas: uniformidad, aleatoriedad, independencia
- Metodología de validación

#### [2.2.1 Pruebas de uniformidad](2.2.1.md)
- Prueba Chi-cuadrada
- Prueba Kolmogorov-Smirnov
- Ejemplos numéricos completos

#### [2.2.2 Pruebas de aleatoriedad](2.2.2.md)
- Prueba de póker
- Prueba de huecos (gaps)
- Prueba de corridas arriba/abajo

#### [2.2.3 Pruebas de independencia](2.2.3.md)
- Prueba de corridas arriba/abajo de la media
- Prueba de autocorrelación
- Prueba de series

### [2.3 Generación de variables aleatorias y método Monte Carlo](2.3.md) *(Archivo padre)*
- Introducción al método Monte Carlo
- Relación con generación de variables aleatorias

#### [2.3.1 Características del método Monte Carlo](2.3.1.md)
- Ley de los Grandes Números
- Teorema del Límite Central
- Convergencia y precisión

#### [2.3.2 Aplicaciones del método Monte Carlo](2.3.2.md)
- Finanzas (valoración de opciones)
- Física (simulación de partículas)
- Ingeniería (análisis de riesgo)
- Gráficos por computadora (ray tracing)

#### [2.3.3 Solución de problemas mediante Monte Carlo](2.3.3.md)
- Estimación de π
- Integración numérica
- Problema de Buffon
- Simulación de proyectos

## Objetivos de Aprendizaje

Al completar esta unidad, serás capaz de:
- ✅ Implementar generadores de números pseudoaleatorios
- ✅ Validar generadores usando pruebas estadísticas
- ✅ Aplicar el método Monte Carlo a problemas reales
- ✅ Interpretar resultados de pruebas estadísticas

## Recursos Adicionales

- **Software:** Python (NumPy, SciPy)
- **Libros:** Knuth (1997), Devroye (1986)
- **Tiempo estimado:** 10-12 horas

---

---

<div align="center">

⬅️ [1.7 Decisión de Uso](../unidad1/1.7.md) &nbsp;&nbsp;|&nbsp;&nbsp; [2.1 Generación de Números](2.1.md) ➡️

</div>
