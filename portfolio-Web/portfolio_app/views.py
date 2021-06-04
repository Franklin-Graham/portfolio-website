from django.shortcuts import render
from . models import My_details,Project,Account
# Create your views here.
def fun1(request):
    details = My_details.objects.all()
    project = Project.objects.all()
    account = Account.objects.all()
    return render(request,'index.html',{'obj_1':details,'obj_2':project,'obj_3':account})