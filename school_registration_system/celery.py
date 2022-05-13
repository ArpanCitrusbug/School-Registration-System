from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_registration_system.settings')

app = Celery('school_registration_system',include=['school_registration_system.celery'],broker=settings.CELERY_BROKER_URL,backend=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='Celery')

#Celery Beat Settings

    
# }

# Looks up for task modules in Django applications and loads them

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"request:{self.request!r}")


    # celery -A school_registration_system.celery worker --pool=solo -l info