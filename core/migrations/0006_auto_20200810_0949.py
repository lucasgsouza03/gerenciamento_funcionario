# Generated by Django 3.1 on 2020-08-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200810_0204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionarios',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='funcionario',
        ),
        migrations.RemoveField(
            model_name='funcionarios',
            name='nome',
        ),
        migrations.AddField(
            model_name='funcionarios',
            name='empresa',
            field=models.ManyToManyField(blank=True, null=True, related_name='funcionarios', to='core.Empresas'),
        ),
    ]