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

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage_OR/input_Login_emailOrUsername'), GlobalVariable.userName)

WebUI.setText(findTestObject('Rocketchat_OR/LoginPage_OR/input_Login_pass'), GlobalVariable.userPassword)

WebUI.click(findTestObject('Rocketchat_OR/LoginPage_OR/button_Login'))

WebUI.waitForPageLoad(15)

WebUI.click(findTestObject('Rocketchat_OR/Homepage/DirectUser_Object'))

WebUI.waitForPageLoad(5, FailureHandling.STOP_ON_FAILURE)

WebUI.click(findTestObject('Rocketchat_OR/Homepage/ChatWindowTextarea_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage/ChatWindowTextarea_Object'), 'A message to test reaction')

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage/ChatWindowTextarea_Object'), Keys.chord(Keys.ENTER))

WebUI.mouseOver(findTestObject('Rocketchat_OR/Homepage/ReactionMessage_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage/AddReaction_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage/SmileyInput_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage/SmileyInput_Object'), 'Smiley')

WebUI.waitForElementVisible(findTestObject('Rocketchat_OR/Homepage/Smileyemoji_Object'), 5)

WebUI.click(findTestObject('Rocketchat_OR/Homepage/Smileyemoji_Object'))

WebUI.delay(3)

WebUI.closeBrowser()

