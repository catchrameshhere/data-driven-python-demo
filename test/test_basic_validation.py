

def test_page_title_validation(driver):
    expected_title = 'Facebook – log in or sign up'
    actual_title = driver.title
    assert actual_title == expected_title


def test_url_validation(driver):
    expected_url = 'https://www.facebook.com/'
    actual_url = driver.current_url
    assert expected_url == actual_url

