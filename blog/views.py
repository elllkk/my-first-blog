from django.http import HttpResponse
from django import forms

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UploadFileForm(forms.Form):
    file = forms.FileField()


# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })
