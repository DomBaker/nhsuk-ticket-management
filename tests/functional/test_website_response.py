from flask import url_for
from flask_testing import TestCase
import unittest


from main import app


class TestApp(TestCase):
    def create_app(self):
        return app


class TestResponse(TestApp):
    # AUTH TESTS
    def test_login_response(self):
        """GIVEN
        WHEN
        THEN"""
        response = self.client.get(url_for("auth.login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_response(self):
        """GIVEN
        WHEN
        THEN"""
        response = self.client.get(url_for("auth.logout"))
        self.assertEqual(response.status_code, 302)

    def test_register_response(self):
        """GIVEN
        WHEN
        THEN"""
        response = self.client.get(url_for("auth.register"))
        self.assertEqual(response.status_code, 200)

    # VIEW Tests
    # Page returns 302 as login is required
    def test_home_response(self):
        response = self.client.get(url_for("views.home"))
        self.assertEqual(response.status_code, 302)

    def test_create_ticket_response(self):
        response = self.client.get(url_for("views.create_ticket"))
        self.assertEqual(response.status_code, 302)

    def test_view_ticket_response(self):
        response = self.client.get(url_for("views.view_ticket"))
        self.assertEqual(response.status_code, 302)

    def test_admin_nav_page_response(self):
        response = self.client.get(url_for("views.admin_nav_page"))
        self.assertEqual(response.status_code, 302)

    def test_admin_view_ticket_response(self):
        response = self.client.get(url_for("views.admin_view_ticket"))
        self.assertEqual(response.status_code, 302)

    def test_admin_view_users_response(self):
        response = self.client.get(url_for("views.admin_view_users"))
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
