from rest_framework import serializers
from django_filters import rest_framework as filters
from dateapp.models import Search,Table

class Search_Serializer (serializers.ModelSerializer):
    class Meta:
        model=Search
        fields=('male_number','female_number','situation','time')

class Table_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields=('table_name', 'describe')

class FilterSearch(filters.FilterSet):
    search_name= filters.CharFilter(lookup_expr='contains')

    class Meta:
        model=Search
        fields=('male_number','female_number','situation','time')


class FilterTable(filters.FilterSet):
    table_name=filters.CharFilter(lookup_expr='contains')

    class Meta:
        model=Table
        fields=('table_name', 'describe')

