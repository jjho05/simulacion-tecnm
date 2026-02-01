# Unidad 3: Generación de Variables Aleatorias

## Descripción

Esta unidad cubre los métodos para generar variables aleatorias de diferentes distribuciones de probabilidad, esenciales para modelar la aleatoriedad en simulaciones.

## Contenido

### [3.1 Conceptos básicos de variables aleatorias](3.1.md)
- Variables aleatorias discretas y continuas
- Función de densidad de probabilidad (PDF)
- Función de distribución acumulada (CDF)
- Parámetros: media, varianza, momentos

### [3.2 Variables aleatorias discretas](3.2.md)
- Distribución Uniforme discreta
- Distribución Bernoulli
- Distribución Binomial
- Distribución Geométrica
- Distribución Poisson

### [3.3 Variables aleatorias continuas](3.3.md)
- Distribución Uniforme continua
- Distribución Exponencial
- Distribución Normal
- Distribución Triangular
- Distribución Weibull
- Distribución Lognormal

### [3.4 Métodos para generar variables aleatorias](3.4.md) *(Archivo padre)*
- Comparación de métodos
- Criterios de selección
- Framework de validación

#### [3.4.1 Método de la transformada inversa](3.4.1.md)
- Teorema fundamental
- Algoritmo general
- Ejemplos: Exponencial, Weibull, Triangular
- Implementación en Python

#### [3.4.2 Método de convolución](3.4.2.md)
- Distribución Erlang
- Distribución Binomial
- Aproximación por Teorema del Límite Central

#### [3.4.3 Método de composición](3.4.3.md)
- Distribución Hiperexponencial
- Distribuciones empíricas
- Distribuciones bimodales

### [3.5 Procedimientos especiales](3.5.md)
- Método de Aceptación-Rechazo
- Método de Box-Muller (Normal)
- Método Polar de Marsaglia
- Generación de Poisson

### [3.6 Pruebas estadísticas al generador de variables](3.6.md)
- Prueba Chi-cuadrada (bondad de ajuste)
- Prueba Kolmogorov-Smirnov
- Gráficos Q-Q
- Prueba de momentos
- Batería completa de validación

## Objetivos de Aprendizaje

Al completar esta unidad, serás capaz de:
- ✅ Generar variables de distribuciones comunes
- ✅ Seleccionar el método apropiado según la distribución
- ✅ Implementar generadores en Python
- ✅ Validar generadores usando pruebas estadísticas

## Recursos Adicionales

- **Software:** Python (NumPy, SciPy, Matplotlib)
- **Libros:** Devroye (1986), Law (2015)
- **Tiempo estimado:** 12-14 horas

---

---

<div align="center">

⬅️ [2.3.3 Solución Problemas](../unidad2/2.3.3.md) &nbsp;&nbsp;|&nbsp;&nbsp; [3.1 Conceptos VA](3.1.md) ➡️

</div>
