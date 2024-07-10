from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Operator
from .forms import OperatorForm

def operator_list(request):
    operators = Operator.objects.all()
    form = OperatorForm()
    return render(request, 'operator_list.html', {'operators': operators, 'form': form})

def operator_create(request):
    if request.method == "POST":
        form = OperatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    return redirect('operator_list')

def operator_update(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == "POST":
        form = OperatorForm(request.POST, request.FILES, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    return redirect('operator_list')

def operator_delete(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == "POST":
        operator.delete()
        return redirect('operator_list')
    return redirect('operator_list')

def operator_detail(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    return render(request, 'operator_detail.html', {'operator': operator})
