# Generated by Django 2.0.5 on 2018-05-31 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='report_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='comment',
            name='is_blocked',
            field=models.BooleanField(default=False, verbose_name='노출 제한'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]
