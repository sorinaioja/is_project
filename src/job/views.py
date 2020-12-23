from django.shortcuts import render, get_object_or_404

from account.models import Company
from .forms import JobForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Job
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
            j_form = Job.objects.create(title=title, location=location,work_time=work_time,job_description=job_description, qualifications=qualifications, benefits=benefits,company=company)
            j_form.save()
            return redirect("home")
    else:
        j_form = JobForm()
    context = {
        'j_form': j_form
    }
    return render(request, "job/job_detail.html", context)


def present_job_view(request):
    context = {
        'jobs': Job.objects.all(),
        'Job': Job,
    }
    return render(request, 'job/view_jobs.html', context)


def delete_jobs(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    obj.delete();
    return redirect("home")
    return render(request, 'job/view_jobs.html')



