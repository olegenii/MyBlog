# Generated by Django 3.0.5 on 2020-04-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.TextField()),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
            ],
        ),
    ]
