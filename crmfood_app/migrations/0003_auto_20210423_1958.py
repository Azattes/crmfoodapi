# Generated by Django 3.2 on 2021-04-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmfood_app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checks',
            name='meals',
        ),
        migrations.AddField(
            model_name='checks',
            name='meals',
            field=models.ManyToManyField(to='crmfood_app.Meals'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='mealsid',
        ),
        migrations.AddField(
            model_name='order',
            name='mealsid',
            field=models.ManyToManyField(to='crmfood_app.Meals'),
        ),
    ]
