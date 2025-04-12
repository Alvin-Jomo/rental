from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.models import Profile, User
from django.views.decorators.csrf import csrf_protect
from houses.models import Booking, PaymentRecord, invoice
from django.contrib.auth.decorators import login_required


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey, you are already logged in.")
        return redirect("houses:home")

    # Check if the user was redirected to login due to @login_required
    if request.GET.get('next'):
        messages.warning(request, "You must be logged in to access that page.")

    if request.method == "POST":
        login_id = request.POST.get("login_id")  # Accepts either phone or username
        password = request.POST.get("password")

        try:
            user = User.objects.get(phone=login_id) if login_id.isdigit() else User.objects.get(username=login_id)
        except User.DoesNotExist:
            messages.warning(request, f"User with {login_id} does not exist")
            return redirect("userauths:sign-in")

        user = authenticate(request, phone=user.phone, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("houses:home")
        else:
            messages.warning(request, "Invalid phone/username or password.")

    return render(request, "userauths/sign-in.html")

@csrf_protect
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully.")
            new_user = authenticate(phone=form.cleaned_data['phone'], password=form.cleaned_data['password1'])
            if new_user:
                login(request, new_user)
                return redirect("houses:home")
    else:
        form = UserRegisterForm()

    return render(request, "userauths/sign-up.html", {"form": form})




def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("userauths:sign-in")


@login_required(login_url='userauths:sign-in')  # Redirect to the login page if not logged in
def profile_update(request):
    profile = Profile.objects.get(user=request.user)

    # Fetch booking history, payment history, and invoices for the logged-in user
    bookings = Booking.objects.filter(user=request.user)
    payment_records = PaymentRecord.objects.filter(name=request.user.username)  # Assuming 'name' matches the username
    invoices = invoice.objects.filter(booking__user=request.user)  # Filter invoices by booking user

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Profile Updated Successfully.")
            return redirect("houses:home")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
        "bookings": bookings,
        "payment_records": payment_records,
        "invoices": invoices,
    }
    return render(request, "userauths/profile-edit.html", context)