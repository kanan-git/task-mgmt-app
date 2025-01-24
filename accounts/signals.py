# from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
# from django.dispatch import receiver
# from django.contrib.auth.models import User

# from .models import Account


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user=instance)
