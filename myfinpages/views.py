from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from myfinpages.models import Income
# Create your views here.


class IncomeListView(ListView):
    model = Income
    paginate_by = 100


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    fields = ['value', 'date', 'type', 'notes']
    success_url = reverse_lazy('myfinpages:income_list')


class IncomeUpdateView(UpdateView):
    model = Income
    fields = ['value', 'date', 'type', 'notes']
    success_url = reverse_lazy('myfinpages:income_list')


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = reverse_lazy('myfinpages:income_list')
