# Generated by Django 4.2 on 2024-12-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField(auto_now=True)),
                ('readcount', models.IntegerField(default=0)),
            ],
        ),
    ]