# Generated by Django 2.1 on 2019-03-20 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_freelancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_freelancer', to=settings.AUTH_USER_MODEL),
        ),
    ]
