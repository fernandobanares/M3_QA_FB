
---

## 🚀 Funcionalidades principales

- ✔️ CRUD completo del modelo `Registro`
- ✔️ Validaciones de entrada (`CharField`, `EmailField`, `BooleanField`)
- ✔️ Ciclo completo **Red-Green-Refactor**
- ✔️ Pruebas unitarias con `TestCase` (Django)
- ✔️ Mocking de métodos usando `unittest.mock`
- ✔️ Script `.sql` con operaciones para base SQLite externa
- ✔️ Reportes de cobertura de código con `coverage.py` (≥ 90%)

---

## 📌 Objetivos por lección cumplidos

### ✅ Lección 1 – Fundamentos de TDD
- Se aplicó el ciclo **Red-Green-Refactor**
- Se documentó una prueba inicial que fallaba (fase RED)

### ✅ Lección 2 – CRUD con TDD
- Se implementaron las 4 operaciones CRUD con validaciones
- Se realizaron más de 12 ciclos TDD y 8+ pruebas

### ✅ Lección 3 – Integración con SQL
- Se creó un `script.sql` con tabla `usuarios` y 5 registros
- Se ejecutaron operaciones CRUD usando `sqlite3` en `sqlite_demo.py`
- Se validó la persistencia en `usuarios.db`

### ✅ Lección 4 – Pruebas Unitarias y Mocking
- Se escribieron 12+ pruebas unitarias
- Se utilizaron mocks para `__str__`, `save()` y `objects.get()`

### ✅ Lección 5 – Cobertura de Código
- Se utilizó `coverage.py` y se generó reporte HTML
- La cobertura alcanzada supera el **90%**
- Se revisaron líneas no cubiertas y se agregaron tests adicionales

---

## 🧪 Ejecución de pruebas y cobertura

```bash
# Ejecutar pruebas con Django
python manage.py test registros

# Ejecutar con coverage
coverage run manage.py test registros

# Ver reporte en consola
coverage report -m

# Generar reporte HTML
coverage html



