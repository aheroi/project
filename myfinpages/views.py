from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from myfinpages.forms import IncomeForm
from myfinpages.models import Income
# Create your views here.


class IncomeListView(ListView):
    model = Income
    paginate_by = 100
    # template_name = 'myfinpages/income_list.html'
    # queryset = Income.objects.all()
    # context_object_name = 'income_list'
    # extra_context = {'smth add':'Hello', 'smth add2': 'What is?'}
    # allow_empty = True


class IncomeDetailView(DetailView):
    model = Income
    # template_name = 'myfinpages/income_list.html'
    # queryset = Income.objects.all()
    # context_object_name = 'income'
    # extra_context = {'smth add': 'Hello', 'smth add2': 'What is?'}


class IncomeCreateView(CreateView):
    model = Income
    # fields = ['value', 'date', 'type', 'notes'] # moved to forms.py
    form_class = IncomeForm
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income added successfully.')
        return reverse('myfinpages:income_list', kwargs={'pk': self.object.pk})


class IncomeUpdateView(UpdateView):
    model = Income
    # fields = ['value', 'date', 'type', 'notes'] # moved to forms.py
    form_class = IncomeForm
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income updated successfully.')
        return reverse('myfinpages:income_detail', kwargs={'pk': self.object.pk})


class IncomeDeleteView(DeleteView):
    model = Income
    # success_url = reverse_lazy('myfinpages:income_list')

    def get_success_url(self):
        messages.success(self.request, 'Income deleted successfully.')
        return reverse_lazy('myfinpages:income_list')
