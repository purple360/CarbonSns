from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileDetailsForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Save the user object but don't log them in yet
        user = form.save(commit=False)
        user.save()  # Save the user to generate a primary key (pk)

        # Log in the user
        login(self.request, user)

        # Redirect the user to the profile and details page
        return redirect('profile_details', pk=user.pk)
@login_required
def profile_details(request, pk):
    user = request.user  # Get the currently logged-in user

    # Check if the user has a profile
    if hasattr(user, 'profile'):
        profile = user.profile
    else:
        profile = None

    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ProfileDetailsForm(instance=profile)

    return render(request, 'registration/profile_details.html', {'form': form})
