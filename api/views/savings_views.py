from rest_framework import generics, status
from savings.models import Bank, Saved_Money, Receive
from ..serializers.savings_serializers import BankSerializer, SavedMoneySerializer, ReceiveSerializer


class ListBank(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class DetailBank(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ListSavedMoney(generics.ListCreateAPIView):
    queryset = Saved_Money.objects.all()
    serializer_class = SavedMoneySerializer


class DetailSavedMoney(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saved_Money.objects.all()
    serializer_class = SavedMoneySerializer


class ListReceive(generics.ListCreateAPIView):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer