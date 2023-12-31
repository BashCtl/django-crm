from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .froms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.warning(request, "There Was An Error Logging In, PLease Try Again.")
            return redirect('home')
    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out.")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered.")
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        user_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'user_record': user_record})
    else:
        messages.warning(request, "You Myst Be Logged In To View That Page.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        record_to_delete = Record.objects.get(id=pk)
        record_to_delete.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect('home')
    else:
        messages.warning(request, "You Must Be Logged In.")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save()
                messages.success(request, "Customer Record Added.")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.warning(request, "You Must Be Logged In.")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Record Has Been Updated.")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.warning(request, "You Must Be Logged In.")
        return redirect('home')