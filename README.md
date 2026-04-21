# 🔄 testpruebasregresivas — Pruebas de Regresión con Flask y Pytest

API REST construida con **Flask** para calcular precios finales con cupón de descuento e impuesto. El proyecto implementa una suite completa de **pruebas de regresión** con Pytest para verificar que cada cambio no rompa el comportamiento esperado.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Flask](https://img.shields.io/badge/Flask-3.1-lightgrey?logo=flask) ![Pytest](https://img.shields.io/badge/Pytest-8.4-green?logo=pytest)

---

## 📋 Descripción

El sistema expone un endpoint `/precio` que recibe un precio base, un código de cupón (ej: `OFERTA10`, `SUPER20`) y una tasa de impuesto opcional. Devuelve el precio final calculado con descuento e impuesto aplicados.

### Ejemplos de cálculo

| Precio | Cupón | Impuesto | Precio final |
|---|---|---|---|
| $100 | OFERTA10 (10%) | 19% (default) | $107.10 |
| $200 | SUPER20 (20%) | 10% | $176.00 |
| $50 | INVALIDO | 19% | $59.50 |

---

## 🏗️ Estructura del proyecto

```
testpruebasregresivas/
├── app/
│   ├── __init__.py
│   ├── api.py          # Rutas Flask (endpoint /precio)
│   └── cupones.py      # Lógica de cálculo y tabla de cupónes
├── tests/
│   ├── test_api.py     # Tests de integración del endpoint REST
│   └── test_cupones.py # Tests unitarios de lógica de cupónes
├── pytest.ini
└── requirements.txt
```

---

## 🛠️ Tecnologías

| Herramienta | Versión | Rol |
|---|---|---|
| Python | 3.x | Lenguaje principal |
| Flask | 3.1.1 | Framework web / API REST |
| Pytest | 8.4.0 | Framework de testing |
| Werkzeug | 3.1.3 | Cliente de test Flask |

---

## 🚀 Cómo ejecutar

### Prerrequisitos
- Python 3.8+
- pip

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Carl0gonzalez/testpruebasregresivas.git
cd testpruebasregresivas

# 2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Ejecutar los tests de regresión
pytest

# 4. Ejecutar con reporte detallado
pytest -v
```

### Ejecutar la API localmente

```bash
flask --app app.api run
# API disponible en http://localhost:5000
```

### Ejemplo de uso

```bash
curl -X POST http://localhost:5000/precio \
  -H "Content-Type: application/json" \
  -d '{"precio": 100, "cupon": "OFERTA10"}'
# Respuesta: {"precio_final": 107.1}
```

---

## 💡 Aprendizajes clave

- Diseño de suites de regresión para detectar cambios no intencionados
- Uso del cliente de pruebas de Flask (`app.test_client()`) para tests de integración
- Separación de responsabilidades: lógica de negocio vs. capa HTTP
- Fixtures de Pytest para reutilización de configuración de tests

---

## 👤 Autor

**Carlo González** — [GitHub](https://github.com/Carl0gonzalez)
