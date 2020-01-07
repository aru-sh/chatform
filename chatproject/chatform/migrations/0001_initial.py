# Generated by Django 3.0.2 on 2020-01-07 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='chatform.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.CharField(max_length=200)),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender', to='chatform.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.CharField(max_length=200)),
                ('jobid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='chatform.Profile')),
            ],
        ),
    ]