from datetime import date
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required       # only for current_finances

from myfinpages.forms import IncomeForm, OutcomeForm, BalanceForm
from myfinpages.models import Income, Outcome, Balance
# Create your views here.


# @login_required(login_url='/accounts/login/')
class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    paginate_by = 100
    template_name = 'myfinpages/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Income'}
    # queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income_list'

    # allow_empty = True


# @login_required
class IncomeDetailView(LoginRequiredMixin, DetailView):
    model = Income
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Income'}
    # queryset = Income.objects.all()

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'


# @login_required
class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    # fields = ['value', 'date', 'type', 'notes'] # moved to forms.py
    form_class = IncomeForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Income'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Income added successfully.')
        return reverse_lazy('myfinpages:income_list')


# @login_required
class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    # fields = ['value', 'date', 'type', 'notes'] # moved to forms.py
    form_class = IncomeForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Income'}
    # template_name_suffix = '_update_form'
    # queryset = Income.objects.all()

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully.')
        return reverse('myfinpages:income_detail', kwargs={'pk': self.object.pk})


# @login_required
class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = 'myfinpages/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Income'}
    # template_name_suffix = '_delete_form'
    # queryset = Income.objects.all()

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully.')
        return reverse_lazy('myfinpages:income_list')


class OutcomeListView(LoginRequiredMixin, ListView):
    model = Outcome
    paginate_by = 100
    template_name = 'myfinpages/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeDetailView(LoginRequiredMixin, DetailView):
    model = Outcome
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeCreateView(LoginRequiredMixin, CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Outcome'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Outcome added successfully.')
        return reverse_lazy('myfinpages:outcome_list')


class OutcomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome updated successfully.')
        return reverse('myfinpages:outcome_detail', kwargs={'pk': self.object.pk})


class OutcomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Outcome
    template_name = 'myfinpages/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome deleted successfully.')
        return reverse_lazy('myfinpages:outcome_list')


class BalanceListView(LoginRequiredMixin, ListView):
    model = Balance
    paginate_by = 100
    template_name = 'myfinpages/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceDetailView(LoginRequiredMixin, DetailView):
    model = Balance
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Balance'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceCreateView(LoginRequiredMixin, CreateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Add Balance'}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Balance added successfully.')
        return reverse_lazy('myfinpages:balance_list')


class BalanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = 'myfinpages/balance_income_outcome_form.html'
    extra_context = {'header': 'Update Balance'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance updated successfully.')
        return reverse('myfinpages:balance_detail', kwargs={'pk': self.object.pk})


class BalanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Balance
    template_name = 'myfinpages/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Balance'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance deleted successfully.')
        return reverse_lazy('myfinpages:balance_list')


# def current_finances(request):
#     last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
#     if not last_balance:
#         messages.warning(request, 'No current balance have been yet. Please add at least '
#                                   'one current balance entry.')
#         return render(request, 'myfinpages/current_finances.html')
#
#     today = date.today()
#     total_income = Income.objects\
#         .filter(user=request.user, date__gte=last_balance.date, date__lte=today)\
#         .aggregate(total=Sum('value'))['total']
#     total_income = 0 if total_income is None else total_income
#     total_outcome = Outcome.objects\
#         .filter(user=request.user, date__gte=last_balance.date, date__lte=today)\
#         .aggregate(total=Sum('value'))['total']
#     total_outcome = 0 if total_outcome is None else total_outcome
#     context = {
#         'last_balance': last_balance,
#         'estimated_balance': last_balance.value + total_income - total_outcome,
#         'total_income': total_income,
#         'total_outcome': total_outcome,
#     }
#
#     return render(request, 'myfinpages/current_finances.html', context=context)


# def current_finances(request):
#     last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
#     if not last_balance:
#         messages.warning(request, 'No current balance have been yet. Please add at least '
#                                   'one current balance entry.')
#     return render(request, 'myfinpages/current_finances.html')

@login_required(login_url='/accounts/login/')
def current_finances(request):
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    last_balance_savings = Balance.objects.filter(user=request.user, type=2).order_by('-date').first()
    if not last_balance:
        messages.warning(request, 'No current balance have been yet. Please add at least '
                                  'one current balance entry.')
        return render(request, 'myfinpages/current_finances.html')

    today = date.today()
    total_income = Income.objects \
        .filter(user=request.user, date__gte=last_balance.date, date__lte=today) \
        .aggregate(total=Sum('value'))['total']
    total_income = 0 if total_income is None else total_income
    total_outcome = Outcome.objects \
        .filter(user=request.user, date__gte=last_balance.date, date__lte=today) \
        .aggregate(total=Sum('value'))['total']
    total_outcome = 0 if total_outcome is None else total_outcome

    total_income_savings = Income.objects \
        .filter(user=request.user, date__gte=last_balance_savings.date, type=4, date__lte=today) \
        .aggregate(total=Sum('value'))['total']
    total_income_savings = 0 if total_income_savings is None else total_income_savings
    total_outcome_savings = Outcome.objects \
        .filter(user=request.user, date__gte=last_balance_savings.date, type=12, date__lte=today) \
        .aggregate(total=Sum('value'))['total']
    total_outcome_savings = 0 if total_outcome_savings is None else total_outcome_savings

    # return JsonResponse({
    #     'last_balance_value': last_balance.value,
    #     'last_balance_date': last_balance.date,
    #     'estimated_balance': last_balance.value + total_income - total_outcome,
    #     'total_income': total_income,
    #     'total_outcome': total_outcome,
    #     'last_balance_savings_value': last_balance_savings.value,
    #     'last_balance_savings_date': last_balance_savings.date,
    #     'estimated_balance_savings_value': last_balance_savings.value + total_income_savings - total_outcome_savings,
    #     'total_income_savings': total_income_savings,
    #     'total_outcome_savings': total_outcome_savings,
    # })
    context = {
        'last_balance_date': last_balance.date,
        'last_balance_value': last_balance.value,
        'estimated_balance': last_balance.value + total_income - total_outcome,
        'total_income': total_income,
        'total_outcome': total_outcome,
        'last_balance_savings_date': last_balance_savings.date,
        'last_balance_savings_value': last_balance_savings.value,
        'estimated_balance_savings': last_balance_savings.value + total_income_savings - total_outcome_savings,
        'total_income_savings': total_income_savings,
        'total_outcome_savings': total_outcome_savings,
    }

    return render(request, 'myfinpages/current_finances.html', context=context)


# def current_finances_by_type(request):
#     today = date.today()
#     last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
#     # last_balance_savings = Balance.objects.filter(user=request.user, type=2).order_by('-date').first()
#
#     if not last_balance:
#         return JsonResponse({'error': 'Please add at least one balance entry.'})
#
#     labels_income = []
#     data_income = []
#     labels_outcome = []
#     data_outcome = []
#
#     for income_type in Income.IncomeTypes.choices:
#         labels_income.append(income_type[1])
#         total_income = Income.objects \
#             .filter(user=request.user, date__gte=last_balance.date, type=income_type[0], date__lte=today) \
#             .aggregate(total=Sum('value'))['total']
#         total_income = 0 if total_income is None else total_income
#         data_income.append(total_income)
#
#     for outcome_type in Outcome.OutcomeTypes.choices:
#         labels_outcome.append(outcome_type[1])
#         total_outcome = Outcome.objects \
#             .filter(user=request.user, date__gte=last_balance.date, type=outcome_type[0], date__lte=today) \
#             .aggregate(total=Sum('value'))['total']
#         total_outcome = 0 if total_outcome is None else total_outcome
#         data_outcome.append(total_outcome)
#
#     # context = {
#     #     'last_balance': last_balance.value,
#     #     'estimated_balance': last_balance.value + total_income - total_outcome,
#     #     'total_income': total_income,
#     #     'total_outcome': total_outcome,
#     #     'last_balance_savings': last_balance_savings.value,
#     #     'estimated_balance_savings': last_balance_savings.value + total_income_savings - total_outcome_savings,
#     #     'total_income_savings': total_income_savings,
#     #     'total_outcome_savings': total_outcome_savings,
#     #     'labels': labels_income,
#     #     'data': data_income,
#     # }
#     #
#     # return render(request, 'myfinpages/current_finances.html', context=context)
#
#     return JsonResponse({
#         'labels_income': labels_income,
#         'data_income': data_income,
#         'labels_outcome': labels_outcome,
#         'data_outcome': data_outcome,
#     })
# #
#
#

def current_incomes_by_type(request):
    today = date.today()
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()

    if not last_balance:
        return JsonResponse({'error': 'Please add at least one balance entry.'})
    labels = []
    data = []

    for income_type in Income.IncomeTypes.choices:
        labels.append(income_type[1])
        total_income = Income.objects \
            .filter(user=request.user, date__gte=last_balance.date, type=income_type[0], date__lte=today) \
            .aggregate(total=Sum('value'))['total']
        total_income = 0 if total_income is None else total_income
        data.append(total_income)

    return JsonResponse({
        'labels': labels,
        'data': data,
    })


def current_outcomes_by_type(request):
    today = date.today()
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()

    if not last_balance:
        return JsonResponse({'error': 'Please add at least one balance entry.'})

    labels = []
    data = []

    for outcome_type in Outcome.OutcomeTypes.choices:
        labels.append(outcome_type[1])
        total_outcome = Outcome.objects \
            .filter(user=request.user, date__gte=last_balance.date, type=outcome_type[0], date__lte=today) \
            .aggregate(total=Sum('value'))['total']
        total_outcome = 0 if total_outcome is None else total_outcome
        data.append(total_outcome)

    return JsonResponse({
        'labels': labels,
        'data': data
    })
