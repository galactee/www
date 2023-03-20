# Generated by Django 4.1.7 on 2023-03-20 21:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("permanence", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="permanenceday",
            options={
                "verbose_name": "Jour de Permanence",
                "verbose_name_plural": "Jours de Permanence",
            },
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_amount_1",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Nombre d'appels 1"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_amount_2",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Nombre d'appels 2"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_amount_3",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Nombre d'appels 3"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_amount_4",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Nombre d'appels 4"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_duration_1",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Durée d'appel 1"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_duration_2",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Durée d'appel 2"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_duration_3",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Durée d'appel 3"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="call_duration_4",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="Durée d'appel 4"
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="inscrite_1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="inscrite_2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="inscrite_3",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="permanenceday",
            name="inscrite_4",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
