from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class CropSolution(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crop_images/')
    description = models.TextField()
    guide = models.FileField(upload_to='guides/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.job.title}"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class HeroImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='hero_images/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or f"Hero Image {self.id}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}'s Testimonial"


# models.py
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    short_description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    is_bestseller = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Model for Services
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model for Careers
class Career(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model for Blog Posts
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model for Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
class Consultation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Equipment(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    image = models.ImageField(upload_to='equipment_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.BooleanField(default=False)
    key_feature_1 = models.CharField(max_length=255, blank=True, null=True)
    key_feature_2 = models.CharField(max_length=255, blank=True, null=True)
    key_feature_3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name