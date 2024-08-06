from .import views

from django.urls import path

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/',views.item,name='item'),
    path('<int:pk>',views.FoodDetail.as_view(), name='detail'),
    path('add',views.create_item, name='create_item'),
    path('update/<int:id>/',views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name="delete_item"),
    
]
