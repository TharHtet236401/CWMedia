# Generated by Django 5.1.6 on 2025-03-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('myanmar', 'Myanmar'), ('indonesia', 'Indonesia'), ('philippines', 'Philippines'), ('singapore', 'Singapore'), ('malaysia', 'Malaysia'), ('tournament', 'Tournament'), ('other', 'Other')], default='other', max_length=200, null=True),
        ),
    ]
