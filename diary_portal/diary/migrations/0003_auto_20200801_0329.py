# Generated by Django 3.0.8 on 2020-08-01 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_remove_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remarks',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='remarks', to='diary.Company'),
        ),
    ]
