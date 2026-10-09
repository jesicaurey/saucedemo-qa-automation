from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_inventory(logged_in_driver):
    # Verificar el título de la página después del login
    assert logged_in_driver.title == "Swag Labs", "El título de la página no coincide"

    # Validar presencia de productos en la página de inventario
    productos = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert productos, "No se encontraron productos en el inventario"

    primer_producto = productos[0]

    # Verificar que el primer producto esté visible
    assert primer_producto.is_displayed(), "El primer producto no está visible"

    # Verificar el nombre y el precio del primer producto
    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio_producto = primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    assert nombre_producto == "Sauce Labs Backpack", "El nombre del producto no coincide"
    assert precio_producto == "$29.99", "El precio del producto no coincide"

    # Verificar que el menú de navegación esté visible
    menu = logged_in_driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú de navegación no está visible"

    # Verificar que el filtro de productos esté visible
    filtro = logged_in_driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro de productos no está visible"

    # Verificar que el carrito de compras esté visible
    carrito = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito.is_displayed(), "El carrito de compras no está visible"


def test_agregar_producto_al_carrito(logged_in_driver):
    # Verificar que el carrito esté vacío inicialmente
    assert not logged_in_driver.find_elements(
        By.CLASS_NAME, "shopping_cart_badge"
    ), "El carrito debería estar vacío al inicio"

    # Agregar el primer producto al carrito
    logged_in_driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    # Verificar que el contador del carrito se incremente
    contador = WebDriverWait(logged_in_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert contador.text == "1", "El contador no indica un producto"


    # Navegar al carrito de compras
    logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verificar que el producto agregado aparezca en el carrito
    producto_carrito = WebDriverWait(logged_in_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    nombre_producto = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    assert nombre_producto == "Sauce Labs Backpack", "El producto no aparece en el carrito"
        