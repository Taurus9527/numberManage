# Generated by Django 5.0.6 on 2024-05-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_userinfo_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]
