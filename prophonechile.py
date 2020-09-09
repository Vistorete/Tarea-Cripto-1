from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__)) # obtiene la direccion absuluta
CHROMEDRIVE_PATH = os.path.join(ABSOLUTE_PATH, "chromedriver.exe") # Le da direccion al ejecutable
SESSION_PATH = os.path.join(ABSOLUTE_PATH, "session\\")
CHROME_BROWSER = None

import itertools
def split(word): 
    return [char for char in word]


def init_web():
    global CHROME_BROWSER
    CHROME_BROWSER = webdriver.Chrome(CHROMEDRIVE_PATH) # ejecuta chromedriver.exe
    CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/")
    
def crear_cuenta(email = "tarea_cripto_usr15@yopmail.com",contraseña = r'miramenteexplico574'):
    global CHROME_BROWSER
    CHROME_BROWSER.find_element_by_id("reg_email").send_keys(email)
    CHROME_BROWSER.find_element_by_id("reg_password").send_keys(contraseña)
    CHROME_BROWSER.find_element_by_name("register").click()
    
def entrar_cuenta(email = "tarea_cripto_usr15@yopmail.com",contraseña = r'miramenteexplico574'):
    global CHROME_BROWSER
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='username']")))
    CHROME_BROWSER.find_element_by_id("username").clear()
    CHROME_BROWSER.find_element_by_id("username").send_keys(email)
    CHROME_BROWSER.find_element_by_id("password").send_keys(contraseña)
    CHROME_BROWSER.find_element_by_name("login").click()  

def cambiar_contraseña(email = "tarea_cripto_usr15@yopmail.com",contraseña = 'miramenteexplico574', nueva_contraseña = "nuevacontraseñamaster789"):
    entrar_cuenta(email,contraseña)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='entry-content']")))
    CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/edit-account/")
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password_current']")))
    CHROME_BROWSER.find_element_by_id("account_first_name").clear()
    CHROME_BROWSER.find_element_by_id("account_first_name").send_keys("Minombre")
    CHROME_BROWSER.find_element_by_id("account_last_name").clear()
    CHROME_BROWSER.find_element_by_id("account_last_name").send_keys("Miapellido")
    CHROME_BROWSER.find_element_by_id("account_display_name").clear()
    CHROME_BROWSER.find_element_by_id("account_display_name").send_keys("tarea_cripto_usr15")
    CHROME_BROWSER.find_element_by_id("password_current").send_keys(contraseña)
    CHROME_BROWSER.find_element_by_id("password_1").send_keys(nueva_contraseña)
    CHROME_BROWSER.find_element_by_id("password_2").send_keys(nueva_contraseña)
    CHROME_BROWSER.find_element_by_name("save_account_details").click()


def fuerza_bruta(charset = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789", repeticiones = 100, mincaracteres = 12):
    stuff = split(charset)
    counter = 0
    for L in range(mincaracteres + 1, len(stuff)+1):
        for subset in itertools.combinations_with_replacement(stuff, L):
            if counter >= repeticiones:
                break
            entrar_cuenta(contraseña = ''.join(subset))
            print( str(counter) +":",''.join(subset))
            counter += 1

def recuperar_contraseña(email = "tarea_cripto_usr15@yopmail.com" ):
    global CHROME_BROWSER
    CHROME_BROWSER.get("https://prophonechile.cl/mi-cuenta/lost-password/")
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='user_login']")))
    CHROME_BROWSER.find_element_by_id("user_login").send_keys(email)
    buttons = CHROME_BROWSER.find_elements_by_xpath("//*[contains(text(), 'Restablecer contraseña')]")
    for btn in buttons:
        btn.click()

if __name__ == "__main__":
    init_web()
    # crear_cuenta()
    # entrar_cuenta()
    # cambiar_contraseña()
    # recuperar_contraseña()
    # fuerza_bruta()
    # se debe descomentar la opcion que desea utilizar
