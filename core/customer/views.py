from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
  return render(request, 'customer/base.html')
  