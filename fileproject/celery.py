from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define a variável de ambiente padrão para o Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fileproject.settings')

# Instancia o objeto Celery para o projeto
app = Celery('FileHandlerPro')

# Carrega todas as configurações do Celery do arquivo settings do Django, usando um namespace 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodescoberta de tarefas nos aplicativos Django
app.autodiscover_tasks()
