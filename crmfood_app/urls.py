from django.urls import path
from crmfood_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("statuses", views.StatusesViewSet)


app_name = 'crmfood_app'
urlpatterns = [
    path('meals/', views.MealsAPIView.as_view(), name='meals'),
    path('meals/<int:pk>/', views.MealsDetail.as_view(), name='meals_detail'),
    path('tables/', views.TablesAPIView.as_view(), name='tables'),
    path('tables/<int:pk>', views.TablesDetail.as_view(), name='tables_detail'),
    path('departments/', views.DepartmentsAPIView.as_view(), name='departments'),
    path('departments/<int:pk>', views.DepartmentsDetail.as_view(),
         name='departments_detail'),
    path('mealcategories/', views.MealCategoriesAPIView.as_view(),
         name='mealcategories'),
    path('mealcategories/<int:pk>', views.MealCategoriesDetail.as_view(),
         name='mealcategories_detail'),
    # path('statuses/', views.StatusesAPIView.as_view(), name = 'statuses'),
    # path('statuses/<int:pk>', views.StatusesDetail.as_view(), name = 'statuses_detail'),
    path('servicepercentage/', views.ServicePercentageAPIView.as_view(),
         name='servicepercentage'),
    path('orders/', views.OrderAPIView.as_view(), name='orders'),
    path('orders<int:pk>/', views.OrderDetail.as_view(), name='orders_detail'),
    path('checks/', views.ChecksAPIView.as_view(), name='checks'),
    path('checks/<int:pk>', views.ChecksDetail.as_view(), name='checks_detail'),
    path('mealstoorder/', views.MealsToOrderAPIView.as_view(), name='mealstoorder'),
    path('mealstoorder/<int:pk>', views.MealsToOrderDetail.as_view(),
         name='mealstoorder_detail'),
    path('categoriesByDepartment/<int:pk>/',
         views.MealCategoriesByDepartment.as_view(), name='categoriesByDepartment'),
]


urlpatterns += router.urls
