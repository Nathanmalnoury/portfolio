# Generated by Django 3.0.3 on 2020-02-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200211_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
