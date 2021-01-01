from django.shortcuts import render, get_object_or_404

from account.models import Applicant
from .forms import ForumForm, DiscussionForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Forum, Discussion
# Create your views here.


def add_in_forum(request):
    if request.POST:

        f_form = ForumForm(request.POST)

        if f_form.is_valid():

            topic = request.POST.get('topic')
            description = request.POST.get('description')
            link = request.POST.get('link')
            applicant = request.user.applicant
            f_form.save(commit=False)
            f_form = Forum.objects.create(topic=topic, description=description,link=link,applicant=applicant)
            f_form.save()
            return redirect("home")
    else:
        f_form = ForumForm()
    context = {
        'f_form': f_form
    }
    return render(request, "forum/addInForum.html", context)

def present_forum_view(request):
    context = {
        'forums': Forum.objects.all(),
        'Forum': Forum,
    }
    return render(request, 'forum/viewDiscussions.html', context)









