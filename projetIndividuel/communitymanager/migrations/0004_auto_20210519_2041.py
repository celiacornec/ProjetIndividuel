# Generated by Django 2.1.15 on 2021-05-19 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communitymanager', '0003_auto_20210518_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
                ('contenu', models.TextField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'commentaire',
                'ordering': ['date_creation'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='date_evenement',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='priorite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='communitymanager.Priorite'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communitymanager.Post'),
        ),
    ]