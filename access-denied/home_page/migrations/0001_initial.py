# Generated by Django 3.1.4 on 2020-12-24 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=25, null=True)),
                ('last_donation_date', models.DateField(blank=True, null=True)),
                ('disease', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]