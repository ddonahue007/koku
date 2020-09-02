# Generated by Django 2.2.15 on 2020-09-01 22:45
import pkgutil

import django.db.models.deletion
from django.db import connection
from django.db import migrations
from django.db import models
from jinjasql import JinjaSql

from koku import pg_partition as ppart


def resummarize_tags(apps, schema_editor):
    jinja_sql = JinjaSql()
    sql_files = [
        "sql/reporting_awstags_summary.sql",
        "sql/reporting_azuretags_summary.sql",
        "sql/reporting_ocpawstags_summary.sql",
        "sql/reporting_ocpazuretags_summary.sql",
    ]
    for sql_file in sql_files:
        agg_sql = pkgutil.get_data("masu.database", sql_file)
        agg_sql = agg_sql.decode("utf-8")
        agg_sql_params = {"schema": ppart.resolve_schema(ppart.CURRENT_SCHEMA)}
        agg_sql, agg_sql_params = jinja_sql.prepare_query(agg_sql, agg_sql_params)
        with connection.cursor() as cursor:
            cursor.execute(agg_sql, params=list(agg_sql_params))


class Migration(migrations.Migration):

    dependencies = [("reporting", "0132_auto_20200901_1811")]

    operations = [
        migrations.RunSQL(
            """
                DELETE FROM reporting_awstags_summary_values_mtm;
                DELETE FROM reporting_azuretags_summary_values_mtm;
                DELETE FROM reporting_ocpawstags_summary_values_mtm;
                DELETE FROM reporting_ocpazuretags_summary_values_mtm;

                DELETE FROM reporting_awstags_summary;
                DELETE FROM reporting_azuretags_summary;
                DELETE FROM reporting_ocpawstags_summary;
                DELETE FROM reporting_ocpazuretags_summary;

                DELETE FROM reporting_awstags_values;
                DELETE FROM reporting_azuretags_values;
                DELETE FROM reporting_ocpawstags_values;
                DELETE FROM reporting_ocpazuretags_values
            """
        ),
        migrations.RunPython(resummarize_tags),
    ]