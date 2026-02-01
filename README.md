# 🎯 Simulación - TecNM (SCD-1022)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![SimPy](https://img.shields.io/badge/SimPy-4.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)
![Lines](https://img.shields.io/badge/Lines-20K+-orange.svg)

**Recurso educativo completo para la materia de Simulación del TecNM**

[📚 Contenido](#-contenido) • [🚀 Inicio Rápido](#-inicio-rápido) • [💻 Ejemplos](#-ejemplos-de-código) • [📖 Documentación](#-documentación)

</div>

---

## 📋 Descripción

Este repositorio contiene material educativo **profesional y completo** para la asignatura **Simulación (SCD-1022)** del Tecnológico Nacional de México (TecNM). Incluye:

- ✅ **~20,000 líneas** de contenido teórico en Markdown
- ✅ **35 archivos** de documentación detallada
- ✅ **16 ejemplos** de código Python ejecutables
- ✅ **100% alineado** con el temario oficial TecNM
- ✅ **5 unidades** completas con teoría, código y ejercicios

## 🎓 Competencias del Curso

Al completar este curso, serás capaz de:

1. ✅ **Analizar** sistemas complejos mediante simulación
2. ✅ **Diseñar** modelos de simulación de eventos discretos
3. ✅ **Implementar** simulaciones en Python (SimPy) y Arena
4. ✅ **Validar** modelos usando pruebas estadísticas
5. ✅ **Optimizar** sistemas productivos y de servicios

## 📚 Contenido

### [Unidad 1: Introducción a la Simulación](content/unidad1/README.md)
**7 archivos • 4,940 líneas • 5 ejemplos de código**

- [1.1 Conceptos básicos](content/unidad1/1.1.md)
- [1.2 Áreas de aplicación](content/unidad1/1.2.md)
- [1.3 Sistemas y modelos](content/unidad1/1.3.md)
- [1.4 Fases de un estudio](content/unidad1/1.4.md)
- [1.5 Metodología general](content/unidad1/1.5.md)
- [1.6 Componentes de un simulador DES](content/unidad1/1.6.md)
- [1.7 Decisión de usar simulación](content/unidad1/1.7.md)

**Ejemplos de código:** [Ver carpeta](content/unidad1/codigos/)

---

### [Unidad 2: Números Pseudoaleatorios](content/unidad2/README.md)
**9 archivos • 5,146 líneas • 3 ejemplos de código**

- [2.1 Métodos de generación](content/unidad2/2.1.md)
- [2.2 Pruebas de validación](content/unidad2/2.2.md)
  - [2.2.1 Pruebas de uniformidad](content/unidad2/2.2.1.md)
  - [2.2.2 Pruebas de aleatoriedad](content/unidad2/2.2.2.md)
  - [2.2.3 Pruebas de independencia](content/unidad2/2.2.3.md)
- [2.3 Monte Carlo y generación de VA](content/unidad2/2.3.md)
  - [2.3.1 Características del método](content/unidad2/2.3.1.md)
  - [2.3.2 Aplicaciones](content/unidad2/2.3.2.md)
  - [2.3.3 Solución de problemas](content/unidad2/2.3.3.md)

**Ejemplos de código:** [Ver carpeta](content/unidad2/codigos/)

---

### [Unidad 3: Generación de Variables Aleatorias](content/unidad3/README.md)
**9 archivos • 4,509 líneas • 3 ejemplos de código**

- [3.1 Conceptos básicos](content/unidad3/3.1.md)
- [3.2 Variables discretas](content/unidad3/3.2.md)
- [3.3 Variables continuas](content/unidad3/3.3.md)
- [3.4 Métodos para generar VA](content/unidad3/3.4.md)
  - [3.4.1 Transformada inversa](content/unidad3/3.4.1.md)
  - [3.4.2 Convolución](content/unidad3/3.4.2.md)
  - [3.4.3 Composición](content/unidad3/3.4.3.md)
- [3.5 Procedimientos especiales](content/unidad3/3.5.md)
- [3.6 Pruebas estadísticas](content/unidad3/3.6.md)

**Ejemplos de código:** [Ver carpeta](content/unidad3/codigos/)

---

### [Unidad 4: Lenguajes de Simulación](content/unidad4/README.md)
**8 archivos • 3,836 líneas • 2 ejemplos de código**

- [4.1 Lenguajes y simuladores](content/unidad4/4.1.md)
- [4.2 Aprendizaje y uso](content/unidad4/4.2.md)
- [4.3 Aplicación a casos](content/unidad4/4.3.md)
  - [4.3.1 Líneas de espera](content/unidad4/4.3.1.md)
  - [4.3.2 Inventarios](content/unidad4/4.3.2.md)
- [4.4 Análisis de resultados](content/unidad4/4.4.md)
  - [4.4.1 Pruebas paramétricas](content/unidad4/4.4.1.md)
  - [4.4.2 Pruebas no paramétricas](content/unidad4/4.4.2.md)

**Ejemplos de código:** [Ver carpeta](content/unidad4/codigos/)

---

### [Unidad 5: Proyecto Integrador](content/unidad5/README.md)
**1 archivo • ~700 líneas • 1 template completo**

- [5.1 Análisis y modelado de sistemas](content/unidad5/5.1.md)

**Template de proyecto:** [Ver carpeta](content/unidad5/codigos/)

---

## 🚀 Inicio Rápido

### Prerrequisitos

```bash
# Python 3.8 o superior
python --version

# Instalar dependencias
pip install simpy numpy scipy pandas matplotlib
```

### Ejecutar Ejemplos

```bash
# Navegar a una unidad
cd content/unidad1/codigos/

# Ejecutar ejemplo
python 01_simulacion_basica_mm1.py
```

### Estructura del Proyecto

```
simulacion-tecnm/
├── README.md                    # Este archivo
├── content/                     # Contenido del curso
│   ├── unidad1/                # Introducción
│   │   ├── README.md
│   │   ├── 1.1.md - 1.7.md
│   │   └── codigos/            # Ejemplos Python
│   ├── unidad2/                # Números Pseudoaleatorios
│   ├── unidad3/                # Variables Aleatorias
│   ├── unidad4/                # Lenguajes de Simulación
│   └── unidad5/                # Proyecto Integrador
└── Simulacion.pdf              # Temario oficial TecNM
```

## 💻 Ejemplos de Código

### Unidad 1: Simulación Básica M/M/1

```python
# Ejemplo simple de cola M/M/1
from simulacion_basica import SimulacionCola

sim = SimulacionCola(
    tasa_llegada=3,      # 3 clientes/hora
    tasa_servicio=4,     # 4 clientes/hora
    tiempo_simulacion=1000
)

sim.simular()
sim.mostrar_resultados()
```

### Unidad 2: Generador LCG

```python
# Generador de números pseudoaleatorios
from generador_lcg import GeneradorLCG

gen = GeneradorLCG(semilla=42)
numeros = gen.generar_n(1000)
```

### Unidad 4: SimPy Básico

```python
# Simulación con SimPy
import simpy

def cliente(env, servidor):
    with servidor.request() as req:
        yield req
        yield env.timeout(5)

env = simpy.Environment()
servidor = simpy.Resource(env, capacity=1)
env.process(cliente(env, servidor))
env.run()
```

## 📖 Documentación

### Guías por Unidad

Cada unidad incluye:
- **README.md**: Índice y objetivos
- **Archivos .md**: Teoría detallada con ejemplos
- **Carpeta codigos/**: Ejemplos ejecutables
- **Ejercicios**: Problemas propuestos con soluciones

### Recursos Adicionales

- **Teoría de Colas**: Unidades 1 y 4
- **Método Monte Carlo**: Unidades 2 y 3
- **SimPy Tutorial**: Unidad 4
- **Proyecto Completo**: Unidad 5

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **SimPy**: Simulación de eventos discretos
- **NumPy**: Operaciones numéricas
- **SciPy**: Estadística y distribuciones
- **Pandas**: Análisis de datos
- **Matplotlib**: Visualización

## 📊 Estadísticas del Proyecto

- **Archivos Markdown**: 35
- **Líneas de teoría**: ~20,000
- **Ejemplos de código**: 16
- **Líneas de código**: ~3,000
- **Unidades completas**: 5/5
- **Cobertura del temario**: 100%

## 🎯 Casos de Estudio Incluidos

1. **Hospital** - Sala de emergencias (M/M/c)
2. **Banco** - Optimización de cajeros
3. **Supermercado** - Gestión de inventario
4. **Call Center** - Dimensionamiento de agentes
5. **Manufactura** - Línea de producción

## 📝 Cómo Usar Este Recurso

### Para Estudiantes

1. **Estudiar teoría**: Leer archivos .md en orden
2. **Ejecutar código**: Probar ejemplos en `/codigos/`
3. **Hacer ejercicios**: Resolver problemas propuestos
4. **Proyecto final**: Usar template de Unidad 5

### Para Profesores

1. **Material de clase**: Usar archivos .md como slides
2. **Laboratorios**: Ejemplos de código listos
3. **Tareas**: Ejercicios en cada unidad
4. **Evaluación**: Rúbrica en Unidad 5

## 🤝 Contribuciones

Este es un recurso educativo abierto. Sugerencias y mejoras son bienvenidas.

## 📄 Licencia

MIT License - Libre para uso educativo

## ✨ Autor

**Jesús Olvera**  
Estudiante de Ingeniería en Sistemas Computacionales  
Instituto Tecnológico de Ciudad Madero (ITCM)

---

<div align="center">

**⭐ Si este recurso te fue útil, considera darle una estrella ⭐**

[📚 Ver Contenido](#-contenido) • [🚀 Comenzar](#-inicio-rápido) • [💻 Ejemplos](#-ejemplos-de-código)

<br>

**[⬅️ Volver al Menú de Materias (Skills ISC)](../README.md)**


</div>
