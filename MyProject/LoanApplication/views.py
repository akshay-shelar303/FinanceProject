from django.shortcuts import render, redirect
from .models import SanctionedLoan
from .forms import SanctionedLoanModelForm


def home_view(request):
    return render(request, template_name="index.html")


def create_sanctionedoan_view(request):
    form = SanctionedLoanModelForm()
    if request.method == "POST":
        form = SanctionedLoanModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_sanction")
    template_name = "DashboardApp/sanctioned_loan.html"
    context = {"form": form}
    return render(request, template_name, context)


def show_sanctionedoan_view(request):
    sanction_obj = SanctionedLoan.objects.all()
    template_name = "DashboardApp/show_sanctioned_loan.html"
    context = {"sanction_obj": sanction_obj}
    return render(request, template_name, context)


def update_sanctionedoan_view(request, i):
    sanction_obj = SanctionedLoan.objects.get(id=i)
    print(sanction_obj)
    form = SanctionedLoanModelForm(instance=sanction_obj)
    if request.method == "POST":
        form = SanctionedLoanModelForm(request.POST, instance=sanction_obj)
        if form.is_valid():
            form.save()
            return redirect("show_sanction")
    template_name = "DashboardApp/sanctioned_loan.html"
    context = {"form": form}
    return render(request, template_name, context)
