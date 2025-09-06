from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import get_recommended_careers

@login_required
def recommended_careers(request):
    careers = get_recommended_careers(request.user)
    return render(request, "recommendations/list.html", {"careers": careers})
