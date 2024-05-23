from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import FileUpload
from .forms import FileUploadForm


@require_http_methods(["POST"])
def upload_file(request):
    file_obj = request.FILES['file']
    file_instance = FileUpload(file=file_obj)
    file_instance.save()
    return HttpResponse("File uploaded successfully.")


def upload_file_form(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'fileapp/upload_file.html', {
                'form': form,
                'message': 'File uploaded successfully!'
            })
    else:
        form = FileUploadForm()
    return render(request, 'fileapp/upload_file.html', {'form': form})


def download_file(request, file_id):
    file_instance = FileUpload.objects.get(id=file_id)
    response = HttpResponse(
        file_instance.file, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="%s"' % file_instance.file.name
    return response
