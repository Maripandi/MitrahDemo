# Generated by Django 2.2.26 on 2022-02-01 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220201_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Designation'),
        ),
    ]
