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
    CHROME_BROWSER.get("https://www.20minutos.es/")
    
def crear_cuenta(email = "tarea_cripto_usr50@yopmail.com", username = "usr_cripto_50",contraseña = r'miramenteexplico574'):
    global CHROME_BROWSER
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ui_circle_user']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='registerGigya bttn trk-cabecera-registarse']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
    WebDriverWait(CHROME_BROWSER, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(email)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys(username)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(contraseña)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='passwordRetype']"))).send_keys(contraseña)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='data.acceptTerms']"))).click()
    time.sleep(1)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gigya-input-submit']"))).send_keys(Keys.RETURN)



def entrar_cuenta(email = "tarea_cripto_usr50@yopmail.com",contraseña = r'miramenteexplico574'):
    global CHROME_BROWSER
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui_circle_user']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='loginGigya bttn trk-cabecera-entrar']"))).click()
    WebDriverWait(CHROME_BROWSER, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(email)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(contraseña)
    time.sleep(1)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gigya-input-submit']"))).send_keys(Keys.RETURN)
    
    
    
def cambiar_contraseña(email = "tarea_cripto_usr50@yopmail.com",contraseña = 'miramenteexplico574', nueva_contraseña = "nuevacontraseñamaster789"):
    global CHROME_BROWSER
    entrar_cuenta(email, contraseña)
    time.sleep(2)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ui_circle_user']"))).click()
    time.sleep(3)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='profileGigya bttn']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='gigya-composite-control gigya-composite-control-link']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gigya-password-password']"))).send_keys(contraseña)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gigya-password-newPassword']"))).send_keys(nueva_contraseña)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='gigya-password-passwordRetype']"))).send_keys(nueva_contraseña)
    time.sleep(1)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gigya-input-submit']"))).send_keys(Keys.RETURN)    

def recuperar_contraseña(email = "tarea_cripto_usr50@yopmail.com" ):
    global CHROME_BROWSER
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui_circle_user']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='loginGigya bttn trk-cabecera-entrar']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='gigya-forgotPassword gigya-composite-control gigya-composite-control-link']"))).click()
    time.sleep(2)
    CHROME_BROWSER.find_element_by_name("username").send_keys(email)
    time.sleep(1)
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gigya-input-submit']"))).send_keys(Keys.RETURN)    


def fuerza_bruta(email = "tarea_cripto_usr50@yopmail.com",charset = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789", repeticiones = 100, mincaracteres = 8):
    stuff = split(charset)
    counter = 0
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ui_circle_user']"))).click()
    WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='loginGigya bttn trk-cabecera-entrar']"))).click()
    WebDriverWait(CHROME_BROWSER, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(email)
    for L in range(mincaracteres + 1, len(stuff)+1):
        for subset in itertools.combinations_with_replacement(stuff, L):
            if counter >= repeticiones:
                break
            WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).clear()
            time.sleep(1)
            WebDriverWait(CHROME_BROWSER, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(''.join(subset))
            time.sleep(1)
            WebDriverWait(CHROME_BROWSER, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gigya-input-submit']"))).send_keys(Keys.RETURN)
            print( str(counter) +":",''.join(subset))
            counter += 1



if __name__ == "__main__":
    init_web()
    # crear_cuenta()
    # entrar_cuenta()
    # cambiar_contraseña()
    # recuperar_contraseña()
    # fuerza_bruta()
    # se debe descomentar la opcion que desea utilizar

