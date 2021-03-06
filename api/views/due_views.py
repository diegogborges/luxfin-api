from rest_framework import generics, status
from due.models import Due, Due_Definition
from category.models import Category
from ..serializers.due_serializers import DueSerializer, DueDefinitionSerializer


class ListDue(generics.ListCreateAPIView):
    queryset = Due.objects.all()
    serializer_class = DueSerializer


class DetailDue(generics.RetrieveUpdateDestroyAPIView):
    queryset = Due.objects.all()
    serializer_class = DueSerializer


class ListDueDefinition(generics.ListCreateAPIView):
    queryset = Due_Definition.objects.all()
    serializer_class = DueDefinitionSerializer


class DetailDueDefinition(generics.RetrieveUpdateDestroyAPIView):
    dues = Due_Definition.objects.raw(
        "SELECT dd.`value`, dd.`day_pay`, dd.`time_initial`, d.`due_description`, c.`id` "
        +" FROM due_due_definition dd"
        +" INNER JOIN due_due d ON d.id = dd.`due_id`"
        +" INNER JOIN category_category c ON c.`id` = d.category_id;")

    print("dueee:", dues)

    due2 = Due_Definition.objects.all().values_list("due_id").union
    (Due.objects.all().values_list("id"))

    print(due2)
    queryset = Due_Definition.objects.all()
    serializer_class = DueDefinitionSerializer