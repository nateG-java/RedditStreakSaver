from playwright.sync_api import sync_playwright
import datetime
import logging
import os

logging.basicConfig(
    filename="/home/youruser/streak.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s"
)

DAY = DAYS_IN_YOUR_STREAK # not required, just for fun, set to a number, or crash
DAYS_LEFT = 50 - DAY # also not required
USERNAME = "REDDIT_USERNAME"
PASSWORD = "YOUR_PASSWORD"

def keep_streak():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        )
        page = context.new_page()

        try:
            logging.info("Logging in...")
            page.goto("https://www.reddit.com/login", wait_until="networkidle")
            page.wait_for_timeout(2000)
            page.fill('input[name="username"]', USERNAME)
            page.fill('input[name="password"]', PASSWORD)
            page.click('button[type="submit"]')
            page.wait_for_timeout(4000)

            if "login" in page.url:
                raise Exception("Login failed — check your credentials")

            today = datetime.date.today().strftime("%B %d, %Y")
            page.goto(f"https://www.reddit.com/r/u_{USERNAME}/submit", wait_until="networkidle")
            page.wait_for_timeout(2000)

            page.fill('textarea[name="title"]', f"Daily check-in — {today}")
            page.wait_for_timeout(1000)

            page.click('button[type="submit"]')
            page.wait_for_timeout(3000)
            DAY += 1

            logging.info(f"Success — streak maintained for {today}")
            print(f"Done! Streak kept for {today}")
            print(f"Today was day # {DAY}. {DAYS_LEFT} until you hit 300 days!")

        except Exception as e:
            logging.error(f"Failed — {e}")
            print(f"Error: {e}")

        finally:
            browser.close()

keep_streak()
