from django.test import TestCase
from .models import Category, Location, Photos

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='wild')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Kakamega')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locat = Location.objects.all()
        self.assertTrue(len(locat) > 0) 

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)

class ImagesTestClass(TestCase):
    
    def setUp(self):

        self.location = Location(location_name='Kakamega')
        self.location.save_location()

        self.category = Category(category_name='Wild')
        self.category.save_category()

        self.wild= Photos(id=1,image_name = 'River', image_details ='Testing images class model',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.wild,Photos))
    
    def test_save_image(self):
        self.wild.save_image()
        image = Photos.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_image(self):
        self.wild.delete_image()
        image = Photos.objects.all()
        self.assertTrue(len(image)== 0)


    def test_get_image_by_id(self):
        self.wild.save_image()
        img = self.wild.get_image_by_id(self.wild.id)
        images = Photos.objects.filter(id=self.wild.id)
        self.assertTrue(img, images) 

    def test_search_by_category(self):
        category = 'wild'
        found_img = self.wild.search_by_category(category)
        self.assertFalse(len(found_img) > 1)  

    def tearDown(self):
        Photos.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()