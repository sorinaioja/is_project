from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods

from account.models import Company
from .forms import JobForm, JobFormApplication
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job, JobApplication


# Create your views here.


def job_create_view(request):
    if request.POST:

        j_form = JobForm(request.POST)

        if j_form.is_valid():
            title = request.POST.get('title')
            location = request.POST.get('location')
            work_time = request.POST.get('work_time')
            job_description = request.POST.get('job_description')
            qualifications = request.POST.get('qualifications')
            benefits = request.POST.get('benefits')
            company = request.user.company
            j_form.save(commit=False)
            j_form = Job.objects.create(title=title, location=location, work_time=work_time,
                                        job_description=job_description, qualifications=qualifications,
                                        benefits=benefits, company=company)
            j_form.save()
            return redirect("home")
    else:
        j_form = JobForm()
    context = {
        'j_form': j_form
    }
    return render(request, "job/job_detail.html", context)


def job_application_view(request, pk):

    if request.POST:

        j_form = JobFormApplication(request.POST, request.FILES)

        if j_form.is_valid():

            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            start_date = request.POST.get('start_date')
            display_CV = request.FILES['display_CV']
            print(display_CV.name)
            print(display_CV.size)
            job = get_object_or_404(Job, pk=pk)
            company = job.company
            print(job.title)
            fs = FileSystemStorage()
            fs.save(display_CV.name, display_CV)
            j_form.save(commit=False)
            j_form = JobApplication.objects.create(name=name, email=email, phone_number=phone_number, start_date=start_date, display_CV=display_CV, company=company, job=job)
            j_form.save()
            return redirect("home")
    else:
        j_form = JobForm()

    context = {
        'j_form': j_form,
        'jobpk': get_object_or_404(Job, pk=pk),

    }
    return render(request, "job/job_application.html", context)


def present_job_view(request):
    context = {
        'jobs': Job.objects.all(),
        'Job': Job,

    }
    return render(request, 'job/view_jobs.html', context)


def user_job_view(request):
    context = {
        'jobs': Job.objects.all(),
        'Job': Job,
    }
    return render(request, 'job/user_view_jobs.html', context)


def delete_jobs(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    obj.delete()
    return redirect("home")
    return render(request, 'job/view_jobs.html')


@require_http_methods(['GET'])
def search(request):
    q = request.GET.get('q')
    if q:
        jobs = Job.objects.filter(location=q)
        return render(request, 'job/job_filterr.html', {'jobs':jobs, 'query':q})
    return HttpResponse('Please submit a search term.')