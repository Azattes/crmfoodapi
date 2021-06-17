from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from crmfood_app import serializers
from rest_framework import status, generics, viewsets
from crmfood_app.models import Departments, Tables, Statuses, MealCategories, Meals, MealsToOrder, Order, Checks
from crmfood_app.serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import CoachAccessPermission


class DepartmentsAPIView(APIView):
    def get(self, request):
        departments = Departments.objects.all()
        serializer = DepartmentsSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentsDetail(APIView):
    def get(self, request, pk, format=None):
        departments = Departments.objects.get(pk=pk)
        serializer = DepartmentsSerializer(departments)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        departments = Departments.objects.get(pk=pk)
        departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        departments = Departments.objects.get(pk=pk)
        serializer = serializers.DepartmentsSerializer(
            departments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TablesAPIView(APIView):
    def get(self, request):
        tables = Tables.objects.all()
        serializer = TablesSerializer(tables, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TablesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TablesDetail(APIView):
    def get(self, request, pk, format=None):
        tables = Tables.objects.get(pk=pk)
        serializer = TablesSerializer(tables)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        tables = Tables.objects.get(pk=pk)
        tables.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        tables = Tables.objects.get(pk=pk)
        serializer = serializers.TablesSerializer(tables, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusesAPIView(APIView):
    def get(self, request):
        statuses = Statuses.objects.all()
        serializer = StatusesSerializer(statuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StatusesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusesDetail(APIView):
    def get(self, request, pk, format=None):
        statuses = Statuses.objects.get(pk=pk)
        serializer = StatusesSerializer(statuses)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        statuses = Statuses.objects.get(pk=pk)
        statuses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        statuses = Statuses.objects.get(pk=pk)
        serializer = serializers.StatusesSerializer(
            statuses, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealCategoriesAPIView(APIView):
    def get(self, request):
        mealcategories = MealCategories.objects.all()
        serializer = MealCategoriesSerializer(mealcategories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealCategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealCategoriesDetail(APIView):
    def get(self, request, pk, format=None):
        mealcategories = MealCategories.objects.get(pk=pk)
        serializer = MealCategoriesSerializer(mealcategories)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        mealcategories = MealCategories.objects.get(pk=pk)
        mealcategories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        mealcategories = MealCategories.objects.get(pk=pk)
        serializer = serializers.MealCategoriesSerializer(
            mealcategories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealCategoriesByDepartment(generics.RetrieveAPIView):
    model = Departments
    queryset = Departments.objects.all()
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        categories = MealCategories.objects.filter(departmentid=instance.id)
        serializer = MealCategoriesSerializer(categories, many=True)
        return Response(serializer.data)


class MealsAPIView(APIView):
    def get(self, request):
        meals = Meals.objects.all()
        serializer = MealsSerializer(meals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealsDetail(APIView):
    def get(self, request, pk, format=None):
        meals = Meals.objects.get(pk=pk)
        serializer = MealsSerializer(meals)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        meals = Meals.objects.get(pk=pk)
        meals.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        meals = Meals.objects.get(pk=pk)
        serializer = serializers.MealsSerializer(meals, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealsToOrderAPIView(APIView):
    def get(self, request):
        mealstoorder = MealsToOrder.objects.all()
        serializer = MealsToOrderSerializer(mealstoorder, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealsToOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealsToOrderDetail(APIView):
    def get(self, request, pk, format=None):
        mealstoorder = MealsToOrder.objects.get(pk=pk)
        serializer = MealsToOrderSerializer(mealstoorder)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        mealstoorder = MealsToOrder.objects.get(pk=pk)
        mealstoorder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        mealstoorder = MealsToOrder.objects.get(pk=pk)
        serializer = serializers.MealsToOrderSerializer(
            mealstoorder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    def get(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        order = Order.objects.get(pk=pk)
        serializer = serializers.OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChecksAPIView(APIView):
    def get(self, request):
        checks = Checks.objects.all()
        serializer = ChecksSerializer(checks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChecksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChecksDetail(APIView):
    def get(self, request, pk, format=None):
        checks = Checks.objects.get(pk=pk)
        serializer = ChecksSerializer(checks)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        checks = Checks.objects.get(pk=pk)
        checks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        checks = Checks.objects.get(pk=pk)
        serializer = serializers.ChecksSerializer(checks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicePercentageAPIView(APIView):
    def get(self, request):
        servicepercentage = ServicePercentage.objects.all()
        serializer = ServicePercentageSerializer(servicepercentage, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicePercentageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicePercentageDetail(APIView):
    def get(self, request, pk, format=None):
        servicepercentage = ServicePercentage.objects.get(pk=pk)
        serializer = ServicePercentageSerializer(servicepercentage)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        servicepercentage = ServicePercentage.objects.get(pk=pk)
        servicepercentage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        servicepercentage = ServicePercentage.objects.get(pk=pk)
        serializer = serializers.ServicePercentageSerializer(
            servicepercentage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CoachAccessPermission]
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer
