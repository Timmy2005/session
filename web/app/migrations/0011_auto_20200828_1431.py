# Generated by Django 3.1 on 2020-08-28 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_usersettings_selected_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProgress',
            fields=[
                ('completed_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_completed', models.DateTimeField(auto_now=True)),
                ('group_index', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionCompleted',
            fields=[
                ('completed_session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_completed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['user'], name='app_group_user_id_294657_idx'),
        ),
        migrations.AddField(
            model_name='sessioncompleted',
            name='group_progress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.groupprogress'),
        ),
        migrations.AddField(
            model_name='sessioncompleted',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.session'),
        ),
        migrations.AddField(
            model_name='sessioncompleted',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupprogress',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AddField(
            model_name='groupprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='sessioncompleted',
            index=models.Index(fields=['user', 'group_progress'], name='app_session_user_id_c2c389_idx'),
        ),
        migrations.AddIndex(
            model_name='groupprogress',
            index=models.Index(fields=['user'], name='app_grouppr_user_id_01116c_idx'),
        ),
    ]