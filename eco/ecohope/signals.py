from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import BlogPost, Subscriber
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=BlogPost)
def notify_subscribers(sender, instance, created, **kwargs):
    if created and getattr(instance, 'published', False):  # Check if published exists and True
        subscribers = Subscriber.objects.all()
        subject = f"New Blog Post: {instance.title}"
        
        # Construct the full URL
        blog_url = settings.SITE_URL + reverse('blog_detail', kwargs={'slug': instance.slug})
        
        message = (
            f"{instance.title}\n\n"
            f"{instance.excerpt}\n\n"
            f"Read more here: {blog_url}"
        )

        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [subscriber.email for subscriber in subscribers]

        if recipient_list:
            send_mail(subject, message, from_email, recipient_list)
