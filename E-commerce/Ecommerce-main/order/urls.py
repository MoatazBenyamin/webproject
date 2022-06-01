from django.urls import path

from order import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),  
    path('chart/', views.index, name='dashboard-index'),
    path('pie-chart/', views.index2, name='dashboard-index2'),
    path('line-chart/', views.index3, name='dashboard-index3'),
    path('RankingReport/', views.rankingindex , name= 'dashboard-rankingindex'),
]