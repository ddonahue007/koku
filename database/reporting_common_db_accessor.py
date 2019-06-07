#
# Copyright 2018 Red Hat, Inc.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Downloader for cost usage reports."""

from collections import defaultdict

from masu.database.koku_database_access import KokuDBAccess


class ReportingCommonDBAccessor(KokuDBAccess):
    """Class to interact with customer reporting tables."""

    # pylint: disable=too-few-public-methods
    class ReportingCommonSchema:
        """A container for the shared reporting table objects."""

    def __init__(self, schema='public'):
        """Establish the database connection."""
        super().__init__(schema)
        self.report_common_schema = self.ReportingCommonSchema()
        self._get_reporting_tables()
        self.column_map = self.generate_column_map()

    def _get_reporting_tables(self):
        """Load table objects for reference and creation."""
        base = self.get_base()

        for table in base.classes:
            if 'reporting_common' in table.__name__:
                setattr(self.report_common_schema, table.__name__, table)

            if 'region_mapping' in table.__name__:
                setattr(self, f'_{table.__name__}', table)

    # pylint: disable=arguments-differ
    def _get_db_obj_query(self, table_name):
        """Create a query for a database object.

        Args:
            table_name (str): The name of the table to create

        Returns:
            (Query): A SQLALchemy query object on the table

        """
        table = getattr(self.report_common_schema, table_name)
        return self._session.query(table)

    def generate_column_map(self):
        """Generate a mapping of provider data columns to db columns."""
        column_map = defaultdict(dict)

        report_column_map = \
            self._get_db_obj_query('reporting_common_reportcolumnmap').all()

        for row in report_column_map:
            entry = {row.provider_column_name: row.database_column}
            column_map[row.database_table].update(entry)

        return column_map

    def add(self, table, fields, use_savepoint=True):
        """
        Add a new row to the database.

        Args:
            table (string): Table name
            fields (dict): Fields containing attributes.
                    Valid keys are the table's fields.

        Returns:
            None

        """
        new = getattr(self, f'_{table.lower()}')(**fields)
        if use_savepoint:
            self.savepoint(self._session.add, new)
        else:
            self._session.add(new)
