from django.test import TestCase
from elsys.temperatures.api_temperatures import ApiTemperature
from unittest.mock import Mock, patch
import json

# Create your tests here.

class TestApiTemperatureModel(TestCase):
    def setUp(self):
        self.data = json.load(open('./elsys/temperatures.json'))

    def tearDown(self):
        pass

    @patch("requests.post")
    def test_minimum_temperature(self):
        mocked_requests.return_value.json = Mock(return_value = self.data)
        assert ApiTemperature.min_temp() == 3

    @patch("requests.post")
    def test_maximum_temperature(self):
        mocked_requests.return_value.json = Mock(return_value = self.data)
        assert ApiTemperature.max_temp() == 8

    @patch("requests.post")
    def test_average_temperature(self):
        mocked_requests.return_value.json = Mock(return_value = self.data)
        assert ApiTemperature.avg_temp() == 5.0
