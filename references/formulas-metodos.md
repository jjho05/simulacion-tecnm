# Fórmulas y Métodos Clave - Simulación

## 1. Generación de Números Pseudoaleatorios

### Método Congruencial Lineal
```
X(n+1) = (a * X(n) + c) mod m

Donde:
- X(n): número pseudoaleatorio en la iteración n
- a: multiplicador
- c: incremento
- m: módulo
- X(0): semilla (seed)

Número aleatorio en [0,1]: r(n) = X(n) / m
```

**Condiciones para periodo máximo (m):**
1. c y m son primos relativos
2. a - 1 es divisible por todos los factores primos de m
3. Si m es múltiplo de 4, entonces a - 1 también lo es

### Método Congruencial Multiplicativo
```
X(n+1) = (a * X(n)) mod m

Condiciones para periodo máximo:
- m debe ser primo
- a debe ser una raíz primitiva de m
```

---

## 2. Pruebas Estadísticas

### Prueba Chi-cuadrada (χ²) - Uniformidad

**Hipótesis:**
- H₀: Los números son uniformemente distribuidos
- H₁: Los números NO son uniformemente distribuidos

**Estadístico:**
```
χ² = Σ [(O(i) - E(i))² / E(i)]

Donde:
- O(i): frecuencia observada en la clase i
- E(i): frecuencia esperada en la clase i = n/k
- n: número total de datos
- k: número de clases
```

**Criterio de decisión:**
```
Si χ²(calculado) < χ²(α, k-1) → Aceptar H₀
Si χ²(calculado) ≥ χ²(α, k-1) → Rechazar H₀

Donde:
- α: nivel de significancia (típicamente 0.05)
- k-1: grados de libertad
```

### Prueba de Kolmogorov-Smirnov (K-S)

**Estadístico:**
```
D = max|F(x) - S(x)|

Donde:
- F(x): función de distribución teórica acumulada
- S(x): función de distribución empírica acumulada
- D: máxima diferencia absoluta
```

**Criterio de decisión:**
```
Si D < D(α,n) → Aceptar H₀
Si D ≥ D(α,n) → Rechazar H₀

Donde:
- D(α,n): valor crítico de la tabla K-S
- n: tamaño de la muestra
```

### Prueba de Corridas Arriba y Abajo

**Estadístico:**
```
μ(r) = (2n - 1) / 3
σ(r) = √[(16n - 29) / 90]

Z = (r - μ(r)) / σ(r)

Donde:
- r: número de corridas observadas
- n: número de datos
```

**Criterio de decisión:**
```
Si |Z| < Z(α/2) → Aceptar H₀ (son independientes)
Si |Z| ≥ Z(α/2) → Rechazar H₀

Para α = 0.05: Z(0.025) = 1.96
```

---

## 3. Generación de Variables Aleatorias

### Método de la Transformada Inversa

**Teorema:** Si U ~ Uniforme(0,1) y F(x) es una función de distribución, entonces:
```
X = F⁻¹(U)
```
tiene distribución F(x).

**Algoritmo:**
1. Generar U ~ Uniforme(0,1)
2. Calcular X = F⁻¹(U)
3. Retornar X

### Distribuciones Discretas

#### Distribución Uniforme Discreta
```
P(X = x(i)) = 1/n

Generación:
X = x(i) donde i = ⌈n * U⌉
```

#### Distribución de Bernoulli
```
P(X = 1) = p
P(X = 0) = 1 - p

Generación:
Si U ≤ p entonces X = 1
Si U > p entonces X = 0
```

#### Distribución Binomial
```
P(X = k) = C(n,k) * p^k * (1-p)^(n-k)

Generación (método directo):
X = Σ(i=1 hasta n) de Bernoulli(p)
```

#### Distribución de Poisson
```
P(X = k) = (λ^k * e^(-λ)) / k!

Generación (método de la transformada inversa):
1. a = e^(-λ), b = 1, i = 0
2. Generar U ~ Uniforme(0,1)
3. b = b * U
4. Si b < a, retornar X = i
5. i = i + 1, ir al paso 2
```

### Distribuciones Continuas

#### Distribución Uniforme Continua
```
f(x) = 1/(b-a) para a ≤ x ≤ b

Generación:
X = a + (b - a) * U
```

#### Distribución Exponencial
```
f(x) = λ * e^(-λx) para x ≥ 0

Generación:
X = -ln(1 - U) / λ
o simplemente:
X = -ln(U) / λ
```

#### Distribución Normal (Método Box-Muller)
```
Si U₁, U₂ ~ Uniforme(0,1), entonces:

Z₁ = √(-2 ln U₁) * cos(2π U₂)
Z₂ = √(-2 ln U₁) * sin(2π U₂)

Donde Z₁, Z₂ ~ Normal(0,1)

Para Normal(μ, σ²):
X = μ + σ * Z
```

#### Distribución Triangular
```
f(x) tiene forma triangular con parámetros a, b, c
donde a ≤ c ≤ b

Generación:
Si U ≤ (c-a)/(b-a):
    X = a + √[U(b-a)(c-a)]
Si U > (c-a)/(b-a):
    X = b - √[(1-U)(b-a)(b-c)]
```

#### Distribución Weibull
```
f(x) = (β/α) * (x/α)^(β-1) * e^(-(x/α)^β)

Generación:
X = α * (-ln(U))^(1/β)
```

---

## 4. Teoría de Colas

### Notación de Kendall
```
A/B/c/K/m/Z

Donde:
A: distribución de llegadas
B: distribución de servicio
c: número de servidores
K: capacidad del sistema
m: tamaño de la población
Z: disciplina de la cola
```

**Códigos comunes:**
- M: Markoviano (exponencial/Poisson)
- D: Determinístico
- G: General
- FIFO: First In First Out
- LIFO: Last In First Out

### Sistema M/M/1

**Parámetros:**
```
λ: tasa de llegadas (clientes/tiempo)
μ: tasa de servicio (clientes/tiempo)
ρ = λ/μ: factor de utilización (debe ser < 1)
```

**Fórmulas:**
```
L = ρ / (1 - ρ)                    # Número promedio en el sistema
Lq = ρ² / (1 - ρ)                  # Número promedio en la cola
W = 1 / (μ - λ)                    # Tiempo promedio en el sistema
Wq = ρ / (μ - λ)                   # Tiempo promedio en la cola
P₀ = 1 - ρ                         # Probabilidad de sistema vacío
Pn = ρⁿ * (1 - ρ)                  # Probabilidad de n clientes
```

### Sistema M/M/c

**Parámetros:**
```
c: número de servidores
ρ = λ/(c*μ): utilización por servidor
```

**Fórmulas:**
```
P₀ = 1 / [Σ(n=0 hasta c-1) (λ/μ)ⁿ/n! + (λ/μ)^c/(c!(1-ρ))]

Lq = P₀ * (λ/μ)^c * ρ / (c! * (1-ρ)²)

L = Lq + λ/μ

Wq = Lq / λ

W = Wq + 1/μ
```

### Sistema M/M/1/K (Capacidad Limitada)

**Fórmulas:**
```
P₀ = (1 - ρ) / (1 - ρ^(K+1))       si ρ ≠ 1
P₀ = 1 / (K + 1)                    si ρ = 1

Pn = P₀ * ρⁿ                        para n ≤ K

P(bloqueo) = PK                     # Probabilidad de rechazo

λ(efectiva) = λ * (1 - PK)          # Tasa efectiva de llegadas

L = Σ(n=0 hasta K) n * Pn
```

---

## 5. Sistemas de Inventario

### Modelo (Q, r) - Revisión Continua

**Parámetros:**
```
Q: cantidad de orden
r: punto de reorden
D: demanda promedio por periodo
L: tiempo de entrega (lead time)
σ(L): desviación estándar de la demanda durante L
```

**Fórmulas:**
```
Q* = √(2 * D * K / h)              # Cantidad económica de orden (EOQ)

Donde:
K: costo de ordenar
h: costo de mantener por unidad por periodo

r = D * L + z * σ(L)               # Punto de reorden con stock de seguridad
z: valor z de la distribución normal para nivel de servicio deseado
```

### Modelo (T, S) - Revisión Periódica

**Parámetros:**
```
T: periodo de revisión
S: nivel objetivo de inventario
```

**Fórmulas:**
```
S = D * (T + L) + z * σ(T+L)

Cantidad a ordenar = S - I(t)
Donde I(t) es el inventario en el momento de revisión
```

---

## 6. Análisis de Resultados

### Intervalo de Confianza para la Media

```
IC = x̄ ± t(α/2, n-1) * (s / √n)

Donde:
x̄: media muestral
s: desviación estándar muestral
n: tamaño de muestra
t(α/2, n-1): valor t de Student
α: nivel de significancia (típicamente 0.05)
```

### Determinación del Número de Réplicas

```
n = (t(α/2) * s / E)²

Donde:
E: error máximo aceptable
s: desviación estándar estimada (de réplicas piloto)
```

### Tiempo de Calentamiento (Warm-up)

**Métodos:**
1. Método gráfico: observar cuando se estabiliza
2. Método de Welch: promedios móviles
3. Regla empírica: 10-20% del tiempo total de simulación

---

## 7. Validación Estadística

### Prueba t para Comparar Dos Medias

```
t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)

Grados de libertad (aproximación):
df ≈ (s₁²/n₁ + s₂²/n₂)² / [(s₁²/n₁)²/(n₁-1) + (s₂²/n₂)²/(n₂-1)]

Si |t| < t(α/2, df) → No hay diferencia significativa
```

### ANOVA (Análisis de Varianza)

```
F = MS(entre) / MS(dentro)

Donde:
MS(entre): media cuadrática entre grupos
MS(dentro): media cuadrática dentro de grupos

Si F < F(α, k-1, N-k) → No hay diferencia significativa entre grupos
```

---

## 8. Método de Monte Carlo

### Estimación de Integrales

```
Para estimar I = ∫(a hasta b) g(x) dx:

1. Generar n valores U₁, U₂, ..., Un ~ Uniforme(0,1)
2. Calcular X(i) = a + (b-a) * U(i)
3. Evaluar g(X(i)) para cada i
4. Estimar: Î = (b-a) * (1/n) * Σ g(X(i))
```

### Estimación de π

```
1. Generar puntos (x,y) uniformemente en [0,1] × [0,1]
2. Contar cuántos caen dentro del círculo: x² + y² ≤ 1
3. π ≈ 4 * (puntos dentro / total de puntos)
```

---

## Notas Importantes

- Todas las fórmulas asumen condiciones de estado estable
- Los sistemas de colas requieren ρ < 1 para estabilidad
- Siempre verificar supuestos antes de aplicar fórmulas
- Realizar pruebas de bondad de ajuste para validar distribuciones
- Usar múltiples réplicas para obtener intervalos de confianza confiables
