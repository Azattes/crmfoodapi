from django.contrib import admin
from crmfood_app.models import Departments, MealCategories, Meals, Tables, Order, Checks, MealsToOrder, Statuses


admin.site.register(Departments)
admin.site.register(MealCategories)
admin.site.register(Meals)
admin.site.register(Tables)
admin.site.register(Order)
admin.site.register(Checks)
admin.site.register(MealsToOrder)
admin.site.register(Statuses)