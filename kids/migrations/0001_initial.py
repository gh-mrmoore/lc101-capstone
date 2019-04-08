# Generated by Django 2.1.2 on 2019-04-08 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('eventsID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('eventsDate', models.DateField(verbose_name='Event Date')),
                ('eventsTime', models.TimeField()),
                ('eventsGenNote', models.CharField(max_length=40)),
                ('eventsExtendedNote', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('kidID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('kidName', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='eventsKidID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.Kids'),
        ),
    ]
