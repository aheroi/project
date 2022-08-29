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

    path('outcome_list/', views.OutcomeListView.as_view(), name='outcome_list'),
    path('outcome_detail/<pk>', views.OutcomeDetailView.as_view(), name='outcome_detail'),
    path('outcome_create/', views.OutcomeCreateView.as_view(), name='outcome_create'),
    path('outcome_update/<pk>', views.OutcomeUpdateView.as_view(), name='outcome_update'),
    path('outcome_delete/<pk>', views.OutcomeDeleteView.as_view(), name='outcome_delete'),

    path('balance_list/', views.BalanceListView.as_view(), name='balance_list'),
    path('balance_detail/<pk>', views.BalanceDetailView.as_view(), name='balance_detail'),
    path('balance_create/', views.BalanceCreateView.as_view(), name='balance_create'),
    path('balance_update/<pk>', views.BalanceUpdateView.as_view(), name='balance_update'),
    path('balance_delete/<pk>', views.BalanceDeleteView.as_view(), name='balance_delete'),

    path('current_finances/', views.current_finances, name='current_finances'),
    # path('current_finances_by_type/', views.current_finances_by_type, name='current_finances_by_type'),
    path('current_incomes_by_type/', views.current_incomes_by_type, name='current_incomes_by_type'),
    path('current_outcomes_by_type/', views.current_outcomes_by_type, name='current_outcomes_by_type'),
    # path('current_finances_label/', views.current_finances_label, name='current_finances_label'),


]