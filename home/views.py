from django.shortcuts import render, redirect
from .models import DietaryPreference, InvitationDetail, DietPreference
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils.dateformat import DateFormat

# Create your views here.

# Check if the user is a superadmin
def is_superadmin(user):
    return user.is_authenticated and user.is_superuser

def register_superadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Create a new superadmin user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return redirect('home:login')
    return render(request, 'home/register_superadmin.html')

def login_superadmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, 'home/login_superadmin.html', {'error': 'Invalid credentials or not a superadmin.'})
    return render(request, 'home/login_superadmin.html')

@user_passes_test(is_superadmin)
def logout_superadmin(request):
    logout(request)
    return redirect('home:login')

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
    diet_preferences = DietPreference.objects.all()
    return render(request, 'home/index.html', {'diet_preferences': diet_preferences})

def invitation(request):
    user_details = request.session.get('user_details', {})
    try:
        invitation_details = InvitationDetail.objects.latest('id')
    except InvitationDetail.DoesNotExist:
        invitation_details = None
    party_date = DateFormat(invitation_details.party_date).format('jS F Y') if invitation_details else '14th February 2100'
    context = {
        'user_details': user_details,
        'party_title': invitation_details.party_title if invitation_details else 'One party Lunch Together!',
        'party_message': invitation_details.party_message if invitation_details else 'Join me for an afternoon of lunch and fun.',
        'party_date': invitation_details.party_date if invitation_details else 'Wednesday, 14th February',
        'timezone': invitation_details.timezone if invitation_details else 'INR',
        'party_time': invitation_details.party_time if invitation_details else '01:00 PM onwards',
        'party_location': invitation_details.party_location if invitation_details else 'Indian Navy ILMS',
        'main_course': f'A special {user_details.get("diet", "").capitalize()} meal curated for you.' if user_details.get("diet") else 'A special meal curated for you.',
        'optional_desserts': invitation_details.optional_desserts if invitation_details else 'Optional Icecream and/or Rasgulla',
        'gift': invitation_details.gift if invitation_details else False,
        'gift_message': invitation_details.gift_message if invitation_details else 'As a token of appreciation, every guest will receive a special return gift. It’s a surprise I hope you\'ll love!'
    }
    return render(request, 'home/invitation.html', context)

@user_passes_test(is_superadmin)
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