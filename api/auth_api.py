from custom_requester.custom_requester import CustomRequester


class AuthAPI(CustomRequester):

    def auth_and_get_csrf(self, session):
        self.session.auth = ("admin", "admin")
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        if not csrf_token:
            raise ValueError("CSRF token is missing or invalid")
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})



