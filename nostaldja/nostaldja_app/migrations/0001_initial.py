# Generated by Django 4.0.2 on 2022-02-02 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no name', max_length=100)),
                ('image_url', models.TextField(default='no image')),
                ('description', models.TextField(default='no description')),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja_app.decade')),
            ],
        ),
    ]
