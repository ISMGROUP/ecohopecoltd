from django.shortcuts import render, get_object_or_404
from .models import Product, Service, Consultation, CropSolution, Equipment, Subscriber, Career, BlogPost, TeamMember, ContactMessage, HeroImage, Testimonial
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
import smtplib
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.db.models import Q
# Search View

from .models import Job, Application
from .forms import ApplicationForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.candidate = request.user
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'job_detail.html', {'job': job, 'form': form})

def apply_to_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return render(request, 'careers/application_successiful.html', {'job': job})
    else:
        form = ApplicationForm()
    return render(request, 'careers/apply.html', {'form': form, 'job': job})

def application_successiful(request):
    return render(request, 'application_successiful.html')

def search(request):
    query = request.GET.get('query')
    services = about_match = None

    if query:
        services = Service.objects.filter(title__icontains=query)
        if 'about' in query.lower():
            about_match = True

    context = {
        'query': query,
        'services': services,
        'about_match': about_match,
    }
    return render(request, 'search_results.html', context)

# Home Page View
def home(request):
    hero_images = HeroImage.objects.filter(active=True)
    testimonials = Testimonial.objects.filter(active=True)
    services = Service.objects.all()

    return render(request, 'index.html', {
        'hero_images': hero_images,
        'testimonials': testimonials,
        'services': services,
    })

# About Page View
def about(request):
    hero_images = HeroImage.objects.filter(active=True)
    context = {'title': 'About Us'}
    return render(request, 'about.html', {
        'hero_images': hero_images,
        })

def our_team(request):
    members = TeamMember.objects.all()
    return render(request, 'our_team.html', {'members': members})
# Products Page View
def products(request):
    context = {
        'title': 'Our Products',
        'products': [
            {'name': 'Organic Fertilizer', 'description': 'High-quality compost for better crops.'},
            {'name': 'Animal Feeds', 'description': 'Nutrient-rich feeds for livestock health.'}
        ]
    }
    return render(request, 'products.html', context)

# Services Page View
def services(request):
    context = {
        'title': 'Our Services',
        'services': [
            'Agricultural Consultancy',
            'Training Programs',
            'Supply of Organic Farming Inputs'
        ]
    }
    return render(request, 'services.html', context)

# Service Detail View
def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', {'service': service})

# Careers Page View
def careers(request):
    context = {
        'title': 'Join Our Team',
        'job_openings': [
            {'title': 'Farm Manager', 'location': 'Arua, Uganda'},
            {'title': 'Sales Representative', 'location': 'Kampala, Uganda'}
        ]
    }
    return render(request, 'careers.html', context)

# Blog Page View
def blog(request):
    context = {
        'title': 'Our Blog',
        'posts': [
            {'title': 'Sustainable Farming Tips', 'date': '2025-04-03'},
            {'title': 'The Future of Agribusiness in Uganda', 'date': '2025-03-28'}
        ]
    }
    return render(request, 'blog.html', context)

# Contact Page View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject'] or 'No Subject'
            message = form.cleaned_data['message']

            # 1. Send email to your team
            send_mail(
                subject=f"New Contact Message: {subject}",
                message=f"From: {name} <{email}>\nPhone: {phone}\n\nMessage:\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['ecohopeuganda@gmail.com'],  # Replace with your actual inbox
                fail_silently=False,
            )

            # 2. Auto-reply to the sender
            send_mail(
                subject="Thanks for contacting Eco Hope Co. Ltd",
                message=(
                    f"Dear {name},\n\n"
                    "Thank you for reaching out to us! We have received your message and will get back to you shortly.\n\n"
                    "Best regards,\n"
                    "Eco Hope Co. Ltd\n"
                    "📍 Plot 12, Eco Hope Street, Arua City, Uganda\n"
                    "📧 info@ecohopeco.com | 📞 +256 766 670 007"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_successiful')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.info(request, 'You are already subscribed!')
            else:
                try:
                    # Save the email to the database
                    Subscriber.objects.create(email=email)

                    # Send confirmation email
                    send_mail(
                        subject='Thanks for Subscribing!',
                        message='Hello! You are now subscribed to Eco Hope updates.',
                        from_email='ecohopeuganda@gmail.com',
                        recipient_list=[email],
                        fail_silently=False,
                    )
                    messages.success(request, 'Subscribed successfully!')
                except Exception as e:
                    messages.error(request, f'Error: {e}')
                    return redirect(request.META.get('HTTP_REFERER', '/'))

            return redirect('subscription_successiful')
        else:
            messages.error(request, 'Please enter a valid email.')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('subscription_successiful')

def subscription_successiful(request):
    return render(request, 'subscription_successiful.html')

def our_story(request):
    return render(request, 'our_story.html')

def awards(request):
    return render(request, 'awards.html')

def clients(request):
    return render(request, 'clients.html')

def press(request):
    return render(request, 'press.html')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you could save the email to the database or send it somewhere
        messages.success(request, "Thank you for subscribing!")
        return redirect('newsletter')  # Redirect after POST to avoid resubmission
    return render(request, 'newsletter.html')  # ✅ FIXED: Added `request` as first argument


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def consultation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        message = request.POST.get('message')

        # ✅ Save to database
        Consultation.objects.create(
            name=name,
            email=email,
            phone=phone,
            location=location,
            message=message
        )

        # ✅ Send email to admin
        admin_subject = 'New Consultation Request from Eco Hope Website'
        admin_message = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Location: {location}
        Message: {message}
        """
        send_mail(
            admin_subject,
            admin_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        # ✅ Auto-reply to client
        user_subject = 'Thank You for Contacting Eco Hope Co. Ltd'
        user_message = f"""
        Hi {name},

        Thank you for reaching out to Eco Hope Co. Ltd!
        We’ve received your consultation request and one of our team members will get back to you shortly.

        Best regards,  
        Eco Hope Co. Ltd  
        Phone: +256 712 345 678  
        Email: info@ecohopeco.com  
        """
        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, 'Thank you! Your consultation request has been submitted.')
        return redirect('consultation_submitted')

    return render(request, 'consultation.html')


def consultation_submitted(request):
    return render(request, 'consultation_submitted.html')

def search_view(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Search across multiple models if needed
        results = YourModel.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    
    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })

def crop_solutions(request):
    crop_products = Product.objects.all()
    return render (request, 'crop_solutions.html', {'crop_products': crop_products})

def equipment(request):
    featured = Equipment.objects.all()[:8]  # or use a filter like `.filter(is_featured=True)`
    return render(request, 'equipment.html', {'featured_equipment': featured})


def equipment_list(request):
    featured = Equipment.objects.all()[:8]  # or use a filter like `.filter(is_featured=True)`
    return render(request, 'equipment.html', {'featured_equipment': featured})
def terms(request):
    return render(request, 'terms.html')

def contact_successiful(request):
    return render(request, 'contact_successiful.html')

