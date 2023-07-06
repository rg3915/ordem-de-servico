# Generated by Django 4.2.3 on 2023-07-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordemservicoitem',
            options={'ordering': ('-pk',), 'verbose_name': 'item da ordem de serviço', 'verbose_name_plural': 'itens da ordens de serviço'},
        ),
        migrations.AlterField(
            model_name='ordemservicoitem',
            name='proxima_visita',
            field=models.DateField(blank=True, null=True, verbose_name='Próxima Visita'),
        ),
    ]