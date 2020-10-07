# Generated by Django 2.2.10 on 2020-02-21 20:34
import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("reporting", "0097_auto_20200221_1331")]

    operations = [
        migrations.CreateModel(
            name="OCPNodeLabelLineItemDaily",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("cluster_id", models.CharField(max_length=50, null=True)),
                ("cluster_alias", models.CharField(max_length=256, null=True)),
                ("node", models.CharField(max_length=253, null=True)),
                ("usage_start", models.DateTimeField()),
                ("usage_end", models.DateTimeField()),
                ("node_labels", django.db.models.JSONField(null=True)),
                ("total_seconds", models.IntegerField()),
                (
                    "report_period",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="reporting.OCPUsageReportPeriod"
                    ),
                ),
            ],
            options={"db_table": "reporting_ocpnodelabellineitem_daily"},
        )
    ]
