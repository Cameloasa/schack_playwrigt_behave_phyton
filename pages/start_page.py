from playwright.sync_api import Page
import re

class StartPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, base_url: str):
        self.page.goto(base_url)

    def fill_player_name(self, player_name: str):
        """Fills the player name input field with the given name."""
        print("URL curent:", self.page.url)
        self.page.get_by_role("textbox").wait_for(timeout=10000)
        self.page.get_by_role("textbox").fill(player_name)

    def click_add_player_button(self):
        """Clicks the 'Lägg till spelare' button."""
        self.page.get_by_role("button").get_by_text("Lägg till spelare").click(timeout=10000)

    def player_timer_visible(self, player_name: str):
        """Checks if a timer is visible for the given player."""
        # Adaptăm de la prof: verificăm numele + timer cu regex
        locator = self.page.locator(".player").get_by_text(re.compile(player_name + r"\s+0:00.0"))
        return locator.is_visible()

    def is_pause_button_visible(self):
        return self.page.is_visible("text=Pausa")