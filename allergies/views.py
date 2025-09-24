from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from .models import Allergy
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



CustomUser= get_user_model()

# Create your views here.
@csrf_exempt
def allergies(request, user_id):
   user = get_object_or_404(CustomUser, id=user_id)
   queryset = user.allergies.all()

   # if request.method == 'POST':
   #    data = request.POST
   #    allergyname = data.get('allergyname')
   #    test_level = data.get('test_level')
   #    category = data.get('category')

   #    new_allergy = Allergy.objects.create(
   #    allergyname=allergyname,
   #    test_level=test_level,
   #    category=category,
   #  )
   #    user.allergies.add(new_allergy)

   #    return redirect('user_details', user_id=user.id)
   if request.method == 'POST':
    try:
        data = json.loads(request.body)
        allergyname = data.get('allergyname')
        test_level = data.get('test_level')


        new_allergy = Allergy.objects.create(
            allergyname=allergyname,
            test_level=float(test_level),

        )
        user.allergies.add(new_allergy)

        # Safely get severity info
        severity = getattr(new_allergy, 'severity', '')
        badge_class = getattr(new_allergy, 'severity_badge_class', '')
        if callable(badge_class):
            badge_class = badge_class()

        response_data = {
            'status': 'created',
            'allergy_id': new_allergy.id,
            'allergyname': new_allergy.allergyname,
            'test_level': new_allergy.test_level,
            'severity': new_allergy.get_severity_display() if hasattr(new_allergy, 'get_severity_display') else '',
            'severity_badge_class': new_allergy.severity_badge_class() if callable(new_allergy.severity_badge_class) else '',
        }
        return JsonResponse(response_data, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@csrf_exempt
def delete_allergy(request, pk):
    if request.method == 'DELETE':
        try:
            allergy = Allergy.objects.get(pk=pk)
            allergy.delete()
            return JsonResponse({'success': True})
        except Allergy.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Allergy not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


def update_allergy(request, id):
   allergy = get_object_or_404(Allergy, id=id)

   user = allergy.customuser_set.first() 

   if request.method == 'POST':
      data = request.POST
      allergyname = data.get('allergyname')
      test_level = data.get('test_level')
      category = data.get('category')

      allergy.allergyname = allergyname
      allergy.test_level = test_level
      allergy.category = category
      allergy.save()
      context = {'allergy': allergy}
      return redirect('user_details', user_id=user.id)
   
   allergies = user.allergies.all()
   return render(request, 'user_details.html', {'myuser': user, 'allergies': allergies, 'selected_allergy': allergy})


def details(request, id):
    allergy = get_object_or_404(Allergy, id=id)
    
    if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
        return JsonResponse({
            'id': allergy.id,
            'allergyname': allergy.allergyname,
            'test_level': allergy.test_level,
        })
    
    return render(request, 'details.html', {'myallergy': allergy})

def main(request):
    if not request.user.is_authenticated:
        return redirect('login')  # or your login page
    context = {'myuser': request.user}
    return render(request, 'user_details.html', context)
