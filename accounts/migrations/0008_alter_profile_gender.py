# Generated by Django 4.2.2 on 2023-06-22 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('남성', '남성'), ('여성', '여성'), ('기타', '기타')], default='etc', max_length=8, null=True),
        ),
    ]
