from datetime import datetime, timedelta
from django.db.models import Sum
from rest_framework import serializers

from users.models import UserService, UserTrialPeriod
from ..utils import get_tariff_condition, get_fut_expenses, get_past_expenses


class UserServiceRetrieveSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(source='service.image_logo_poster')
    service_name = serializers.CharField(source='service.name')
    cashback = serializers.IntegerField(source='service.cashback')
    tariff_name = serializers.CharField(source='tariff.name')
    price = serializers.IntegerField(source='expense')
    trial_period_end_date = serializers.SerializerMethodField()
    payment_date = serializers.SerializerMethodField()

    class Meta:
        model = UserService
        fields = (
            'id',
            'logo',
            'service_name',
            'tariff_name',
            'cashback',
            'payment_date',
            'end_date',
            'trial_period_end_date',
            'phone_number',
            'price'
        )

    def get_trial_period_end_date(self, obj):
        if UserTrialPeriod.objects.filter(
            user=obj.user,
            service=obj.service
        ).exists():
            return obj.service.trial_period.get(
                user=self.context['request'].user
            ).end_date
        return ''

    def get_payment_date(self, obj):
        if obj.end_date >= datetime.now().date():
            return obj.end_date + timedelta(days=1)
        return ''


class UserServiceListSerializer(UserServiceRetrieveSerializer):
    logo = serializers.ImageField(source='service.image_logo')
    is_active = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()
    period = serializers.SerializerMethodField()

    class Meta:
        model = UserService
        fields = (
            'id',
            'logo',
            'service_name',
            'tariff_name',
            'count',
            'period',
            'price',
            'payment_date',
            'end_date',
            'trial_period_end_date',
            'is_active'
        )

    def get_is_active(self, obj):
        if obj.is_active == True and obj.auto_pay == True:
            return 1
        if obj.is_active == False and obj.auto_pay == False:
            return 0
        return 3

    def get_count(self, obj):
        return get_tariff_condition(
            obj,
            self.context['request'].user
        ).count

    def get_period(self, obj):
        return get_tariff_condition(
            obj,
            self.context['request'].user
        ).period


class UserHistoryPaymentSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(source='service.image_logo')
    service_name = serializers.CharField(source='service.name')
    tariff_name = serializers.CharField(source='tariff.name')
    price = serializers.IntegerField(source='expense')
    date = serializers.DateField(source='start_date')

    class Meta:
        model = UserService
        fields = (
            'id',
            'logo',
            'service_name',
            'tariff_name',
            'cashback',
            'price',
            'status_cashback',
            'date'
        )


class ExpensesByCategorySerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = UserService
        fields = ('data',)

    def get_data(self, obj):
        for exp in get_past_expenses(obj, self.context):
            del exp['service__category__name']
            yield exp


class FutureExpensesSerializer(serializers.ModelSerializer):
    future_expenses = serializers.SerializerMethodField()

    class Meta:
        model = UserService
        fields = (
            'future_expenses',
        )

    def get_future_expenses(self, obj):
        return get_fut_expenses(obj, self.context)
