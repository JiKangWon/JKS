# Generated by Django 5.1.1 on 2024-12-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0003_chapter_link_alter_term_total_of_months'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='link',
        ),
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(default='http://example.com', max_length=250, verbose_name='Nguồn khóa học'),
            preserve_default=False,
        ),
    ]
