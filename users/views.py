from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreateForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('booking:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super().form_valid(form)
