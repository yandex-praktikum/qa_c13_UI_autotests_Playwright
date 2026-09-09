import os
import pytest
from playwright.sync_api import Page


@pytest.fixture
def page(browser, request):
    page = browser.new_page()

    yield page

    # TODO: если тест завершился с ошибкой, сохранить скриншот
    # Подсказка: используйте request.node.rep_call.failed
    # Скриншоты сохраняйте в папку screenshots/

    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
