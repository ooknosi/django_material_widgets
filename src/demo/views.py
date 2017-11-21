"""
DJANGO MATERIAL COMPONENTS DEMO VIEWS
demo/views.py
"""
# pylint: disable=too-many-ancestors

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import DemoForm, DemoModelForm

class IndexView(FormView):
    """Form view of index.html."""
    template_name = 'demo/index.html'
    form_class = DemoForm
    success_url = reverse_lazy('demo:index')

    def post(self, request, *args, **kwargs):
        form = DemoForm(request.POST)
        return render(request, 'demo/index.html', {'form': form})


class DemoModelFormView(FormView):
    """Form view of modelform.html."""
    template_name = 'demo/modelform.html'
    form_class = DemoModelForm
    success_url = reverse_lazy('demo:modelform')

    def post(self, request, *args, **kwargs):
        form = DemoModelForm(request.POST)
        return render(request, 'demo/modelform.html', {'form': form})
