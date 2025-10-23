from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile
from .tasks import send_email
from .forms.create_user_profile_form import UserProfileForm
from django.templatetags.static import static



# Create your views here.
def create_user_profile(request):
    title = "Create User Profile"
    context = {
        'title': title,
        "style_css": static("css/globals.css"),
    }
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save()
            # Trigger the asynchronous email sending task
            send_email.delay(user_profile.pk)
            # redirect to a form success page or render a success message
            return render(request, 'academic/success.html', context)
    else:
        context['heading'] = "Create a New User Profile"
        form = UserProfileForm()
        context["form"] = form
    return render(request, 'academic/create_user_profile.html', context)
