from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
# from django.contrib.auth.decorators import login_required       # for login_required

from myfinpages.forms import IncomeForm
from myfinpages.models import Income
# Create your views here.


# @login_required
class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    # template_name = 'myfinpages/income_list.html'
    # queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income_list'
    # extra_context = {'smth add':'Hello', 'smth add2': 'What is?'}
    # allow_empty = True


# @login_required
class IncomeDetailView(DetailView):
    model = Income
    # template_name = 'myfinpages/income_list.html'
    # queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)
    # context_object_name = 'income'
    # extra_context = {'smth add': 'Hello', 'smth add2': 'What is?'}


# @login_required
class IncomeCreateView(CreateView):
    model = Income
    # fields = ['value', 'date', 'type', 'notes'] # moved to forms.py
    form_class = IncomeForm

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
    # template_name = 'myfinpages/income_form.html'
    # template_name_suffix = '_update_form'
    # queryset = Income.objects.all()
    # context_object_name = 'income'
    # extra_context = {'smth add': 'Hello', 'smth add2': 'What is?'}
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully.')
        return reverse('myfinpages:income_detail', kwargs={'pk': self.object.pk})


# @login_required
class IncomeDeleteView(DeleteView):
    model = Income
    # template_name = 'myfinpages/income_confirm_delete.html'
    # template_name_suffix = '_delete_form'
    # queryset = Income.objects.all()
    # context_object_name = 'income'
    # extra_context = {'smth add': 'Hello', 'smth add2': 'What is?'}
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully.')
        return reverse_lazy('myfinpages:income_list')
