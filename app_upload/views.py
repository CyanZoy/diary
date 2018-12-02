from django.shortcuts import render, HttpResponse
import json
from app_upload.util import save_image


def index(request):
    if request.method == 'POST':
        myfile = request.FILES.get('file_data', None)
        if str(myfile)[-3:] in ['jpg', 'jpeg', 'png', 'PNG', 'JPG', 'JPEG']:
            # save_image.save(myfile, str(myfile)[-3:])
            pass
        return HttpResponse(json.dumps(False))
    return render(request, 'upload/upload.html', {})
