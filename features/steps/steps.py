from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then

driver = Chrome()

@given("the user is on the page form")
def step_the_user_is_on_the_form_page(context):
    driver.get("https://demoqa.com/automation-practice-form")
@when("the user fills out the form correctly")
def step_the_fill_out_the_form_correctly(context):
    elem = driver.find_element(By.ID, "firstName")
    elem.send_keys("CAMARO")
    elem = driver.find_element(By.ID, "lastName")
    elem.send_keys("AMARELO")
    elem = driver.find_element(By.ID, "userEmail")
    elem.send_keys("camaro@amarelo.com")
    select = driver.find_element(By.ID, 'gender-radio-1')
    driver.execute_script("arguments[0].click();", select)
    elem = driver.find_element(By.ID, "userNumber")
    elem.send_keys("6940028922",Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-3-input")
    elem.send_keys("NCR", Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-4-input")
    elem.send_keys("Noida",Keys.TAB)
@when("the user sends form")
def step_the_user_is_on_the_form_page(context):
    elem = driver.find_element(By.ID, "userNumber")        
    elem = driver.find_element(By.ID, "react-select-3-input")
    elem.send_keys(Keys.TAB)
    elem.send_keys(Keys.TAB)
    elem.send_keys(Keys.ENTER)
@when("the user fills out the form with an invalid email address")
def step_the_user_fills_out_the_form_with_an_invalid_email_address(context):
    elem = driver.find_element(By.ID, "firstName")
    elem.send_keys("CAMARO")
    elem = driver.find_element(By.ID, "lastName")
    elem.send_keys("AMARELO")
    elem = driver.find_element(By.ID, "userEmail")
    elem.send_keys("camaroamarelo")
    select = driver.find_element(By.ID, 'gender-radio-1')
    driver.execute_script("arguments[0].click();", select)
    elem = driver.find_element(By.ID, "userNumber")
    elem.send_keys("6940028922",Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-3-input")
    elem.send_keys("NCR", Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-4-input")
    elem.send_keys("Noida")
@when("the user fills out the form with an invalid contact number")
def step_the_user_fills_out_the_form_with_an_invalid_contact_number(context):
    elem = driver.find_element(By.ID, "firstName")
    elem.send_keys("CAMARO")
    elem = driver.find_element(By.ID, "lastName")
    elem.send_keys("AMARELO")
    elem = driver.find_element(By.ID, "userEmail")
    elem.send_keys("camaro@amarelo.com")
    select = driver.find_element(By.ID, 'gender-radio-1')
    driver.execute_script("arguments[0].click();", select)
    elem = driver.find_element(By.ID, "userNumber")
    elem.send_keys("40028922",Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-3-input")
    elem.send_keys("NCR", Keys.TAB)
    elem = driver.find_element(By.ID, "react-select-4-input")
    elem.send_keys("Noida")   
@when("the user refreshes the page form")
def step_the_user_refreshes_the_page_form(context):
    driver.refresh()
    elem = driver.find_element(By.ID, "firstName")
    elem = driver.find_element(By.ID, "lastName")
    elem = driver.find_element(By.ID, "userEmail")
    elem = driver.find_element(By.ID, "userNumber")

    assert not(elem.get_attribute("value")=="CAMARO")
    assert not(elem.get_attribute("value")=="AMARELO")
    assert not(elem.get_attribute("value")=="camaro@amarelo.com")
    assert not(elem.get_attribute("value")=="6940028922")
@then("the user see a message that indicates success in terminal")
def step_the_user_see_a_message_that_indicates_success_in_terminal(context):
    try:
        elemento_confirmacao = driver.find_element(By.ID, "example-modal-sizes-title-lg")
        assert elemento_confirmacao.is_displayed()
        print("Form sent successfully")
    except NoSuchElementException:
        print("The form could not be sent")

@then('the user see an error message indicating an invalid data "{message}" in terminal')
def step_the_user_an_error_message_indicating_invalid_email_in_terminal(context, message):
    try:
        elemento_confirmacao = driver.find_element(By.ID, "example-modal-sizes-title-lg")
        if elemento_confirmacao.is_displayed():
            raise Exception
    except NoSuchElementException:
        match message:
            case "email":
                print("The form could not be sent - invalid email")
            case "contact number":
                print("The form could not be sent - invalid contact number")
            case "blank form":
                print("The form could not be sent - blank form")
            case "reloaded form":
                print("The form could not be sent - reloaded form")
            case _:
                raise Exception
    except Exception:
        print("An error has occurred")