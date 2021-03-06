# Generated by Django 2.0.5 on 2018-05-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=100)),
                ('bookName', models.CharField(max_length=100)),
                ('bookUrl', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('publishYear', models.CharField(max_length=20)),
                ('index', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=40)),
                ('catalog', models.TextField()),
            ],
        ),
    ]
