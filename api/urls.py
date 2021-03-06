from django.urls import path

from .views.due_views import ListDue, DetailDue, ListDueDefinition, DetailDueDefinition
from .views.savings_views import ListBank, DetailBank, ListSavedMoney, DetailSavedMoney
from .views.report_views import report

urlpatterns = [
    path('savings', ListSavedMoney.as_view()),
    path('savings/<int:pk>/', DetailSavedMoney.as_view()),
    path('bank', ListBank.as_view()),
    path('bank/<int:pk>/', DetailBank.as_view()),
    path('due', ListDue.as_view()),
    path('due/<int:pk>/', DetailDue.as_view()),
    path('due_definition', ListDueDefinition.as_view()),
    path('due_definition/<int:pk>/', DetailDueDefinition.as_view()),
    path('report', report),
]