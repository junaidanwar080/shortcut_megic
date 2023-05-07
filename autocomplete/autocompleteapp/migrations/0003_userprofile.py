# Generated by Django 4.0.5 on 2023-04-19 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autocompleteapp', '0002_company_shortcuts_shortcut_type_shortcuts_company_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.TextField(blank=True, max_length=20)),
                ('created_on', models.DateField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('Updated_on', models.DateField(blank=True, null=True)),
                ('Updated_by', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]