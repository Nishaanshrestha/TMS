# Generated by Django 5.0.4 on 2024-04-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='src',
        ),
        migrations.AddField(
            model_name='attachment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='attachment/', verbose_name='image'),
        ),
    ]
