# Generated by Django 4.2.1 on 2023-08-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_contact_email_alter_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('Number', models.CharField(max_length=10)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
