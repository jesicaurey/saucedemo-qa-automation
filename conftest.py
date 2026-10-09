import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    # Abrir el navegador para la prueba
    navegador = webdriver.Chrome()
    yield navegador

    # Cerrar el navegador al terminar la prueba
    navegador.quit()


@pytest.fixture
def logged_in_driver(driver):
    # Realizar login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Esperar a que cargue la página de inventario
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    return driver
