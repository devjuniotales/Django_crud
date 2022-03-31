from django.views.generic import ListView , CreateView, UpdateView ,DetailView, DeleteView
from django.urls import reverse_lazy

from crud.models import User
# Create your views here.

class UserList(ListView):
    model = User
    queryset = User.objects.all()

class CreateUser(CreateView):
    model = User
    fields = ['name','email']
    success_url = reverse_lazy('list') 

class UserUpdate(UpdateView):
    model = User
    fields = ['name','email']
    success_url = reverse_lazy('list')   


class UserDetail(DetailView):
    queryset = User.objects.all()
 
class UserDelete(DeleteView):
    queryset = User.objects.all()
    success_url = reverse_lazy('list')    
