from selenium.webdriver.common.by import By

from PrivateProject.functions import General
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

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
general.fill_order_call_submission("Dor", "dorkokotek9@gmail.com", "0509102112")
general.click_send_in_order_call_popup()

general.click_send_in_footer_help_bar(trying_to_fail=True)
general.fill_footer_how_can_we_help_submission("Dor", "dorkokotek9@gmail.com", "0509102112")
general.click_send_in_footer_help_bar()

general.driver.close()
print("No Bugs were found!")
