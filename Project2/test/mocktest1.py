from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock

import mock


class TestMock(TestCase):

    @patch('source.main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 3), 9)

    # @patch('source.main.Calculator')
    def test_sum_new(self):
        calMock = mock.patch('source.main.Calculator')
        calMock.return_value = Mock()
        cal_insatance = calMock.return_value
        cal_insatance.sum.return_value = 6
        # cal.sum_new.return_value = 6
        obj = Mock()
        self.assertEqual(cal_insatance.sum(), 6)

