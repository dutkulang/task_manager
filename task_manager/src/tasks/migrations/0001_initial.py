# Generated by Django 5.1.5 on 2025-01-28 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('details', models.TextField()),
                ('assigned_to', models.CharField(max_length=39)),
                ('status', models.CharField(choices=[('C', 'Completed'), ('P', 'Pending'), ('S', 'Started'), ('A', 'Abandon')], max_length=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=30)),
            ],
        ),
    ]
