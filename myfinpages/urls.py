from django.urls import path

from myfinpages import views

app_name = 'myfinpages'


## for @login_required
# urlpatterns = [
#     path('income_list/', views.IncomeListView, name='income_list'),
#     path('income_detail/<pk>', views.IncomeDetailView, name='income_detail'),
#     path('income_create/', views.IncomeCreateView, name='income_create'),
#     path('income_update/<pk>', views.IncomeUpdateView, name='income_update'),
#     path('income_delete/<pk>', views.IncomeDeleteView, name='income_delete'),
# ]
urlpatterns = [
    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_detail/<pk>', views.IncomeDetailView.as_view(), name='income_detail'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),
    path('income_update/<pk>', views.IncomeUpdateView.as_view(), name='income_update'),
    path('income_delete/<pk>', views.IncomeDeleteView.as_view(), name='income_delete'),
]