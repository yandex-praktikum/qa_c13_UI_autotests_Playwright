from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def pytest_playwright_context_args():
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True
    }

def pytest_playwright_browser_launch_args():
    return {
        "headless": True
    }
