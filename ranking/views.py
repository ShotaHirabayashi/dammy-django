from django.shortcuts import render
from django.views.generic import TemplateView ,ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import barRank , BarRankCSV
import csv
from io import TextIOWrapper, StringIO
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class barRankListView(LoginRequiredMixin,ListView):
    model = BarRankCSV
    template_name = "list.html"
    paginate_by = 5
    login_url = '/login/'
    

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            #csvの読み込みとしてBarRankCSV()が必要
            barRankCSV = BarRankCSV()
            barRankCSV.title = line[0]
            barRankCSV.kanaTitle = line[1]
            barRankCSV.address = line[2]
            barRankCSV.promotion = line[3]
            barRankCSV.save()
    return render(request, 'upload.html')



def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('/list/')
        else:
            return redirect('/login/')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('barRankCsv:login')