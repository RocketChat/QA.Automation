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

WebUI.mouseOver(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/DyanmicChannel_Object'))

String value = WebUI.getText(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/DynamicChannelLabel_Object'))

//String value = WebUI.getAttribute(findTestObject('null'), 'text')
WebUI.comment('the value is:' + value)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/MoreOptions_Object/ChannelMoreOptions_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/MoreOptions_Object/LeaveChannelOption_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/MoreOptions_Object/LeaveChannelButton_Object'))

WebUI.delay(5)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/Directory_Object'))

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchChannelInput_Object'))

WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchChannelInput_Object'), value)

WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchChannelInput_Object'), Keys.chord(Keys.ENTER))

//when general search works
//WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchButton_Object'))
//WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'))
//WebUI.setText(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'), value)
//WebUI.sendKeys(findTestObject('Rocketchat_OR/Homepage Objects/Search Objects/SearchInput_Object'), Keys.chord(Keys.ENTER))
// Search in directory
WebUI.waitForPageLoad(10)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/channelElement_Object'))

WebUI.delay(5)

WebUI.click(findTestObject('Rocketchat_OR/Homepage Objects/Private Channel Objects/JoinButton_Object'))

WebUI.delay(5)

WebUI.closeBrowser()

