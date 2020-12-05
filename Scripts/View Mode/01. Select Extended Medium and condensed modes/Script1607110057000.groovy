import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import internal.GlobalVariable as GlobalVariable

WebUI.openBrowser('')

WebUI.navigateToUrl('https://open.rocket.chat/home')

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_emailOrUsername'), GlobalVariable.userName)

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_pass'), GlobalVariable.userPassword)

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/button_Login'))

WebUI.waitForPageLoad(15)

//Extended Mode
WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/ViewMode_Object'))

WebUI.check(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/Extended_Object'))

WebUI.delay(5)

WebUI.doubleClick(findTestObject('Rocketchat_OR/Homepage Objects/Menu objects/Home_Object'))
//Medium Mode

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/ViewMode_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/Medium_Object'))

WebUI.delay(5)

WebUI.doubleClick(findTestObject('Rocketchat_OR/Homepage Objects/Menu objects/Home_Object'))
//Condensed Mode

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/ViewMode_Object'))

WebUI.check(findTestObject('Rocketchat_OR/Homepage Objects/View Mode objects/Condensed_Object'))

WebUI.delay(5)

WebUI.doubleClick(findTestObject('Rocketchat_OR/Homepage Objects/Menu objects/Home_Object'))

WebUI.delay(5)

WebUI.closeBrowser()

