from PrivateProject.functions import General

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

general.driver.close()
print("No Bugs were found!")
