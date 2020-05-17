from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from first_app.blending import blendimages
from first_app.blending1 import blendimages1
# Create your views here.
import os

def index(request):
   
    my_dic={'insert_me':"hello iam from views.py"}
    if request.method == 'POST':
        print(request.POST.get("blend-tech", ""))
        blend_type = request.POST.get("blend-tech", "")

        fs = FileSystemStorage()
       
        file_paths = []
        for file_name in request.FILES:
            upload_file = request.FILES[file_name]
            extension = os.path.splitext(upload_file.name)[1]
            file_path = os.path.join(settings.MEDIA_ROOT_URL, file_name + extension)
            file_paths.append(file_path)
            filename = fs.save(file_path, request.FILES[file_name])
        if(blend_type=="half-half"):
            
            blend_img_path= blendimages(*file_paths)
        elif(blend_type=="image-within-image"):
            blend_img_path= blendimages1(*file_paths)

                
        try:
            with open(blend_img_path, "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            return render(request,'index.html',context=my_dic)
        
        
        
    return render(request,'index.html',context=my_dic)