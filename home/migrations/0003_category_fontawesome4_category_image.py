# Generated by Django 4.1 on 2022-09-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Fontawesome4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Services'),
        ),
    ]