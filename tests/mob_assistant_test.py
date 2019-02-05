from hamcrest import *
import unittest

import mob_assistant


class TestMobAssistant(unittest.TestCase):
    def setUp(self):
        pass

    def test_package_name(self):
        assert_that(mob_assistant.name, is_('mob_assistant'))
