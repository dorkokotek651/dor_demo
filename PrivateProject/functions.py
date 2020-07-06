from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class General:
    def __init__(self):
        pass

    driver = webdriver.Chrome()

    def verify_header_logo_strip(self):
        header_logo = self.driver.find_elements_by_css_selector("#logom")
        if not header_logo:
            raise Exception("Header logo was not found in automation assignment page")

        header_logo_phrase = self.driver.find_elements_by_css_selector("[class*=logo__TextContainer-sc] span")
        if not header_logo_phrase:
            raise Exception("Header logo phrase was not found in automation assignment page")
        logo_strip_text = ""
        for part in header_logo_phrase:
            logo_strip_text += part.text + " "
        logo_strip_text = logo_strip_text[:-1]
        assert logo_strip_text == 'מפתחים בשפה שלך', "Logo text does not match desired text"

    def verify_introduction_strip_text(self):
        introduction_strip = self.driver.find_elements_by_css_selector("[class*='introduction__Introduction-sc']")
        if not introduction_strip:
            raise Exception("Introduction strip was not found in automation assignment page")

        introduction_title = introduction_strip[0].find_element_by_css_selector("[class*='typography__DesktopTitle']")
        assert introduction_title.text == "הירולו - מובילים בפיתוח", "introduction strip title is wrong"

        introduction_line_1 = introduction_strip[0].find_element_by_css_selector(
            "[class*='introduction__TextDesk']").text
        assert introduction_line_1 == "הירולו היא חברת פיתוח מובילה המתמחה בפתרונות Front-End ו-Full Stack.", \
            "Introduction line 1 text is wrong"
        introduction_line_2_and_3 = introduction_strip[0].find_elements_by_css_selector("h4")
        assert introduction_line_2_and_3[0].text == "עד היום, בנינו מאות אפליקציות ווב" \
                                               " ומובייל עבור עשרות לקוחות באמצעות הטכנולוגיות החדישות ביותר בתעשייה.", \
            "Introduction line 2 text is wrong"
        assert introduction_line_2_and_3[1].text == "אם אתם זקוקים לפיתוח מכל סוג או הרחבה וחיזוק צוות הפיתוח שלכם – " \
                                               "הגעתם למקום הנכון.",\
            "Introduction line 3 text is wrong"

    def verify_single_how_can_we_help_strip_card(self):
        help_card = self.driver.find_elements_by_css_selector(
            "[class*='services__CardsContainer'] > [class*='serviceCard']")
        if not help_card:
            raise Exception("Info cards were not found in 'How Can We help Strip'")

        outsourcing_card_title = help_card[0].find_element_by_css_selector("h3").text
        assert outsourcing_card_title == "מיקור חוץ לפיתוח Frontend ובודקי איכות", "outsourcing card title is wrong"
        outsourcing_card_description = help_card[0].find_element_by_css_selector("p span").text
        assert outsourcing_card_description == "אנחנו בונים צוותים המורכבים ממפתחי Full Stack, צד לקוח" \
                                               " (React, Angular, Vue), בודקי איכות (ידני ואוטומציה) ומנהלי פרויקטים." \
                                               " בעזרתנו תוכלו להקים במהירות צוות טכנולוגי איכותי וממוקצע.", \
            "outsourcing_card_description is wrong"

    def verify_links_social_media_links(self):
        links = self.driver.find_elements_by_css_selector("[class*='socialMediaBar__container'] a")
        assert links[0].get_attribute("href") == "https://www.linkedin.com/company/herolo/", "Linkedin link is wrong"
        assert links[1].get_attribute("href") == "https://api.whatsapp.com/send?phone=972544945333",\
            "WhatsApp link is wrong"
        assert links[2].get_attribute("href") == "https://www.facebook.com/Herolofrontend", "Facebook link is wrong"
        assert links[3].get_attribute("href") == "https://herolo.co.il/?lang=he", \
            "Herolo official website link is wrong"

    def test_whatsapp_side_link(self):
        whatsapp_side_btn = self.driver.find_elements_by_css_selector("[class*='callUsWhatsapp__BtnWhatsapp-sc']")
        if not whatsapp_side_btn:
            raise Exception("WhatsApp side button was not found")
        assert "whatsapp.com" in whatsapp_side_btn[0].get_attribute("href"), "WhatsApp side link is wrong"

    def test_projects_for_example_carousel(self):
        number_of_slides = self.driver.find_elements_by_css_selector("[class*='portfolio__Portfolio-sc'] li")
        slide_right_btn = self.driver.find_element_by_css_selector(".slick-next")
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_right_btn)
        for i in range(len(number_of_slides) + 1):
            slide_right_btn.click()
            sleep(1)
        assert number_of_slides[0].get_attribute("class") == "slick-active", \
            "carousel did not go back to the first slide"

    def verify_customers_carousel_functionality(self):
        customers_carousel = self.driver.find_element_by_css_selector("[class*='customers__Slider']")
        self.driver.execute_script("arguments[0].scrollIntoView();", customers_carousel)

        first_slide = wait(self.driver, 12).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "[class*='customers__Slider'] li:nth-child(1).slick-active")))

        counter = 4
        last_slide = None
        for i in range(4):
            last_slide = wait(self.driver, 5).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, "[class*='customers__Slider'] li:nth-child(" + str(counter) + ").slick-active")))
            counter -= 1

        assert last_slide == first_slide, "Customers carousel did not make a full round"







