import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_passage_commande(driver):
    # Accès à l'application
    driver.get("https://qa-test:mdw@@2025@recrutement.arvea-test.ovh/")

    # Connexion
    username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    )
    username.send_keys("TN25000000")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("maisonduweb123")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.waves-effect.waves-light.border-round.gradient-45deg-arvea-color.col.s6.push-s3")
    login_button.click()

    # Menu : Commandes > Nouvelle commande
    menu_commandes = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Commandes']"))
    )
    menu_commandes.click()

    commande_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Nouvelle commande']"))
    )
    commande_menu.click()

    # Ajouter un produit
    produit_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "searchinput_products"))
    )
    produit_dropdown.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchResults_products > div:nth-child(1)")))

    first_product = driver.find_element(By.CSS_SELECTOR, "#searchResults_products > div:nth-child(1)")
    first_product.click()

    qte_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "quantity"))
    )
    qte_input.clear()
    qte_input.send_keys("5") 

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add")))
    add_button.click()

    # Mode de livraison : Siège
    select2_container = WebDriverWait(driver, 70).until(
        EC.element_to_be_clickable((By.ID, "select2-addDeliveryType-container"))
    )
    select2_container.click()

    siege_option = WebDriverWait(driver, 70).until(
        EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Siège')]"))
    )
    siege_option.click()

    # Sélection de l'agence : Agence Tunis
    select2_container = WebDriverWait(driver, 70).until(
        EC.element_to_be_clickable((By.ID, "select2-addDepot-container"))
    )
    select2_container.click()

    agence_tunis_option = WebDriverWait(driver, 70).until(
        EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Agence Tunis')]"))
    )
    agence_tunis_option.click()
    payment_mode_container = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "select2-paymentMode-container"))
)
    payment_mode_container.click()

# Attendre que l'option "En ligne" soit visible et cliquer dessus
    en_ligne_option = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'A la livraison')]"))
    
)
    en_ligne_option.click()
     
    commander_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "saveOrderBtn"))
)

# Cliquer sur le bouton
    commander_button.click()
    # Faire défiler la page jusqu'à un élément spécifique (par exemple, le bouton de validation)
    success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Succès')]"))
)

# Vérifier que le message contient le texte attendu
    assert "Votre Net à payer est" in success_message.text
    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "element-id"))  # Remplacez "element-id" par l'ID réel de l'élément
    )
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", target_element)

    # Vous pouvez maintenant interagir avec l'élément ciblé
    # Par exemple : target_element.click()
