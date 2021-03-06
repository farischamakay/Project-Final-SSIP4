# Generated by Django 3.1.1 on 2021-01-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TierList', '0008_auto_20210102_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='element',
            field=models.ManyToManyField(to='TierList.Element'),
        ),
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.ManyToManyField(to='TierList.Gender'),
        ),
        migrations.AddField(
            model_name='character',
            name='nation',
            field=models.ManyToManyField(to='TierList.Nation'),
        ),
        migrations.AddField(
            model_name='character',
            name='weapon',
            field=models.ManyToManyField(to='TierList.Weapon'),
        ),
    ]
