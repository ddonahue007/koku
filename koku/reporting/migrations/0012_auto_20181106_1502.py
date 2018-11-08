# Generated by Django 2.1.2 on 2018-11-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0011_auto_20181018_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('metric', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=6, max_digits=25)),
                ('timeunit', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('metric', 'price', 'timeunit')},
        ),
    ]