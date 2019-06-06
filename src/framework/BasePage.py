from src.framework.BaseEntity import BaseEntity


class BasePage(BaseEntity):
    def __init__(self, type, locator, name):
        super().__init__(type, locator, name=name)
        self.assert_is_open()

    def assert_is_open(self):
        """
        Check that page is displayed
        """
        assert self.get_element().is_displayed()

    def refresh(self):
        """
        Refresh current page
        """
        pass

    def scroll(self, locator):
        """
        Scroll page to locator
        """
        pass

    def navigate_back_forward(self):
        """
        Click browser Back button
        """
        pass

    def get_current_link(self):
        """
        Get current link
        Returns:
            current page url
        """
        pass

    def get_page_title(self):
        """
        Get current title
        Returns:
            current page title
        """
        pass

    def get_HTML_source(self):
        """
        Get current HTML for page
        Returns:
            current page HTML
        """
        pass

    def switch_to_next_tab(self, title):
        """
        Switch to next browser tab by title
        """
        pass

    def set_windows_size(self):
        """
        Set browser window size
        """
        pass

    def set_windows_position(self):
        """
        Set browser window position
        """
        pass

    def switching_to_frame(self):
        """
        Switch to frame on page
        """
        pass
