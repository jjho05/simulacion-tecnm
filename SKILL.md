---
name: simulacion-tecnm
description: Skill de soporte experto para la asignatura de Simulación (SCD-1022) - Ingeniería en Sistemas Computacionales del TecNM. Proporciona herramientas para el análisis, modelado y experimentación de sistemas mediante simulación de eventos discretos. Cubre generación de números pseudoaleatorios, pruebas estadísticas, variables aleatorias y marcos de trabajo para proyectos de simulación.
---

# Simulación: Guía de Referencia (SCD-1022)

Este skill ha sido desarrollado como una herramienta de apoyo integral para la asignatura de **Simulación** dentro del programa de Ingeniería en Sistemas Computacionales del Tecnológico Nacional de México (TecNM). El contenido está estrictamente alineado con el programa oficial SCD-1022.

---

## Objetivo y Competencia General

El propósito de este skill es asistir en el análisis, modelado, desarrollo y experimentación de sistemas productivos y de servicios. La competencia central a desarrollar es la capacidad de aplicar herramientas matemáticas y computacionales para representar el comportamiento de sistemas complejos y facilitar la toma de decisiones fundamentada en resultados estadísticos.

---

## Estructura de la Asignatura

1. **Introducción a la simulación**: Fundamentos teóricos, metodología formal y etapas de un estudio.
2. **Números pseudoaleatorios**: Métodos de generación y validación mediante pruebas de uniformidad e independencia. Incluye el estudio del método de Monte Carlo.
3. **Generación de variables aleatorias**: Representación estocástica de sistemas mediante distribuciones de probabilidad discretas y continuas.
4. **Lenguajes de simulación**: Implementación de modelos en software especializado y lenguajes de alto nivel, con enfoque en líneas de espera e inventarios.
5. **Proyecto Integrador**: Desarrollo completo de un modelo de simulación aplicado a un caso real.

---

## Recursos del Skill

### Documentación de Referencia (`references/`)
- **`temario-completo.md`**: Documento detallado que contiene la caracterización de la asignatura, intención didáctica, desglose de subtemas y bibliografía oficial.
- **`formulas-metodos.md`**: Compendio detallado de fórmulas para generación aleatoria, pruebas estadísticas y teoría de colas.

### Implementaciones Técnicas (`scripts/`)
- **`generador_pseudoaleatorios.py`**: Algoritmos de generación de números (LCG, Cuadrados Medios, etc.).
- **`pruebas_estadisticas.py`**: Scripts para la validación de hipótesis (Chi-cuadrada, K-S, Corridas, Póker).
- **`generador_variables_aleatorias.py`**: Generación de valores para diversas distribuciones de probabilidad.
- **`simulador_colas.py`**: Herramientas para el modelado de sistemas de líneas de espera M/M/1 y M/M/c.

---

## Metodología de Uso Sugerida

Al utilizar este skill para resolver problemas académicos o de ingeniería, se recomienda seguir este orden lógico:

1. **Identificación del Problema**: Clasificar el requerimiento dentro de una de las unidades del programa.
2. **Consulta Teórica**: Revisar los fundamentos y fórmulas en los archivos de la carpeta `references/`.
3. **Selección de Herramientas**: Identificar el script de la carpeta `scripts/` necesario para la resolución computacional.
4. **Análisis de Resultados**: Validar que los resultados obtenidos (como la utilización de un sistema o los resultados de una prueba) sean coherentes con los criterios de aceptación teóricos.
5. **Documentación**: Presentar la solución siguiendo la estructura de reporte sugerida en el programa oficial.

---

## Notas de Calidad y Estabilidad

- **Validación de Sistemas de Colas**: Es mandatorio verificar la condición de estabilidad (ρ < 1) antes de proceder con el cálculo de métricas en estado estable.
- **Propiedades Aleatorias**: Los números utilizados para simular deben haber pasado satisfactoriamente las pruebas de uniformidad e independencia para garantizar la validez del estudio.
- **Verificación contra el Programa**: Todas las operaciones deben referenciar directamente los objetivos de aprendizaje del documento SCD-1022.

---
**Autor:** Jesús Olvera  
**Versión:** 1.0  
**Fecha de actualización:** Enero 2026
