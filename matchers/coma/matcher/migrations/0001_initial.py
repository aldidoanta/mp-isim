# Generated by Django 4.2.3 on 2023-08-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_schema', models.CharField(blank=True, default='', max_length=100)),
                ('target_schema', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
