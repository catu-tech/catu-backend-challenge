# Generated by Django 3.2.23 on 2023-11-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('who', models.CharField(max_length=100)),
                ('action_type', models.CharField(max_length=100)),
                ('object_type', models.CharField(max_length=100)),
                ('object_id', models.IntegerField()),
            ],
        ),
    ]
