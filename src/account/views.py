from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserChangeForm
from datetime import date

from .forms import RegistrationForm, RegistrationFormApplicant, RegistrationFormCompany, AccountAuthenticationForm, UserUpdateForm, CompanyUpdateForm, ApplicantUpdateForm, CommentForm

from account.models import Account, Company, Applicant, Comment
from job.models import Job

from django.shortcuts import render, get_object_or_404


def register_view_Applicant(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    if request.POST:
        form = RegistrationForm(request.POST)
        applicant_form = RegistrationFormApplicant(request.POST)
        if form.is_valid() and applicant_form.is_valid():
            user = form.save()
            applicant = applicant_form.save(commit=False)
            user.refresh_from_db()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user.is_applicant = True
            user.save()
            applicant.user = user
            applicant.save()
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            # destination = kwargs.get("next")
            # if destination:
            #     return redirect(destination)
            return redirect('home')
        else:
            form = RegistrationForm()
            applicant_form = RegistrationFormApplicant()


    else:
        form = RegistrationForm()
        applicant_form = RegistrationFormApplicant()
    return render(
        request,
        'account/register_account.html',
        {'form': form, 'applicant_form': applicant_form}
    )


def register_view_Company(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated as " + str(user.email))

    if request.POST:
        form = RegistrationForm(request.POST)
        company_form = RegistrationFormCompany(request.POST)
        if form.is_valid() and company_form.is_valid():
            user = form.save()
            company = company_form.save(commit=False)
            user.refresh_from_db()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user.is_company = True
            user.save()
            company.user = user
            company.save()
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            # destination = kwargs.get("next")
            # if destination:
            #     return redirect(destination)
            return redirect('home')
        else:
            form = RegistrationForm()
            company_form = RegistrationFormCompany()
            return render(
                request,
                'account/register_company.html',
                {'form': form, 'company_form': company_form}
            )


    else:
        form = RegistrationForm()
        company_form = RegistrationFormCompany()
    return render(
        request,
        'account/register_company.html',
        {'form': form, 'company_form': company_form}
    )


def register_view(request):
    context = {}
    return render(request, "account/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


# def company_view(request):
# 	context = {
# 		'companies': Company.objects.all(),
# 	}
# 	return render(request,'account/companies.html', context)

def account_view(request, *args, **kwargs):
    context = {}
    user_id = kwargs.get("user_id")
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return HttpResponse("Something went wrong.")
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['profile_image'] = account.profile_image.url
        context['hide_email'] = account.hide_email

        return render(request, "account/account.html", context)


def userprofile_view(request):
    context = {}
    return render(request, "account/userprofile.html", context)


def edit_user_profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            new_username = user_form.cleaned_data['username']
            return redirect("userprofile")
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        'user_form': user_form
    }
    return render(request, 'account/update_user.html', context)


def companyprofile_view(request):
    context = {}
    return render(request, "account/compprofile.html", context)


def present_companies_view(request):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'account/present_companies.html', context)


@login_required
def company_profile_update(request):
    if request.method == 'POST':

        c_form = CompanyUpdateForm(request.POST, instance=request.user.company)
        if c_form.is_valid():
            c_form.save()
            return redirect("home")
    else:
        c_form = CompanyUpdateForm(instance=request.user.company)

    context = {
        'c_form': c_form
    }

    return render(request, 'account/update_company.html', context)


def user_profile_update(request):
    if request.method == 'POST':

        c_form = ApplicantUpdateForm(request.POST, instance=request.user.applicant)
        if c_form.is_valid():
            c_form.save()
            return redirect("home")
    else:
        c_form = CompanyUpdateForm(instance=request.user.applicant)

    context = {
        'c_form': c_form
    }

    return render(request, 'account/update_user.html', context)


def one_company_detail(request,pk):
    comp = get_object_or_404(Company, pk=pk)
    print("intra")
    comment_form = CommentForm(request.POST)
    if request.POST:
        if comment_form.is_valid():
            name = request.POST.get('name')
            body = request.POST.get('body')
            date_added = date.today()
            print("intra")
            comment_form.save(commit=False)
            comment_form = Comment.objects.create(company=comp, name=name, body=body, date_added=date_added)
            comment_form.save()
    context = {
        'comment_form': comment_form,
        'company': comp
    }
    return render(request, 'account/company_detail.html', context)



