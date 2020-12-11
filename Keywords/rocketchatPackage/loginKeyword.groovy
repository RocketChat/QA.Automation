package rocketchatPackage

import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject

import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.checkpoint.Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling
import com.kms.katalon.core.testcase.TestCase
import com.kms.katalon.core.testdata.TestData
import com.kms.katalon.core.testobject.TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows

import internal.GlobalVariable

public class loginKeyword {
	@Keyword
	def loginRocketchat (String) {
		
		WebUI.navigateToUrl('https://open.rocket.chat/home')
		
		WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_emailOrUsername'), GlobalVariable.userName)
		
		WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_pass'), GlobalVariable.userPassword)
		
		WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/button_Login'))
		
		WebUI.waitForPageLoad(10)
	}
}
