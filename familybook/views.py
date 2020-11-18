from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.db.models.functions import Lower
import os
from myextendedfamily import settings

from .models import Entry, Profile
from django.contrib.auth.models import User
def json_func(request):
    if request.META['HTTP_ACCEPT'] == 'application/json':
        json_context = []
        for entry in Entry.objects.filter(user = request.user).order_by(Lower('last_name'), Lower('first_name')):
            json_context.append({
                "profile_pic": entry.profile_pic.url,
                "address": entry.get_address()+f", {entry.country}",
                })
        return JsonResponse(json_context, safe=False)
    raise Http404

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('entry-list'))
    else:
        return render(request, 'familybook/intro.html')

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user).order_by(Lower('last_name'), Lower('first_name'))

@login_required
def entry_detail_view(request, id):
    entry = get_object_or_404(Entry, pk=id)
    if entry.user == request.user:
        return render(request, 'familybook/entry_detail.html', {'entry': entry})
    raise Http404

@login_required
def profile_detail_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'familybook/profile_detail.html', {'profile': profile})

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['profile_pic', 'first_name', 'last_name', 'email', 'street_address', 'city', 'state', 'zip_code', 'country', 'phone_number']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     print(form.errors)
    #     return super().form_invalid(form)

class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['profile_pic', 'first_name', 'last_name', 'email', 'street_address', 'city', 'state', 'zip_code', 'country', 'phone_number']


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['profile_pic', 'first_name', 'last_name', 'email', 'street_address', 'city', 'state', 'zip_code', 'country', 'phone_number']
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        count = Profile.objects.filter(user=self.request.user).count()
        if count == 1:
            raise Http404
        return super().dispatch(request)
    # def form_invalid(self, form):
    #     print(form.errors)
    #     return super().form_invalid(form)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['profile_pic', 'first_name', 'last_name', 'email', 'street_address', 'city', 'state', 'zip_code', 'country', 'phone_number']
    template_name_suffix = '_update'
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

def register(request):
    if request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return redirect('profile-create')
    else:
        form = UserCreationForm()
    
    return render(request, 'familybook/register.html', {'form': form})