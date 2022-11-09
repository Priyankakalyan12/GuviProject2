from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import randint
import time


class Orange:
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(20)

    # method to login to OrangeHRM
    def login(self, url, userName, pwd):
        self.driver.get(url)

        userNameBox = self.driver.find_element(by=By.XPATH, value="//input[@name='username']")
        userNameBox.send_keys(userName)

        pwdBox = self.driver.find_element(by=By.XPATH, value="//input[@name='password']")
        pwdBox.send_keys(pwd)

        loginBtn = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        loginBtn.click()
        timeout = 15
        element_present = EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"))
        WebDriverWait(self.driver, timeout).until(element_present)


    # method to add new Employee
    def addNewEmployee(self,firstName,middleName,lastName):
        addBtn = self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
        addBtn.click()

        firstNameField = self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
        firstNameField.send_keys(firstName)

        middleNameField = self.driver.find_element(by=By.XPATH,
                                                  value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
        middleNameField.send_keys(middleName)

        lastNameField = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
        lastNameField.send_keys(lastName)

        id=randint(1000, 9999)

        employeeIdField = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input")
        employeeIdField.send_keys(id)

        saveButton = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
        saveButton.click()
        time.sleep(5)

        saveButton2 = self.driver.find_element(by=By.XPATH,
                                              value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")
        saveButton2.click()
        time.sleep(5)

    def addNewEmployeeInAdmin(self,firstName,newUsername,newPwd):
        adminLink = self.driver.find_element(by=By.XPATH,
                                               value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
        adminLink.click()

        addBtn = self.driver.find_element(by=By.XPATH,
                                          value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
        addBtn.click()

        employeeNameField = self.driver.find_element(by=By.XPATH,
                                          value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input")
        employeeNameField.send_keys(firstName)
        time.sleep(5)

        selectEmployee=self.driver.find_element(by=By.XPATH,
                                          value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span")
        time.sleep(5)
        selectEmployee.click()

        #//div[@class='oxd-form-row']//div[@class='oxd-autocomplete-option'//span[contains(text(),'prateek')]
        # employeeNameField.send_keys(Keys.ARROW_DOWN)
        # employeeNameField.send_keys(Keys.ENTER)

        userRoleField = self.driver.find_element(by=By.XPATH,
                                                     value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        userRoleField.click()

        selectESS = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[3]/span")

        selectESS.click()



        status = self.driver.find_element(by=By.XPATH,
                                                     value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div")
        status.click()

        enabledStatus = self.driver.find_element(by=By.XPATH,
                                          value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]/span")
        enabledStatus.click()

        usernameField = self.driver.find_element(by=By.XPATH,
                                                   value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
        usernameField.send_keys(newUsername)

        pwdField = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
        pwdField.send_keys(newPwd)

        confirmPwdField = self.driver.find_element(by=By.XPATH,
                                            value="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
        confirmPwdField.send_keys(newPwd)
        time.sleep(3)

        saveButton = self.driver.find_element(by=By.XPATH,
                                                    value="//*[@id='app']//div[@class='oxd-form-actions']//button[@type='submit']")

        saveButton.click()
        time.sleep(3)

    #method to search user in Admin section
    def searchUserInAdminSection(self,newUsername):
        time.sleep(2)
        username = self.driver.find_element(by=By.XPATH,
                                            value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
        username.send_keys(newUsername)
        time.sleep(2)

        searchButton = self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        searchButton.click()
        time.sleep(3)

        userNameInResults=self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div")

        return userNameInResults

    #method to logout from application
    def logout(self):
        userdropdown=self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i")
        userdropdown.click()

        logoutLink= self.driver.find_element(by=By.XPATH,
                                                 value="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
        logoutLink.click()























