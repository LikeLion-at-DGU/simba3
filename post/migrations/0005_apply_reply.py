# Generated by Django 4.2.2 on 2023-06-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_apply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='reply',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
