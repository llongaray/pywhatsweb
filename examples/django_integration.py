"""
Exemplo de integração do PyWhatsWeb com Django
"""

# Este arquivo demonstra como integrar PyWhatsWeb com Django
# Para usar, copie o código para suas views.py e urls.py do Django

"""
# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import os
import tempfile

from pywhatsweb import WhatsAppClient, DatabaseManager

# Configuração do banco de dados
database = DatabaseManager("localhost")  # Pode ser alterado para sqlite ou mysql

# Cliente WhatsApp global (em produção, use Redis ou similar)
whatsapp_client = None

def index(request):
    # Página principal
    global whatsapp_client
    
    status = {
        'connected': False,
        'authenticated': False,
        'status': 'disconnected'
    }
    
    session_id = "minha_sessao"
    qr_code = None
    
    if whatsapp_client:
        try:
            status = whatsapp_client.get_status()
            session_id = whatsapp_client.session_id
            
            # Verifica se há QR code
            session_data = whatsapp_client.session_manager.get_session(session_id)
            if session_data and session_data.get('qr_code'):
                qr_code = session_data['qr_code']
        except:
            pass
    
    context = {
        'status': status,
        'session_id': session_id,
        'qr_code': qr_code
    }
    
    return render(request, 'whatsapp/index.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def connect(request):
    # Conecta ao WhatsApp
    global whatsapp_client
    
    try:
        data = json.loads(request.body)
        session_id = data.get('session_id', 'minha_sessao')
        
        # Cria novo cliente
        whatsapp_client = WhatsAppClient(session_id, database)
        
        # Conecta
        if whatsapp_client.connect():
            return JsonResponse({'success': True, 'message': 'Conectado com sucesso'})
        else:
            return JsonResponse({'success': False, 'message': 'Erro ao conectar'})
            
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def disconnect(request):
    # Desconecta do WhatsApp
    global whatsapp_client
    
    try:
        if whatsapp_client:
            whatsapp_client.disconnect()
            whatsapp_client = None
        
        return JsonResponse({'success': True, 'message': 'Desconectado com sucesso'})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def send_message(request):
    # Envia mensagem de texto
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return JsonResponse({'success': False, 'message': 'Cliente não autenticado'})
        
        data = json.loads(request.body)
        phone = data.get('phone')
        message = data.get('message')
        
        if not phone or not message:
            return JsonResponse({'success': False, 'message': 'Dados incompletos'})
        
        # Envia mensagem
        message_id = whatsapp_client.send_message(phone, message)
        
        return JsonResponse({'success': True, 'message': 'Mensagem enviada', 'message_id': message_id})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def send_file(request):
    # Envia arquivo (imagem/documento)
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return JsonResponse({'success': False, 'message': 'Cliente não autenticado'})
        
        phone = request.POST.get('phone')
        file = request.FILES.get('file')
        
        if not phone or not file:
            return JsonResponse({'success': False, 'message': 'Dados incompletos'})
        
        # Salva arquivo temporariamente
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.name)
        
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Determina tipo de arquivo
        file_ext = os.path.splitext(file.name)[1].lower()
        image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        
        if file_ext in image_exts:
            message_id = whatsapp_client.send_image(phone, file_path, "Arquivo enviado via Django")
        else:
            message_id = whatsapp_client.send_document(phone, file_path, "Documento enviado via Django")
        
        # Remove arquivo temporário
        os.remove(file_path)
        os.rmdir(temp_dir)
        
        return JsonResponse({'success': True, 'message': 'Arquivo enviado', 'message_id': message_id})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@require_http_methods(["GET"])
def get_chats(request):
    # Obtém lista de chats
    global whatsapp_client
    
    try:
        if not whatsapp_client or not whatsapp_client.authenticated:
            return JsonResponse({'success': False, 'message': 'Cliente não autenticado'})
        
        chats = whatsapp_client.get_chats()
        return JsonResponse({'success': True, 'chats': chats})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
@require_http_methods(["POST"])
def delete_session(request):
    # Deleta a sessão atual
    global whatsapp_client
    
    try:
        if whatsapp_client:
            session_id = whatsapp_client.session_id
            whatsapp_client.session_manager.delete_session(session_id)
            whatsapp_client = None
        
        return JsonResponse({'success': True, 'message': 'Sessão deletada'})
        
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@require_http_methods(["GET"])
def status(request):
    # Retorna status atual
    global whatsapp_client
    
    try:
        if whatsapp_client:
            return JsonResponse(whatsapp_client.get_status())
        else:
            return JsonResponse({
                'session_id': None,
                'connected': False,
                'authenticated': False,
                'status': 'disconnected',
                'phone_number': None
            })
            
    except Exception as e:
        return JsonResponse({'error': str(e)})
"""

"""
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='whatsapp_index'),
    path('connect/', views.connect, name='whatsapp_connect'),
    path('disconnect/', views.disconnect, name='whatsapp_disconnect'),
    path('send_message/', views.send_message, name='whatsapp_send_message'),
    path('send_file/', views.send_file, name='whatsapp_send_file'),
    path('get_chats/', views.get_chats, name='whatsapp_get_chats'),
    path('delete_session/', views.delete_session, name='whatsapp_delete_session'),
    path('status/', views.status, name='whatsapp_status'),
]
"""

"""
# settings.py (adicione ao seu Django)
INSTALLED_APPS = [
    # ... suas apps
    'whatsapp',  # sua app do WhatsApp
]

# Configurações do PyWhatsWeb
PYWHATSWEB_CONFIG = {
    'database_type': 'localhost',  # ou 'sqlite', 'mysql'
    'sqlite_path': 'whatsapp_sessions.db',  # se usar SQLite
    'mysql_config': {  # se usar MySQL
        'host': 'localhost',
        'user': 'seu_usuario',
        'password': 'sua_senha',
        'database': 'whatsapp_db',
        'port': 3306
    }
}
"""

"""
# models.py (opcional - para salvar mensagens no banco do Django)
from django.db import models
from django.utils import timezone

class WhatsAppMessage(models.Model):
    MESSAGE_TYPES = [
        ('text', 'Texto'),
        ('image', 'Imagem'),
        ('document', 'Documento'),
        ('audio', 'Áudio'),
        ('video', 'Vídeo'),
    ]
    
    STATUS_CHOICES = [
        ('sent', 'Enviado'),
        ('delivered', 'Entregue'),
        ('read', 'Lido'),
        ('failed', 'Falhou'),
    ]
    
    session_id = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255, unique=True)
    from_number = models.CharField(max_length=20, null=True, blank=True)
    to_number = models.CharField(max_length=20)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES)
    content = models.TextField()
    caption = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='sent')
    
    class Meta:
        db_table = 'whatsapp_messages'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.message_type} para {self.to_number} - {self.status}"
"""

"""
# admin.py (opcional - para gerenciar mensagens no admin do Django)
from django.contrib import admin
from .models import WhatsAppMessage

@admin.register(WhatsAppMessage)
class WhatsAppMessageAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'message_type', 'to_number', 'status', 'timestamp']
    list_filter = ['message_type', 'status', 'timestamp']
    search_fields = ['message_id', 'to_number', 'content']
    readonly_fields = ['message_id', 'timestamp']
    
    def has_add_permission(self, request):
        return False  # Mensagens só podem ser criadas via API
"""

"""
# middleware.py (opcional - para gerenciar sessões automaticamente)
from django.utils.deprecation import MiddlewareMixin
from pywhatsweb import WhatsAppClient, DatabaseManager

class WhatsAppMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Inicializa cliente WhatsApp se necessário
        if not hasattr(request, 'whatsapp_client'):
            database = DatabaseManager("localhost")
            request.whatsapp_client = WhatsAppClient("session_web", database)
        
        return None
    
    def process_response(self, request, response):
        # Fecha cliente WhatsApp se necessário
        if hasattr(request, 'whatsapp_client'):
            request.whatsapp_client.close()
        
        return response
"""

"""
# forms.py (opcional - para formulários de envio)
from django import forms

class WhatsAppMessageForm(forms.Form):
    phone_number = forms.CharField(
        label='Número de Destino',
        max_length=20,
        help_text='Ex: 5511999999999'
    )
    
    message = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'rows': 4}),
        max_length=4096
    )
    
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        # Aqui você pode adicionar validação do número
        return phone

class WhatsAppFileForm(forms.Form):
    phone_number = forms.CharField(
        label='Número de Destino',
        max_length=20
    )
    
    file = forms.FileField(
        label='Arquivo',
        help_text='Imagem, documento, áudio ou vídeo'
    )
    
    caption = forms.CharField(
        label='Legenda',
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={'rows': 3})
    )
"""

"""
# signals.py (opcional - para ações automáticas)
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WhatsAppMessage

@receiver(post_save, sender=WhatsAppMessage)
def on_message_saved(sender, instance, created, **kwargs):
    if created:
        # Aqui você pode implementar lógicas automáticas
        # como notificações, logs, etc.
        print(f"Nova mensagem salva: {instance.message_id}")
"""

"""
# tasks.py (opcional - para Celery/background tasks)
from celery import shared_task
from pywhatsweb import WhatsAppClient, DatabaseManager

@shared_task
def send_whatsapp_message(phone_number, message, session_id="default"):
    # Task para enviar mensagem WhatsApp em background
    try:
        database = DatabaseManager("localhost")
        client = WhatsAppClient(session_id, database)
        
        if client.connect():
            if client.wait_for_authentication(timeout=60):
                message_id = client.send_message(phone_number, message)
                client.close()
                return {'success': True, 'message_id': message_id}
            else:
                client.close()
                return {'success': False, 'error': 'Falha na autenticação'}
        else:
            return {'success': False, 'error': 'Erro ao conectar'}
            
    except Exception as e:
        return {'success': False, 'error': str(e)}

@shared_task
def send_whatsapp_file(phone_number, file_path, file_type, caption="", session_id="default"):
    # Task para enviar arquivo WhatsApp em background
    try:
        database = DatabaseManager("localhost")
        client = WhatsAppClient(session_id, database)
        
        if client.connect():
            if client.wait_for_authentication(timeout=60):
                if file_type == 'image':
                    message_id = client.send_image(phone_number, file_path, caption)
                else:
                    message_id = client.send_document(phone_number, file_path, caption)
                
                client.close()
                return {'success': True, 'message_id': message_id}
            else:
                client.close()
                return {'success': False, 'error': 'Falha na autenticação'}
        else:
            return {'success': False, 'error': 'Erro ao conectar'}
            
    except Exception as e:
        return {'success': False, 'error': str(e)}
"""

"""
# Exemplo de uso nas views
def send_bulk_message(request):
    # Envia mensagem em massa (usando Celery)
    if request.method == 'POST':
        form = WhatsAppMessageForm(request.POST)
        if form.is_valid():
            phone_numbers = request.POST.getlist('phone_numbers')
            message = form.cleaned_data['message']
            
            # Envia mensagens em background
            for phone in phone_numbers:
                send_whatsapp_message.delay(phone, message)
            
            messages.success(request, f"{len(phone_numbers)} mensagens agendadas para envio")
            return redirect('whatsapp_index')
    else:
        form = WhatsAppMessageForm()
    
    return render(request, 'whatsapp/bulk_message.html', {'form': form})
"""

print("Este arquivo contém exemplos de integração com Django.")
print("Copie o código relevante para seus arquivos Django.")
print("Lembre-se de instalar as dependências necessárias:")
print("- Django")
print("- PyWhatsWeb (esta biblioteca)")
print("- mysql-connector-python (se usar MySQL)")
print("- Celery (se usar tasks em background)")
