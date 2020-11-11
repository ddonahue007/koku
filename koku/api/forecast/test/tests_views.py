#
# Copyright 2020 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Forecast view unit tests."""
from django.core.cache import caches
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from api.iam.test.iam_test_case import IamTestCase
from api.iam.test.iam_test_case import RbacPermissions

# from api.forecast.views import AWSCostForecastView
# from api.forecast.views import AzureCostForecastView
# from api.forecast.views import OCPAllCostForecastView
# from api.forecast.views import OCPAWSCostForecastView
# from api.forecast.views import OCPAzureCostForecastView
# from api.forecast.views import OCPCostForecastView


class AWSCostForecastViewTest(IamTestCase):
    """Tests the AWSCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions({"aws.account": {"read": ["*"]}, "aws.organizational_unit": {"read": ["*"]}})
    def test_get_forecast(self):
        """Test that getting a forecast works."""
        url = reverse("aws-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @RbacPermissions({"aws.account": {"read": ["*"]}, "aws.organizational_unit": {"read": ["*"]}})
    def test_get_forecast_invalid(self):
        """Test that getting a forecast works."""
        url = "%s?invalid=parameter" % reverse("aws-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @RbacPermissions({"aws.account": {"read": ["*"]}, "aws.organizational_unit": {"read": ["*"]}})
    def test_get_forecast_date_filter(self):
        """Test that getting a forecast works with datetime filters."""
        filters = [
            (reverse("aws-cost-forecasts"), -1, "month", "monthly"),
            (reverse("aws-cost-forecasts"), -2, "month", "monthly"),
            (reverse("aws-cost-forecasts"), -10, "day", "daily"),
            (reverse("aws-cost-forecasts"), -30, "day", "daily"),
        ]
        for f in filters:
            with self.subTest(filters=f):
                url = "%s?filter[time_scope_value]=%s&filter[time_scope_units]=%s&filter[resolution]=%s" % f
                client = APIClient()
                response = client.get(url, **self.headers)
                self.assertEqual(response.status_code, status.HTTP_200_OK)


class AzureCostForecastViewTest(IamTestCase):
    """Tests the AzureCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions({"azure.subscription_guid": {"read": ["*"]}})
    def test_get_forecast(self):
        """Test that gettng a forecast works."""
        url = reverse("azure-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OCPCostForecastViewTest(IamTestCase):
    """Tests the OCPCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions({"openshift.cluster": {"read": ["*"]}, "openshift.node": {"read": ["*"]}})
    def test_get_forecast(self):
        """Test that gettng a forecast works."""
        url = reverse("openshift-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OCPAWSCostForecastViewTest(IamTestCase):
    """Tests the OCPAWSCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions(
        {
            "aws.account": {"read": ["*"]},
            "aws.organizational_unit": {"read": ["*"]},
            "openshift.cluster": {"read": ["*"]},
            "openshift.node": {"read": ["*"]},
        }
    )
    def test_get_forecast(self):
        """Test that gettng a forecast works."""
        url = reverse("openshift-aws-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OCPAzureCostForecastViewTest(IamTestCase):
    """Tests the OCPAzureCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions(
        {
            "azure.subscription_guid": {"read": ["*"]},
            "openshift.cluster": {"read": ["*"]},
            "openshift.node": {"read": ["*"]},
        }
    )
    def test_get_forecast(self):
        """Test that gettng a forecast works."""
        url = reverse("openshift-azure-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OCPAllCostForecastViewTest(IamTestCase):
    """Tests the OCAllPCostForecastView."""

    def setUp(self):
        """Set up the rate view tests."""
        super().setUp()
        caches["rbac"].clear()

    @RbacPermissions({"openshift.cluster": {"read": ["*"]}, "openshift.node": {"read": ["*"]}})
    def test_get_forecast(self):
        """Test that gettng a forecast works."""
        url = reverse("openshift-all-cost-forecasts")
        client = APIClient()
        response = client.get(url, **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)