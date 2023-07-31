from home_page import HomePage
import pytest

# Думав про те що цю групу тестів можна зробити параметризованими
# але вирішив збергати принцип сінгл респонсобіліті. Тому зробив окремими тестами


@pytest.mark.positive()
def test_facebook(driver):
    """Test confirms that click on facebook icon open correct page in new tab"""

    home_page = HomePage(driver)
    home_page.click_facebook()
    driver.switch_to.window(driver.window_handles[1])

    assert driver.current_url == "https://www.facebook.com/Hillel.IT.School"


@pytest.mark.positive()
def test_telegram(driver):
    """ Test confirms that click on telegram icon open correct page in new tab"""

    home_page = HomePage(driver)
    home_page.click_telegram()
    driver.switch_to.window(driver.window_handles[1])

    assert driver.current_url == "https://t.me/ithillel_kyiv"


@pytest.mark.positive()
def test_youtube(driver):
    """ Test confirms that click on youtube icon open correct page in new tab"""

    home_page = HomePage(driver)
    home_page.click_youtube()
    driver.switch_to.window(driver.window_handles[1])

    assert driver.current_url == "https://www.youtube.com/user/HillelITSchool"


@pytest.mark.positive()
def test_instagram(driver):
    """ Test confirms that click on instagram icon open correct page in new tab"""

    home_page = HomePage(driver)
    home_page.click_instagram()
    driver.switch_to.window(driver.window_handles[1])

    assert driver.current_url == "https://www.instagram.com/hillel_itschool/"


@pytest.mark.positive()
def test_linkedin(driver):
    """ Test confirms that click on linkedin icon open correct page in new tab"""

    home_page = HomePage(driver)
    home_page.click_linkedin()
    driver.switch_to.window(driver.window_handles[1])

    assert driver.current_url == "https://www.linkedin.com/school/ithillel/"
