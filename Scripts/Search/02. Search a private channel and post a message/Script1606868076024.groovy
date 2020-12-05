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
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('https://open.rocket.chat/home')

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_emailOrUsername'), GlobalVariable.userName)

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage Objects/input_Login_pass'), GlobalVariable.userPassword)

WebUI.click(findTestObject('Rocketchat_OR/LoginPage Objects/button_Login'))

WebUI.waitForPageLoad(15)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/searchButton_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'), GlobalVariable.PrivateChannel)

WebUI.delay(3)

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'), Keys.chord(Keys.ENTER))

WebUI.waitForElementVisible(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/ChannelTextarea_Object'), 0)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/ChannelTextarea_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/ChannelTextarea_Object'), GlobalVariable.MessageText)

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/ChannelTextarea_Object'), Keys.chord(Keys.ENTER))

WebUI.delay(5)

WebUI.closeBrowser()

