# Generated by Django 2.0.1 on 2020-04-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='posts',
            name='post_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]