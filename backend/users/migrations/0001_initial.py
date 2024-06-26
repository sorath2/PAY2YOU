# Generated by Django 3.2.16 on 2024-04-02 13:27

import uuid

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserTrialPeriod',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата завершения')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trial_period', to='services.service', verbose_name='Сервис')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trial_period', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'пробный период пользователя',
                'verbose_name_plural': 'Пробный период пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserSpecialCondition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата завершения')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_conditions', to='services.tariff', verbose_name='Тариф')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_conditions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'специальное условие для пользователя',
                'verbose_name_plural': 'Специальные условия для пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField(verbose_name='Дата начала подписки на сервис')),
                ('end_date', models.DateField(verbose_name='Дата окончания подписки на сервис')),
                ('expense', models.PositiveSmallIntegerField(verbose_name='Сумма')),
                ('cashback', models.PositiveSmallIntegerField(verbose_name='Кэшбек')),
                ('status_cashback', models.BooleanField(verbose_name='Статус зачисления кэшбека')),
                ('is_active', models.BooleanField(verbose_name='Активность подписки')),
                ('auto_pay', models.BooleanField(default=True, verbose_name='Автоплатеж')),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(regex='^\\+79[0-9]{9}$')], verbose_name='Номер телефона')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_services', to='services.service', verbose_name='Сервис')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_services', to='services.tariff', verbose_name='Тариф')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_services', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'подписка пользователя',
                'verbose_name_plural': 'Подписки пользователя',
            },
        ),
        migrations.AddConstraint(
            model_name='usertrialperiod',
            constraint=models.UniqueConstraint(fields=('user', 'service'), name='unique_user_service'),
        ),
        migrations.AddConstraint(
            model_name='userspecialcondition',
            constraint=models.UniqueConstraint(fields=('user', 'tariff'), name='unique_user_tariff'),
        ),
    ]
