from enum import Enum

from django.db import models


# Create your models here.
class SexEnum(Enum):
    M = 'Masculino'
    F = 'Feminino'
    TM = 'Trans Masculino'
    TF = 'Trans Feminino'
    O = 'Outro'


class HowKnowAboutClinic(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Como conheceu a clínica'
        verbose_name_plural = 'Como conheceu a clínica'


class Patient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    birth_date = models.DateField(verbose_name='Data de nascimento')
    id_number = models.CharField(max_length=50, verbose_name='RG')
    phone_number = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.CharField(max_length=50, verbose_name='Email')
    sex = models.CharField(max_length=50, verbose_name='Sexo', choices=[(tag, tag.value) for tag in SexEnum])
    address = models.CharField(max_length=50, verbose_name='Endereço')
    how_know_about_clinic = models.ForeignKey(
        HowKnowAboutClinic,
        on_delete=models.PROTECT,
        verbose_name='Como conheceu a clínica'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class UserTypeEnum(Enum):
    HOLDER = 'Titular'
    DEPENDENT = 'Dependente'


class DentalPlan(models.Model):
    convenant_name = models.CharField(max_length=50, verbose_name='Nome do convênio')
    card_number = models.CharField(max_length=50, verbose_name='Número do cartão')
    plan_name = models.CharField(max_length=50, verbose_name='Nome do plano')
    user_type = models.CharField(
        max_length=50,
        verbose_name='Tipo de usuário',
        choices=[(tag, tag.value) for tag in UserTypeEnum]
    )
    holder_name = models.CharField(max_length=50, verbose_name='Nome do titular')
    ans_code = models.CharField(max_length=50, verbose_name='Código da ANS')

    def __str__(self):
        return self.convenant_name

    class Meta:
        verbose_name = 'Plano odontológico'
        verbose_name_plural = 'Planos odontológicos'


class TransactionStatusEnum(Enum):
    IN = 'Entrada'
    OUT = 'Saída'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Transaction(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    date = models.DateTimeField(verbose_name='Data')
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product_transactions',
        verbose_name='Produto'
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name='patient_transactions',
        verbose_name='Paciente'
    )
    description = models.CharField(max_length=50, verbose_name='Descrição')
    status = models.CharField(
        max_length=50,
        verbose_name='Status',
        choices=[(tag, tag.value) for tag in TransactionStatusEnum]
    )
    value = models.FloatField(verbose_name='Valor')
    accumulated = models.FloatField(verbose_name='Acumulado')

    def __str__(self):
        return f"{self.title} - {self.date}"

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'


class Expense(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'


class Supplier(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
