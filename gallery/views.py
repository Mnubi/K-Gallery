
from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.


# index function to display all images
def index(request):
    # get all images ordered by the most recent
    images = Image.objects.all().order_by('-id')
    # images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Homepage'
    return render(request, 'index.html', {'images': images, 'locations': locations, 'categories': categories, 'title': title})


# search function to search for images
def search(request):
    if 'category' in request.GET and request.GET["category"]:
        # change the search to be in lowercase
        search_term = request.GET.get("category").lower()
        searched_images = Image.filter_by_category(search_term)
        message = f"{search_term}"
        locations = Location.objects.all()

        return render(request, 'search.html', {"message": message, "images": searched_images, 'locations': locations})

    else:
        locations = Location.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, 'locations': locations})


# display all images in a specific location
def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    # get the location name
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})


# display single image details
def image(request, image_id):
    locations = Location.objects.all()
    image = Image.objects.get(id=image_id)
    title = image
    return render(request, 'image.html', {'image': image, 'locations': locations, 'title': title})