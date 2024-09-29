# Generated by Django 5.0.6 on 2024-07-13 06:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_category_productclass_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock', models.BigIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='app.color')),
                ('product_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_classify', to='app.productclass')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='app.size')),
            ],
        ),
    ]
