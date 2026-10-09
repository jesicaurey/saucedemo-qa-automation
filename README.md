# SauceDemo QA Automation

Proyecto de automatización de pruebas web desarrollado con Python, Selenium WebDriver y pytest.

Las pruebas verifican el inicio de sesión, la página de inventario y el flujo básico del carrito de compras en [SauceDemo](https://www.saucedemo.com/).

## Tecnologías

- Python
- Selenium WebDriver
- pytest
- pytest-html para generar el reporte HTML
- Google Chrome como navegador de prueba

## Requisitos previos

- Python instalado y disponible mediante el comando `py`.
- Google Chrome instalado.
- Acceso a internet.

Selenium Manager administra el controlador de Chrome automáticamente en versiones actuales de Selenium.

## Instalación de dependencias

Desde la carpeta del proyecto, instala las dependencias declaradas en `requirements.txt`:

```powershell
py -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecuta todas las pruebas:

```powershell
py -m pytest
```

La configuración de `pytest.ini` activa el modo detallado y genera automáticamente un reporte HTML en `reports/report.html`.

Para ejecutar solo un archivo:

```powershell
py -m pytest test_login.py
py -m pytest test_inventory.py
```

## Pruebas incluidas

- Inicio de sesión exitoso y verificación de la página de inventario.
- Inicio de sesión fallido con distintas credenciales inválidas.
- Presencia y visibilidad de productos y elementos importantes del inventario.
- Agregado de Sauce Labs Backpack al carrito y verificación del contador y el producto.

## Estructura del proyecto

```text
saucedemo-qa-automation/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── test_inventory.py
├── test_login.py
└── reports/
    └── report.html
```
