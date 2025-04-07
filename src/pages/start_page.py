from playwright.sync_api import Page

class StartPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, base_url: str):
        """Navigates to the base URL of the game."""
        self.page.goto(base_url)

    def fill_payer_name(self, player_name: str):
        self.page.fill("#player-name", player_name)

    def click_add_player_button(self):
        """Clicks the 'Lägg till spelare' button."""
        self.page.click("text=Lägg till spelare")

    def player_timer_visible(self, player_name: str) -> bool:
        """Checks if a timer is visible for the given player."""
        return self.page.is_visible(f"text={player_name}")

    def get_player_list(self):
        """Returns the list of added player names."""
        return [element.inner_text() for element in self.page.query_selector_all("section div")]

    def is_pause_button_visible(self) -> bool:
        """Checks if the pause button is visible."""
        return self.page.is_visible("text=Pause")


