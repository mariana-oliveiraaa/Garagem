# Generated by Django 4.1.7 on 2023-03-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_acessorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'cores',
            },
        ),
    ]
