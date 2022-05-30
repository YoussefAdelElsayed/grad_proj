from django.db.models.signals import post_save, post_delete,pre_save
from django.dispatch import receiver
from .models import Lecture
import os

@receiver(post_delete, sender=Lecture)
def post_delete_video_Lecture(sender, instance, *args, **kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)

