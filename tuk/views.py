from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'base.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile/profile.html')

@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form": form})
