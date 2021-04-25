from django.db import models
from user.models import User

class Departments(models.Model):
    name = models.CharField(max_length=200)


class MealCategories(models.Model):
    name = models.CharField(max_length=100)
    departmentid = models.ForeignKey(Departments, on_delete=models.CASCADE)


class Meals(models.Model):
    name = models.CharField(max_length=150)
    categoryid = models.ForeignKey(MealCategories, related_name='categories', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=500)


class Tables(models.Model):
    name = models.CharField(max_length=100)


class ServicePercentage(models.Model):
    percentage = models.IntegerField()

class Order(models.Model):
    waiterid = models.ForeignKey(User, related_name='waiterid', on_delete=models.CASCADE)
    tableid = models.ForeignKey(Tables, related_name='table', on_delete=models.CASCADE)
    tablename = models.CharField(max_length=100)
    isitopen = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    mealsid = models.ManyToManyField(Meals)


class Checks(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefree = models.IntegerField()
    totalsum = models.IntegerField()
    meals = models.ManyToManyField(Meals)

class MealsToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Statuses(models.Model):
    name = models.CharField(max_length=100)

