# Generated by Django 4.1.7 on 2023-03-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JuliusPort', '0003_blog_blog_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
