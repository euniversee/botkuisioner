import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Lenovo\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument(r"--profile-directory=Person 1")
driver = webdriver.Chrome(options=options)
driver.get('https://students.unpad.ac.id/pacis/akademik/transkrip_nilai')


while True:
    element = WebDriverWait(driver, 999999999).until(EC.presence_of_element_located((By.ID, 'pilih_1748')))
    for i in range(1748, 1838, 10):
        try:
            p = driver.find_element(By.ID, f"pilih_{i}")
            if p.is_selected(): 
                time.sleep(1)
                driver.find_element(By.ID, "simpan").click()
            else:
                p.click()
        except NoSuchElementException:
            continue 


