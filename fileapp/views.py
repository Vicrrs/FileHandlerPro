from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import FileUpload


@require_http_methods(["POST"])
def upload_file(request):
    file_obj = request.FILES['file']
    file_instance = FileUpload(file=file_obj)
    file_instance.save()
    return HttpResponse("File uploaded successfully.")


def download_file(request, file_id):
    file_instance = FileUpload.objects.get(id=file_id)
    response = HttpResponse(file_instance.file, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file_instance.file.name
    return response
