from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse

# email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .forms import NewUserForm


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string(
        "application/activate_acct_template.html",
        {
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
    )
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        msg = (
            f"Dear {user}, please go to your inbox at {to_email} and click on "
            f"the activation link to confirm and complete the registration. "
            f"Note: Check your spam folder"
        )
        messages.success(request, msg)
    else:
        msg = (
            f"Problem sending confirmation email to {to_email}, "
            f"check if you typed it correctly."
        )
        messages.error(request, msg)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return redirect("account:login")
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect("home")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get("email"))
            return redirect("account:login")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = NewUserForm()

    context = {}
    context["form"] = form
    context["loginUrl"] = reverse("account:login")
    return render(
        request=request, template_name="registration/register.html", context=context
    )


def login_view(request):
    form = AuthenticationForm()
    context = {"form": form}
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("application:profile"))
            else:
                return render(request, "registration/login.html", context)
        else:
            return render(request, "registration/login.html", context)
    else:
        return render(request, "registration/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")
