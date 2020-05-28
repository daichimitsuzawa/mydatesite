from rest_framework import viewsets
from .models import Search, Table
from .serializers import Search_Serializer,Table_Serializer,FilterSearch,FilterTable

class Search_ViewSet(viewsets.ModelViewSet):
    queryset=Search.objects.all()
    serializer_class=Search_Serializer

class Table_Viewset(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=Table_Serializer

class FilterSearch_ViewSet(viewsets.ModelViewSet):
    queryset=Search.objects.all()
    serializer_class=Search_Serializer
    filter_class=FilterSearch


class FilterTable_ViewSet(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=Search_Serializer
    filter_class=FilterTable
