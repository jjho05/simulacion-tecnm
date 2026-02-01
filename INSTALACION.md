# Guía de Instalación

## Requisitos del Sistema

- **Python**: 3.8 o superior
- **Sistema Operativo**: Windows, macOS, o Linux
- **Espacio en disco**: ~100 MB

## Instalación Paso a Paso

### 1. Verificar Python

```bash
python --version
# o
python3 --version
```

Si no tienes Python instalado, descárgalo de [python.org](https://www.python.org/downloads/)

### 2. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/simulacion-tecnm.git
cd simulacion-tecnm
```

### 3. Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

Si no existe `requirements.txt`, instalar manualmente:

```bash
pip install simpy numpy scipy pandas matplotlib
```

### 5. Verificar Instalación

```bash
# Ejecutar ejemplo de prueba
cd content/unidad1/codigos/
python 01_simulacion_basica_mm1.py
```

Si ves resultados de la simulación, ¡todo está listo! ✅

## Dependencias Detalladas

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| simpy | ≥4.0 | Simulación de eventos discretos |
| numpy | ≥1.20 | Operaciones numéricas |
| scipy | ≥1.7 | Estadística y distribuciones |
| pandas | ≥1.3 | Análisis de datos |
| matplotlib | ≥3.4 | Visualización |

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'simpy'"

**Solución:**
```bash
pip install simpy
```

### Error: "Python no reconocido como comando"

**Solución:**
- Asegúrate de que Python esté en el PATH del sistema
- Intenta usar `python3` en lugar de `python`

### Error al importar matplotlib

**Solución:**
```bash
pip install --upgrade matplotlib
```

## Configuración para Desarrollo

Si planeas contribuir o modificar el código:

```bash
# Instalar herramientas de desarrollo
pip install pytest black flake8

# Ejecutar tests (si existen)
pytest

# Formatear código
black content/
```

## Uso con Jupyter Notebook

Para usar los ejemplos en Jupyter:

```bash
pip install jupyter
jupyter notebook
```

Luego navega a la carpeta de códigos y crea un nuevo notebook.

## Recursos Adicionales

- [Documentación de SimPy](https://simpy.readthedocs.io/)
- [Guía de NumPy](https://numpy.org/doc/)
- [Tutorial de Python](https://docs.python.org/3/tutorial/)

---

¿Problemas? Abre un issue en GitHub o contacta al autor.
