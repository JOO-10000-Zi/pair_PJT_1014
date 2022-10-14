from django.shortcuts import render, redirect
from .forms import ReviewsForm
from .models import reviews

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

def create(request):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('reviews:index')
    else:
        form = ReviewsForm()
    context = {
        'form':form
    }
    return render(request, 'reviews/create.html', context)

# def create(request):

    # if request.user.is_authenticated:
    #     article_form = ReviewsForm(request.POST)
    #     if article_form.is_valid():
    #         article_form.save()
    #         return redirect('articles:index')
    #     else:
    #         article_form = ReviewsForm()
    #     context = {
    #         'article_form':article_form
    #     }
    #     return render(request, 'articles/create.html', context)
    # else:
    #     return redirect('accounts:login')
