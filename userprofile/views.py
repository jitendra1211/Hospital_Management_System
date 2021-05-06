from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from account.models import User
from appointment.models import Payment
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# @login_required(login_url='/login/')
def create_user_profile(request):
    button_type = 'Create'
    title = 'Create Patient'
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        payment_form = UserPaymentForm(request.POST)
        if form.is_valid() and payment_form.is_valid():
            profile = form.save(commit=False)
            password = User.objects.make_random_password()
            username = profile.name.split()[0] + id_generator()
            user = User.objects.create(username=username, usertype='P')
            user.set_password(password)
            profile.user = user
            user.email = profile.email
            user.save()
            profile.save()
            payment = payment_form.save(commit=False)
            payment.user = user
            payment.total = payment.paid + payment.outstanding
            payment.save()
            return redirect('r_dashboard')

    else:
        form = UserProfileForm()
        payment_form = UserPaymentForm()
    context = {
        'form': form,
        'payment_form': payment_form,
        'title': title,
        'button_type': button_type
    }
    return render(request, 'userprofile/userprofile.html', context)


def user_profile(request):
    button_type = 'Update'

    user = request.user
    title = 'Hi, ' + user.first_name + ' ' + user.last_name
    profile = UserProfile.objects.get(user=user)
    payment = Payment.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        payment_form = UserPaymentForm(request.POST, instance=payment)
        if form.is_valid() and payment_form.is_valid():
            form.save()
            payment_form.save()
            return redirect('/')

    else:
        form = UserProfileForm(instance=profile)
        payment_form = UserPaymentForm(instance=payment)
    context = {
        'form': form,
        'payment_form': payment_form,
        'title': title,
        'button_type': button_type
    }
    return render(request, 'userprofile/userprofile.html', context)


def update_user_profile_pk(request, pk):
    button_type = 'Update Patient'
    print(pk)
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    title = user.first_name + ' ' + user.last_name
    payment = Payment.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        payment_form = UserPaymentForm(request.POST, instance=payment)
        if form.is_valid() and payment_form.is_valid():
            form.save()
            payment_form.save()
            return redirect('r_dashboard')

    else:
        form = UserProfileForm(instance=profile)
        payment_form = UserPaymentForm(instance=payment)
    print(profile, payment)
    context = {
        'form': form,
        'payment_form': payment_form,
        'title': title,
        'button_type': button_type
    }
    return render(request, 'userprofile/userprofile.html', context)


def delete_user_profile_pk(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()

    return redirect('r_dashboard')

    # else:
    #     context = {
    #         'user': user,
    #     }
    #     return render(request, 'userprofile/userprofile_delete.html', context)


def doc_profile_view(request):
    button_type = 'Update'
    user = request.user
    title = 'Hi, ' + user.first_name + ' ' + user.last_name
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UserProfileForm(instance=profile)
    context = {
        'form': form,
        'title': title,
        'button_type': button_type
    }
    return render(request, 'userprofile/doc_profile.html', context)


def doc_profile_pk(request, pk):
    button_type = 'Update Doctor'
    user = User.objects.get(pk=pk)
    title = user.first_name + ' ' + user.last_name
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = DocProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')

    else:
        form = DocProfileForm(instance=profile)
    context = {
        'form': form,
        'title': title,
        'button_type': button_type
    }
    return render(request, 'userprofile/doc_profile.html', context)


def delete_doc_profile_pk(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user.delete()

    return redirect('hr_dashboard')

