from selenium import webdriver
driver = webdriver.Chrome(executable_path="/home/sahiljariwala/Desktop/SEM_4/SEPP/lab/selenium/chromedriver_linux64/chromedriver")
driver.get("http://127.0.0.1:8000/login")
driver.find_element_by_name("username").send_keys("xyz")
driver.find_element_by_name("password").send_keys("abcd6796")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.get("http://127.0.0.1:8000/bus")
driver.find_element_by_name("source").send_keys("Ahmedabad")
driver.find_element_by_name("destination").send_keys("Surat")
driver.find_element_by_name("type").send_keys("AC")
driver.find_element_by_name("date").send_keys("04/09/2021")
driver.find_element_by_xpath("//input[@type='submit']").click()
