import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_exitoso(driver):
    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales válidas
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar a que cargue la página de inventario
    titulo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]'))
    )

    # Verificar que se haya iniciado sesión correctamente
    assert "inventory.html" in driver.current_url, "No se abrió el inventario"
    assert titulo.text == "Products", "No se mostró el título del inventario"

    # Verificar que aparezca el logo de la aplicación
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs", "No se mostró el logo esperado"


@pytest.mark.parametrize(
    "usuario, password",
    [
        ("standard_user", "password_incorrecta"),
        ("usuario_incorrecto", "secret_sauce"),
    ],
)
def test_login_fallido(driver, usuario, password):
    # Abrir la página de inicio de sesión
    driver.get("https://www.saucedemo.com/")

    # Ingresar credenciales inválidas
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Verificar que se muestre el mensaje de error
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
    )
    assert "Username and password do not match" in error.text, (
        "No se mostró el mensaje esperado para credenciales inválidas"
    )
