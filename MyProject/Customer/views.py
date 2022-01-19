from django.shortcuts import render,redirect
from .models import Customer
from .forms import CustomerForm
from AddressApp.models import PermanentAddress
from customer_guarantor_app.models import Guarantor
from BankDetails.models import BankDetails
from LoanApplication.models import SanctionedLoan
from PrevLoan.models import PrevLoan
from ProfessionalDetails.models import ProfessionalDetails


def create_customer_view(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect("/dapp/address/cAddress/%i" % customer.id)
    template_name = 'DashboardApp/personaldetail.html'
    context = {'form':form}
    return render(request,template_name,context)

def show_customer_view(request):
    customer = Customer.objects.all()
    template_name = 'DashboardApp/showCustomer.html'
    context = {'customer':customer}
    return render(request,template_name,context)

def show_details_view(request,i):
    customer = Customer.objects.get(id=i)
    #guarantor = Guarantor.objects.get(customer=customer)
    paddress = PermanentAddress.objects.get(customer=customer)
    bankdetails = BankDetails.objects.get(customer=customer)
    #loansanction = SanctionedLoan.objects.get(customer=customer)
    prevloan = PrevLoan.objects.get(customer=customer)
   #profdetails =ProfessionalDetails.objects.get(customer=customer)
    #docu = customer.docu.all()
    template_name = 'DashboardApp/customerdetail.html'
    context = {'customer': customer,
                'prevloan':prevloan,
                'bankdetails': bankdetails,
               'paddress':paddress}

    return render(request, template_name, context)

