import unittest
import moodle_locators as locators
import moode_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase):   # create class

    @staticmethod   # signal to unit test that this is a static method
    def test_create_new_user():
        methods.setUp()
        # ------ CREATE NEW USER -------------
        methods.login(locators.admin_user_name, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        # -------- LOGIN AS NEW USER -----------------
        methods.login(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        # ---------- DELETE NEW USER -----------------
        methods.login(locators.admin_user_name, locators.admin_password)
        methods.delete_user()
        methods.log_out()
        # --------------------------------------------
        methods.teardown()
