import re
from playwright.sync_api import Page, expect

BASE_URL = "https://vuejs.org/examples/#form-bindings"


def navigate_to_page(page, url):
    page.goto(url)


def test_text_input(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_role("textbox").click()
    page.frame_locator("iframe").get_by_role("textbox").fill("DarynaP")

    expect(page.frame_locator("iframe").get_by_text("DarynaP")).to_be_visible()


def test_uncheck(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_label("Checked: true").uncheck()
    expect(page.frame_locator("iframe").get_by_text("Checked: false")).to_be_visible()


def test_check(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_label("Checked: true").uncheck()
    page.frame_locator("iframe").get_by_label("Checked: false").check()
    expect(page.frame_locator("iframe").get_by_text("Checked: true")).to_be_visible()


def test_multi_check(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_label("John").check()
    page.frame_locator("iframe").get_by_label("Mike").check()
    page.frame_locator("iframe").get_by_label("Jack").uncheck()

    assert isinstance(expect(page.frame_locator("iframe").get_by_text("John, Mike")).to_be_visible, object)


def test_radio(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_label("Two").check()
    expect(page.frame_locator("iframe").get_by_label("Two")).to_be_enabled()


def test_select(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_role("combobox").select_option("C")
    expect(page.frame_locator("iframe").get_by_text("Selected: C")).to_be_visible()


def test_multi_select(page) -> None:
    navigate_to_page(page, BASE_URL)

    page.frame_locator("iframe").get_by_role("listbox").select_option(["A", "B", "C"])
    expect(page.frame_locator("iframe").get_by_text("Selected: [ \"A\", \"B\", \"C\" ]")).to_be_visible()