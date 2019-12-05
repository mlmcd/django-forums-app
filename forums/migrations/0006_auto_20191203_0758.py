# Generated by Django 2.2.5 on 2019-12-03 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('forums', '0005_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads',
                                    to='forums.Forum'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='text',
            field=models.TextField(default='<empty>'),
        ),
    ]
