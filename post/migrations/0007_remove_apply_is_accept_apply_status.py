# Generated by Django 4.2.2 on 2023-06-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_remove_apply_status_apply_is_accept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='is_accept',
        ),
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('under_review', '검토중'), ('accept', '수락됨'), ('reject', '거절됨')], default='under_review', max_length=15),
        ),
    ]
