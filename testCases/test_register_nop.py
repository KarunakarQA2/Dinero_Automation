import time

import pytest

from pageObjects.HomePge_nop import Homepage
from pageObjects.Register_nop import Register
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestRegister:
    logger = LogGen.loggen()
    url = ReadConfig.getApplicationURL()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register(self,setup):
        self.logger.info("******* STARTED THE LOGS *********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        # Objects for pageObjects
        self.home = Homepage(self.driver)
        self.reg = Register(self.driver)

        self.home.clickRegister()

        self.reg.setGender()
        self.reg.setFirstName("Karunakar")
        self.reg.setLastName("Chavadam")
        self.email_ran = randomString.random_string_generator()+"@gmail.com"
        self.reg.setEmail(self.email_ran)
        self.reg.setPassword("12345678")
        self.reg.setConfirPassword("12345678")
        self.reg.setContinue()
        self.message = self.reg.setConfirmtext()


        if self.message == "Your registration completed":
            assert True
        else:
            path = '/home/karunakar/PycharmProjects/Dinero_UI_Automation/screenshots/'
            self.driver.save_screenshot(path+"test_register_1.png")
            assert False