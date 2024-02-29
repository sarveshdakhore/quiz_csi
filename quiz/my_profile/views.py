from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz_creator.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Questions
import json

@login_required
def profile_view(request):
    user = request.user
    data=  Quiz.objects.filter(user=user)
    return render(request, 'my_profile/profile.html',{"data":data})

@login_required
def quiz_detail(request,quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    try:
        q = Questions.objects.filter(quiz=quiz).first().textbox
        print(q)
        return render(request, 'my_profile/quiz_detail.html',{"quiz":quiz,'q':q})
    
    except:
        q = None
    return render(request, 'my_profile/quiz_detail.html',{"quiz":quiz,'q':q})




@login_required
@csrf_exempt
def saveq(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    data = json.loads(request.body)
    if data is not None:
        Questions.objects.update_or_create(quiz=quiz, defaults={'textbox': data})
        return JsonResponse({"status": "success", 'questions': Questions.objects.filter(quiz=quiz).first().textbox})
    else:
        return JsonResponse({"status": "error", "message": "No data provided"})