# Generated by Django 4.1.10 on 2023-08-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dentalplan',
            options={'verbose_name': 'Plano odontológico', 'verbose_name_plural': 'Planos odontológicos'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
        migrations.AlterModelOptions(
            name='howknowaboutclinic',
            options={'verbose_name': 'Como conheceu a clínica', 'verbose_name_plural': 'Como conheceu a clínica'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': 'Transação', 'verbose_name_plural': 'Transações'},
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='howknowaboutclinic',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
    ]
