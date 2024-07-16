# Generated by Django 5.0.7 on 2024-07-15 11:45

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.UUIDField(default=uuid.uuid4)),
                ('slug', models.SlugField(unique=True)),
                ('clients_email', models.EmailField(max_length=254, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('open', 'open'), ('pending', 'pending'), ('closed', 'closed')], default='open', max_length=100)),
                ('attachments', models.ImageField(null=True, upload_to='attachments/')),
                ('accepted_on', models.DateTimeField(blank=True, null=True)),
                ('closed_on', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
