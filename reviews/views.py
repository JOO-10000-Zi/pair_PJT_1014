from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewsForm
from .models import reviews

# Create your views here.
def index(request):
    name = reviews.objects.all()
    context = {
        'reviews' : name
    }
    
    return render(request, 'reviews/index.html', context)

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

def detail(request, pk):
    review = reviews.objects.get(pk=pk)
    context = {
        'reviews': review,
    }
    return render(request, 'reviews/detail.html', context)


@login_required
def update(request, pk):
    Reviews = reviews.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewsForm(request.POST, instance=Reviews)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', Reviews.pk)
    else:
        form = ReviewsForm(instance=Reviews)
    context = {
        'form': form
    }
    return render(request, 'reviews/update.html', context)
