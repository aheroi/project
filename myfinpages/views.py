from datetime import date
from django.db.models import Sum
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


from myfinpages.forms import IncomeForm, OutcomeForm, BalanceForm
from myfinpages.models import Income, Outcome, Balance
# Create your views here.


# @login_required
class IncomeListView(ListView):
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
class IncomeDetailView(DetailView):
    model = Income
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Income'}
    # queryset = Income.objects.all()

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'


# @login_required
class IncomeCreateView(CreateView):
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
class IncomeUpdateView(UpdateView):
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
class IncomeDeleteView(DeleteView):
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


class OutcomeListView(ListView):
    model = Outcome
    paginate_by = 100
    template_name = 'myfinpages/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeCreateView(CreateView):
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


class OutcomeUpdateView(UpdateView):
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


class OutcomeDeleteView(DeleteView):
    model = Outcome
    template_name = 'myfinpages/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome deleted successfully.')
        return reverse_lazy('myfinpages:outcome_list')


class BalanceListView(ListView):
    model = Balance
    paginate_by = 100
    template_name = 'myfinpages/balance_income_outcome_list.html'
    extra_context = {'list_what': 'Balance'}

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceDetailView(DetailView):
    model = Balance
    template_name = 'myfinpages/balance_income_outcome_detail.html'
    extra_context = {'detail_what': 'Balance'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Balance.objects.filter(user=user)


class BalanceCreateView(CreateView):
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


class BalanceUpdateView(UpdateView):
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


class BalanceDeleteView(DeleteView):
    model = Balance
    template_name = 'myfinpages/balance_income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Balance'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Balance.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Balance deleted successfully.')
        return reverse_lazy('myfinpages:balance_list')


def current_finances(request):
    last_balance = Balance.objects.filter(user=request.user, type=1).order_by('-date').first()
    if not last_balance:
        messages.warning(request, 'No current balance have been yet. Please add at least '
                                  'one current balance entry.')
        return render(request, 'myfinpages/current_finances.html')

    today = date.today()
    total_income = Income.objects\
        .filter(user=request.user, date__gte=last_balance.date, date__lte=today)\
        .aggregate(total=Sum('value'))['total']
    total_income = 0 if total_income is None else total_income
    total_outcome = Outcome.objects\
        .filter(user=request.user, date__gte=last_balance.date, date__lte=today)\
        .aggregate(total=Sum('value'))['total']
    total_outcome = 0 if total_outcome is None else total_outcome
    context = {
        'last_balance': last_balance,
        'estimated_balance': last_balance.value + total_income - total_outcome,
        'total_income': total_income,
        'total_outcome': total_outcome,
    }

    return render(request, 'myfinpages/current_finances.html', context=context)

def finance_history(request):
    return render(request, 'myfinpages/finance_history.html')
