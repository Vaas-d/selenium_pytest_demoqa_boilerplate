import allure


def take_screenshot(web_driver, name) -> None:
    allure.attach(
        body=web_driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
