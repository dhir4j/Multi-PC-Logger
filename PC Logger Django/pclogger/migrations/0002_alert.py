# Generated by Django 4.1.7 on 2023-04-08 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pclogger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('is_approved', models.BooleanField(default=False)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pclogger.pc')),
            ],
        ),
    ]
