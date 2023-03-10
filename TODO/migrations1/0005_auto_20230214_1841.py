# Generated by Django 3.2.8 on 2023-02-14 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0004_remove_project_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note_daytime_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='note_project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='TODO.project'),
        ),
    ]
