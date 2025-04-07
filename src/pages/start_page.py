from playwright.sync_api import Page

class StartPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, base_url: str):
        """Navigates to the base URL of the game."""
        self.page.goto(base_url)

    def fill_payer_name(self, player_name: str):
        self.page.fill("#player-name", player_name)


