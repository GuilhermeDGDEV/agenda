# Generated by Django 3.2.9 on 2021-11-11 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_alter_evento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(null=True, verbose_name='Descrição do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
