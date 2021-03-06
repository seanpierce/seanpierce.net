# Generated by Django 3.1.1 on 2020-09-09 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_work_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.work')),
            ],
        ),
    ]
