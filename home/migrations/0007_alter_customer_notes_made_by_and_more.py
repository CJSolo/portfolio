# Generated by Django 4.0.2 on 2022-02-27 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_alter_dog_options_alter_dog_dog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_notes',
            name='made_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='madenote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer_notes',
            name='note_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mynote', to='home.customer'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dog_breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mybreed', to='home.dog_breeds'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dog_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mydog', to='home.customer'),
        ),
    ]
