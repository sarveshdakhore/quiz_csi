from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Quiz
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect




@csrf_exempt
def check_quiz_name(request):
    if request.method == 'POST':
        user = request.user
        quiz_name = request.POST.get('quiz_name').strip()
        active = request.POST.get('active') == 'true'
        from_date = None
        to_date = None
        quiz_exists = Quiz.objects.filter(user=user,name=quiz_name).exists()
        if quiz_exists or quiz_name == '':
            data = {'status': 'Fail', 'message': 'Quiz with this name already exists'}
            return JsonResponse(data)
        
        if not active:
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            quiz = Quiz.objects.create(
            user=user,
            name=quiz_name,
            is_active=active,
            from_time=from_date,
            to_time=to_date
        )
            if not quiz:
                data = {'status': 'Fail', 'message': 'Some Error Occured while creating quiz'}
                return JsonResponse(data)
        else:
            quiz = Quiz.objects.create(
            user=user,
            name=quiz_name,
            is_active=active
            )
            if not quiz:
                data = {'status': 'Fail', 'message': 'Some Error Occured while creating quiz'}
                return JsonResponse(data)
    data = {'status': 'success'}
    return JsonResponse(data)




@login_required
def create_quiz(request):
    return render(request, 'quiz_creator/create_quiz.html')




