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

CustomKeywords.'rocketchatPackage.loginKeyword.loginRocketchat'()

WebUI.maximizeWindow()

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/AddOption_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/Discussion_Object'))

WebUI.delay(5)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionParentInput_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionParentInput_Object'), 'general')

WebUI.delay(4)

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionParentInput_Object'), Keys.chord(
        Keys.ENTER))

WebUI.delay(4)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionName_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionName_Object'), GlobalVariable.DiscussionName)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionInviteUsers_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionInviteUsers_Object'), 'meherishrat')

WebUI.delay(4)

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionInviteUsers_Object'), Keys.chord(
        Keys.ENTER))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionMessage_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/DiscussionMessage_Object'), 'TestDiscussion')

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Create Objects/CreateDiscussionButton_Object'))

WebUI.delay(5)

WebUI.closeBrowser()

