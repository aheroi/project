from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# from django.contrib.auth.decorators import login_required       # for login_required

from myfinpages.forms import IncomeForm, OutcomeForm
from myfinpages.models import Income, Outcome, Balance
# Create your views here.


# @login_required
class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    template_name = 'myfinpages/income_outcome_list.html'
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
    template_name = 'myfinpages/income_outcome_detail.html'
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
    template_name = 'myfinpages/income_outcome_form.html'
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
    template_name = 'myfinpages/income_outcome_form.html'
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
    template_name = 'myfinpages/income_outcome_confirm_delete.html'
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
    template_name = 'myfinpages/income_outcome_list.html'
    extra_context = {'list_what': 'Outcome'}

    def get_queryset(self):
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeDetailView(DetailView):
    model = Outcome
    template_name = 'myfinpages/income_outcome_detail.html'
    extra_context = {'detail_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)


class OutcomeCreateView(CreateView):
    model = Outcome
    form_class = OutcomeForm
    template_name = 'myfinpages/income_outcome_form.html'
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
    template_name = 'myfinpages/income_outcome_form.html'
    extra_context = {'header': 'Update Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome updated successfully.')
        return reverse('myfinpages:outcome_detail', kwargs={'pk': self.object.pk})



class OutcomeDeleteView(DeleteView):
    model = Outcome
    template_name = 'myfinpages/income_outcome_confirm_delete.html'
    extra_context = {'delete_what': 'Outcome'}

    def get_queryset(self):         # to view only your entries
        user = self.request.user
        return Outcome.objects.filter(user=user)

    def get_success_url(self):
        messages.success(self.request, 'Outcome deleted successfully.')
        return reverse_lazy('myfinpages:outcome_list')
