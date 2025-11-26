from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .form import ProfileForm
# Create your views here.


class registerView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy('login')


def ProfileView(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        if profile:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        if profile:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()

    return render(request=request, template_name="accounts/profile.html", context={'form': form})
