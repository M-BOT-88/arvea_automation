from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommandePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_commande(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Commandes']"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Nouvelle commande']"))
        ).click()

    def ajouter_produit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "searchinput_products"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#searchResults_products > div:nth-child(1)"))
        ).click()
        qte_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "quantity"))
        )
        qte_input.clear()
        qte_input.send_keys("5")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add"))
        ).click()

    def selectionner_livraison(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-addDeliveryType-container"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Siège')]"))
        ).click()

    def selectionner_agence(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-addDepot-container"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Agence Tunis')]"))
        ).click()

    def selectionner_paiement(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "select2-paymentMode-container"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'A la livraison')]"))
        ).click()

    def commander(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "saveOrderBtn"))
        ).click()

    def verifier_succes(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Succès')]"))
        )
        assert "Votre Net à payer est" in success_message.text
