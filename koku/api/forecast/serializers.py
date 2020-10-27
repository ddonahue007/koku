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
"""Forecast Serializers."""
from api.report.serializers import FilterSerializer


class ForecastSerializer(FilterSerializer):
    """Base Forecast Serializer."""


class AWSCostForecastSerializer(ForecastSerializer):
    """AWS Cost Forecast Serializer."""


class AzureCostForecastSerializer(ForecastSerializer):
    """Azure Cost Forecast Serializer."""


class OCPCostForecastSerializer(ForecastSerializer):
    """OCP Cost Forecast Serializer."""


class OCPAWSCostForecastSerializer(ForecastSerializer):
    """OCP+AWS Cost Forecast Serializer."""


class OCPAzureCostForecastSerializer(ForecastSerializer):
    """OCP+Azure Cost Forecast Serializer."""


class OCPAllCostForecastSerializer(ForecastSerializer):
    """OCP+All Cost Forecast Serializer."""
