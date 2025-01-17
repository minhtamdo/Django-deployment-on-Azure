# Generated by Django 5.0.6 on 2024-08-24 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]
