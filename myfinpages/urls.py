from django.urls import path

from myfinpages import views

app_name = 'myfinpages'

urlpatterns = [
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_detail/<pk>', views.IncomeDetailView.as_view(), name='income_detail'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
    path('income_update/<pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('income_delate/<pk>', views.IncomeDeleteView.as_view(), name='income_delete'),
]