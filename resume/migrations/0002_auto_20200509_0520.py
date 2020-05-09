# Generated by Django 2.2 on 2020-05-09 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to={'model__in': ('contactdetail', 'achievement', 'skill', 'interest', 'internship', 'education', 'experience', 'project', 'certification', 'recommendation')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
