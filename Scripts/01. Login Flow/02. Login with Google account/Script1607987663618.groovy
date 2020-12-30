import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable

WebUI.openBrowser('')

WebUI.navigateToUrl('https://open.rocket.chat/home')

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/GoogleButton_Object'))

WebUI.delay(5)

WebUI.switchToWindowIndex('1')

WebUI.delay(10)

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/Email_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/Email_Object'), Email)

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/EmailNextButton_Object'))

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/Password_Object'))

WebUI.setEncryptedText(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/Password_Object'), '8ONjX3ggx5RmoBbvnoZOyw==')

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/Google_Objects/PasswordNextButton_Object'))

WebUI.delay(10)

WebUI.closeBrowser()
