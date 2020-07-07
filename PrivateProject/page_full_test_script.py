from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PrivateProject.functions import General
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def full_page_test():
    general = General()
    general.driver.get("https://automation.herolo.co.il")
    general.driver.maximize_window()

    general.verify_header_logo_strip()

    general.verify_introduction_strip_text()

    general.verify_single_how_can_we_help_strip_card()

    general.verify_links_social_media_links()

    general.test_whatsapp_side_link()

    general.test_projects_for_example_carousel()

    general.verify_customers_carousel_functionality()

    wait(general.driver, 15).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "[class*='onUnloadPopup__ModalWrapper']")))

    general.click_send_in_order_call_popup(trying_to_fail=True)

    general.fill_generic_contact_request_submission("onUnloadPopup", "Dor", "dorkoko@@gmail.co", "abcdefg")
    general.verify_error_messages_in_any_form("onUnloadPopup", "כתובת אימייל לא חוקית", "מספר טלפון לא חוקי")

    general.fill_generic_contact_request_submission(
        "onUnloadPopup", "Dor", "dorkokotek9@gmail.com", "0509102112", clear_first=True)
    general.click_send_in_order_call_popup()

    footer_bar = general.driver.find_element_by_id("footer")
    assert footer_bar.is_displayed(), "Footer bar is suppose to be displayed when it's not end of the page"

    general.driver.execute_script("window.scrollBy(0, 10000);")
    wait(general.driver, 3).until(EC.invisibility_of_element((By.ID, "footer")))
    assert not footer_bar.is_displayed(), "Footer bar is not suppose to be displayed when in end of the page"

    general.driver.execute_script("window.scrollBy(0, -1000);")
    wait(general.driver, 3).until(EC.visibility_of_element_located((By.ID, "footer")))
    general.click_send_in_footer_help_bar(trying_to_fail=True)

    general.fill_generic_contact_request_submission("Footer", "Dor", "dorkoko@@gmail.co", "abcdefg")
    general.verify_error_messages_in_any_form("Footer", "כתובת אימייל לא חוקית", "מספר טלפון לא חוקי")

    general.fill_generic_contact_request_submission(
        "Footer", "Dor", "dorkokotek9@gmail.com", "0509102112", clear_first=True)
    general.click_send_in_footer_help_bar()

    general.click_talk_to_us_button_in_want_to_here_more_form(trying_to_fail=True)

    general.fill_want_to_here_more_fields("Dor", "Company", "dorkoko", "0505")
    errors = wait(general.driver, 3).until(EC.visibility_of_any_elements_located((
                By.CSS_SELECTOR, "[class*='commun__ErrorText']")))  # type: List[WebElement]
    assert errors[0].text == "כתובת אימייל לא חוקית", "Email error message is incorrect"
    assert errors[1].text == "מספר טלפון לא חוקי", "Phone error message is incorrect"

    general.fill_want_to_here_more_fields("", "", "@gmail.com", "911268")
    general.click_talk_to_us_button_in_want_to_here_more_form()

    back_to_top_btn = general.driver.find_element_by_css_selector("[class*='backToTop']")
    assert not back_to_top_btn.is_displayed(), "Back to top button should be displayed only when not in top of the page"

    general.driver.execute_script("window.scrollBy(0, 10000);")
    wait(general.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class*='backToTop']")))
    assert back_to_top_btn.is_displayed(), "Back to top button should be displayed when in end of the page"

    general.click_scroll_back_to_top_btn()
    assert not back_to_top_btn.is_displayed(), "Back to top button should be gone after using it"

    general.driver.close()


if __name__ == "__main__":
    full_page_test()
    print("No Bugs were found!")
