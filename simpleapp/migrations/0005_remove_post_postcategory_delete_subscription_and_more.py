# Generated by Django 4.2.4 on 2023-09-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0004_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postCategory',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='simpleapp.PostCategory', to='simpleapp.category'),
        ),
    ]
