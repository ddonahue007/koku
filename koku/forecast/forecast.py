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
"""Base forecasting module."""
from api.models import Provider


class Forecast:
    """Base forecasting class."""

    def __init__(self, query_params):
        """Class Constructor."""
        pass

    def predict(self):
        """Execute forecast and return prediction."""
        return [0, 1, 2, 3, 4]


class AWSForecast(Forecast):
    """Azure forecasting class."""

    provider = Provider.PROVIDER_AWS


class AzureForecast(Forecast):
    """Azure forecasting class."""

    provider = Provider.PROVIDER_AZURE


class OCPForecast(Forecast):
    """OCP forecasting class."""

    provider = Provider.PROVIDER_OCP


class OCPAWSForecast(Forecast):
    """OCP+AWS forecasting class."""

    provider = Provider.OCP_AWS


class OCPAzureForecast(Forecast):
    """OCP+Azure forecasting class."""

    provider = Provider.OCP_AZURE


class OCPAllForecast(Forecast):
    """OCP+All forecasting class."""

    provider = Provider.OCP_ALL
