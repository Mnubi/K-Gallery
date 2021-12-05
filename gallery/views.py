
from django.shortcuts import render
from .models import Photos, Category, Location
# Create your views here.


# index function to display all images
def index(request):
    # get all images ordered by the most recent
    images = Photos.objects.all().order_by('-id')
    # images = Photos.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Homepage'
    return render(request, 'index.html', {'images': images, 'locations': locations, 'categories': categories, 'title': title})


# search function to search for images
# search function to search for images
def search(request):
    
    location=Location.get_locations()

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Photos.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'search.html')

def location(request,location_name):
    location=Location.get_locations()
    image= Photos.get_images_by_location(location_name)
    message = f"{location_name}"
    return render(request, 'location.html',{"message":message,"image": image,"location":location})

def image_properties(request,image_id):
    location=Location.get_locations()

    image = Photos.get_image_by_id(image_id)
    return render(request, {"image" : image,"location":location})

# display all images in a specific location
def location(request, location_id):
    locations = Location.objects.all()
    images = Photos.objects.filter(location_id=location_id)
    # get the location name
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})


# display single image details
def image(request, image_id):
    locations = Location.objects.all()
    image = Photos.objects.get(id=image_id)
    title = image
    return render(request, 'image.html', {'image': image, 'locations': locations, 'title': title})