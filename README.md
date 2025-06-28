# Proyecto TDD con Django - Módulo de Funcionalidades Básicas

## Descripción
Este proyecto es una práctica integral para desarrollar y fortalecer habilidades en **Test Driven Development (TDD)** usando Django y Python. Incluye la implementación de funcionalidades básicas (CRUD), pruebas unitarias, mocking, medición de cobertura y aplicación de buenas prácticas.

## Objetivos
- Aplicar el ciclo **Red-Green-Refactor** en el desarrollo.
- Implementar un mínimo de 8 pruebas unitarias automatizadas.
- Usar mocking para simular comportamientos externos.
- Mantener una cobertura de código superior al 80%.
- Seguir principios SOLID, DRY y patrones de diseño limpios.
- Utilizar SQLite como base de datos local para desarrollo.
- Documentar el proceso y resultados en un informe.
- Simular integración con base de datos SQL externa mediante script.

## Funcionalidades
- Crear registro
- Actualizar registro
- Eliminar registro
- Listar registros

## Tecnologías y Herramientas
- Python 3.x
- Django
- unittest y unittest.mock (para pruebas y mocking)
- coverage (para medición de cobertura)
- SQLite (base de datos local)
- Git y GitHub (control de versiones y repositorio remoto)
- SQLonline (simulado con `script.sql`)

## Pasos realizados

1. Configuración inicial del proyecto con SQLite por defecto.
2. Implementación de pruebas unitarias con más de 8 casos cubiertos.
3. Refactorización de pruebas usando `subTest` para evitar duplicación.
4. Aplicación de mocking para simular métodos en los tests.
5. Ejecución y revisión de cobertura de código con coverage.
6. Simulación de integración SQL: creación de un archivo `script.sql` con una tabla y 5 registros de ejemplo, ejecutado con `sqlite3` para validar la persistencia.
7. Limpieza y orden del código para mantener buenas prácticas.
8. Creación de este README para documentar el proceso.

## Resultados de la cobertura

| Archivo                      | Líneas | Fallos | Omitidas | Cobertura |
|-----------------------------|--------|--------|----------|-----------|
| manage.py                   | 11     | 2      | 0        | 82%       |
| registros/__init__.py       | 0      | 0      | 0        | 100%      |
| registros/admin.py          | 1      | 0      | 0        | 100%      |
| registros/apps.py           | 4      | 0      | 0        | 100%      |
| registros/migrations/__init__.py | 0 | 0      | 0        | 100%      |
| registros/migrations/0001_initial.py | 5 | 0    | 0        | 100%      |
| registros/models.py         | 7      | 0      | 0        | 100%      |
| registros/tests.py          | 34     | 0      | 0        | 100%      |
| tdd_project/__init__.py     | 0      | 0      | 0        | 100%      |
| tdd_project/settings.py     | 18     | 0      | 0        | 100%      |
| tdd_project/urls.py         | 3      | 0      | 0        | 100%      |

**Cobertura total:** 83 líneas cubiertas de 85, lo que representa un **98% de cobertura**.

---

## Retos y aprendizajes

- Aprendí a aplicar el ciclo TDD de manera disciplinada.
- Practiqué el uso de mocking con `unittest.mock` para simular métodos.
- Mejoré la estructura de los tests para evitar código repetido.
- Comprendí la importancia de la cobertura y cómo medirla.
- Simulé la persistencia en una base SQL usando SQLite + `script.sql`.
- Documenté y versioné el proyecto usando Git y GitHub.

## Cómo ejecutar el proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/fernandobanares/M3_QA_FB
   cd tdd_project


