from django.shortcuts import render, redirect
from .models import DietaryPreference
from django.db.models import Count, Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Capture the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        diet = request.POST.get('diet')
        diseases = request.POST.get('diseases', '')
        allergies = request.POST.get('allergies', '')

        # Create a new DietaryPreference object and save it
        dietary_preference = DietaryPreference(
            name=name,
            email=email,
            diet=diet,
            diseases=diseases,
            allergies=allergies
        )
        dietary_preference.save()

        request.session['user_details'] = {
            'name': dietary_preference.name,
            'email': dietary_preference.email,
            'diet': dietary_preference.diet,
            'diseases': dietary_preference.diseases,
            'allergies': dietary_preference.allergies,
        }

        return redirect('home:invitation')
    return render(request, 'home/index.html')

def invitation(request):
     # Using session to retrieve user details
    user_details = request.session.get('user_details', {})

    return render(request, 'home/invitation.html', {'user_details': user_details})

def summary(request):
    # Count for each diet type
    diet_counts = DietaryPreference.objects.values('diet').annotate(total=Count('diet')).order_by('diet')

    # Count for entries with diseases and allergies
    disease_count = DietaryPreference.objects.exclude(diseases='').count()
    allergy_count = DietaryPreference.objects.exclude(allergies='').count()

    context = {
        'diet_counts': diet_counts,
        'disease_count': disease_count,
        'allergy_count': allergy_count,
    }
    return render(request, 'home/summary.html', context)