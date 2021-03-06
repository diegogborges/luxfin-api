from rest_framework import serializers
from savings.models import Bank, Saved_Money, Receive


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bank


class SavedMoneySerializer(serializers.ModelSerializer):
    bank = BankSerializer()

    class Meta:
        fields = '__all__'
        model = Saved_Money


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Receive