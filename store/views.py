from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'store/home.html')

def products(request):
    return render(request, 'store/products.html')

def analytics(request):
    return render(request, 'store/analytics.html')
def settings_page(request):
    return render(request, 'store/settings.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'store/signup.html', {'form': form})




def python_roadmap(request):
    return render(request, 'store/roadmaps/python.html')

def java_roadmap(request):
    return render(request, 'store/roadmaps/java.html')

def c_roadmap(request):
    return render(request, 'store/roadmaps/c.html')

def cpp_roadmap(request):
    return render(request, 'store/roadmaps/cpp.html')

def react_roadmap(request):
    return render(request, 'store/roadmaps/react.html')

def sql_roadmap(request):
    return render(request, 'store/roadmaps/sql.html')

def r_roadmap(request):
    return render(request, 'store/roadmaps/r.html')

def web_roadmap(request):
    return render(request, 'store/roadmaps/web.html')

from django.contrib.auth.decorators import login_required
from .models import RoadmapStep, UserProgress

@login_required
def course_learn(request, course_id):
    steps = RoadmapStep.objects.filter(course_id=course_id).order_by('order')

    completed_steps = UserProgress.objects.filter(
        user=request.user,
        completed=True
    ).values_list('step_id', flat=True)

    # Find first incomplete step
    current_step = None
    for step in steps:
        if step.id not in completed_steps:
            current_step = step
            break

    return render(request, 'store/learn.html', {
        'step': current_step
    })

@login_required
def complete_step(request, step_id):
    step = RoadmapStep.objects.get(id=step_id)

    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        step=step
    )
    progress.completed = True
    progress.save()

    return redirect('course_learn', course_id=step.course.id)
