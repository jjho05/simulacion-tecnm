# Unidad 5: Proyecto Integrador - Ejemplos de Código

Este directorio contiene el template completo de un proyecto de simulación siguiendo la metodología de 7 fases.

## Archivo Principal

### `proyecto_completo_template.py`

Template completo de proyecto que incluye:

**Fase 1: Definición del Problema**
- Sistema: Línea de producción de laptops
- Objetivos claros
- Alcance definido

**Fase 2: Datos**
- Estructura de datos recolectados
- Parámetros del sistema

**Fase 3: Modelo**
- Clase `LineaProduccion` completa
- 5 estaciones + 2 inspecciones
- Configuración de escenarios

**Fase 4: Verificación**
- Función `verificar_modelo()`
- Pruebas de lógica

**Fase 5: Validación**
- Función `validar_modelo()`
- Comparación con datos reales
- Prueba t estadística

**Fase 6: Experimentación**
- Función `experimentar_escenarios()`
- Múltiples configuraciones
- Análisis económico

**Fase 7: Visualización**
- Función `generar_visualizaciones()`
- Gráficos de producción
- Análisis de beneficios

## Cómo Usar

```bash
# Instalar dependencias
pip install simpy numpy pandas matplotlib scipy

# Ejecutar proyecto completo
python proyecto_completo_template.py
```

## Salida Esperada

El script genera:
- Reporte de verificación
- Reporte de validación
- Tabla de resultados de experimentación
- Gráfico `resultados_proyecto.png`

## Adaptación para Tu Proyecto

1. **Modificar datos** en `DATOS_REALES`
2. **Ajustar modelo** en clase `LineaProduccion`
3. **Definir escenarios** en `experimentar_escenarios()`
4. **Personalizar visualizaciones** según necesidades

## Rúbrica de Evaluación

Este template cubre todos los criterios:
- ✅ Definición del problema (10 pts)
- ✅ Recolección de datos (15 pts)
- ✅ Modelo conceptual (10 pts)
- ✅ Implementación (20 pts)
- ✅ Verificación (10 pts)
- ✅ Validación (15 pts)
- ✅ Experimentación (10 pts)
- ✅ Documentación (10 pts)

---

**Nota:** Este es un template educativo. Los datos son simulados. Para un proyecto real, debes recolectar datos del sistema que estés estudiando.
