from rest_framework import serializers
from crmfood_app.models import Departments, MealCategories, Meals, Tables, Order, Checks, MealsToOrder, Statuses, ServicePercentage


class StatusesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statuses
        fields = ['id', 'name']


class TablesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tables
        fields = ['id', 'name']


class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = ['id', 'name']


class MealCategoriesSerializer(serializers.ModelSerializer):

    departmentid = serializers.PrimaryKeyRelatedField(queryset = Departments.objects.all())

    class Meta:
        model = MealCategories
        fields = ['id', 'name', 'departmentid']


class MealsSerializer(serializers.ModelSerializer):

    categoryid = serializers.PrimaryKeyRelatedField(queryset = MealCategories.objects.all())

    class Meta:
        model = Meals
        fields = ['id', 'name', 'categoryid', 'price', 'description']


class MealsToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model= MealsToOrder
        fields = ['id', 'order']


class OrderSerializer(serializers.ModelSerializer):

    tableid = serializers.PrimaryKeyRelatedField(queryset = Tables.objects.all())
    mealsid = MealsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'isitopen', 'waiterid', 'date', 'tableid', 'tablename', 'mealsid']

    def get_table_name(self, obj):
        table = obj.table_id
        return str(table)


class ChecksSerializer(serializers.ModelSerializer):

    meals = MealsSerializer(many=True)

    class Meta:
        model = Checks
        fields = ['order', 'date', 'servicefree', 'totalsum', 'meals']

    # order = models.ForeignKey(Order, related_name='order', on_delete = models.CASCADE)
    # date = models.DateTimeField(auto_now_add=True)
    # servicefree = models.IntegerField()
    # totalsum = models.IntegerField()
    # meals = models.ForeignKey(Meals, related_name='meals', on_delete=models.CASCADE)


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = ['percentage']