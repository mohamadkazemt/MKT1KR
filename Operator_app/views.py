from django.shortcuts import render, get_object_or_404, redirect
from .models import Operator, Failure, Load
from .forms import OperatorForm

def operator_list(request):
    operators = Operator.objects.all()
    return render(request, 'operator_list.html', {'operators': operators})

def operator_detail(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    failures = operator.failures.all().order_by('-timestamp')
    loads = operator.loads.all().order_by('-timestamp')
    return render(request, 'operator_detail.html', {'operator': operator, 'failures': failures, 'loads': loads})

def operator_create(request):
    if request.method == "POST":
        form = OperatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm()
    return render(request, 'operator_form.html', {'form': form})

def operator_update(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == "POST":
        form = OperatorForm(request.POST, request.FILES, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm(instance=operator)
    return render(request, 'operator_form.html', {'form': form})

def operator_delete(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == "POST":
        operator.delete()
        return redirect('operator_list')
    return render(request, 'operator_confirm_delete.html', {'operator': operator})
