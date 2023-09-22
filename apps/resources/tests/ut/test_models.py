from django.test import TestCase
from apps.resources import models

# Test Case class Test<name>Model

class TestTagModel(TestCase):
    def setUp(self) -> None:
        self.tag_name = 'Python'
        self.tag = models.Tag(name=self.tag_name)

    # unittest 1 # test_<logic_name>
    def test_create_tag_object_successful(self):
        # check if object created is of the instance Tag
        self.assertIsInstance(self.tag, models.Tag)
    
    # unittest 2 # test_<logic_name>        
    def test_dunder_str(self):
        str(self.tag.name) # self.tag.__str__()
        self.assertEqual(str(self.tag), self.tag_name)
        
        
class TestCategoryModel(TestCase):

    """ def setUp(self) -> None:
        self.category_data = {'cat': 'Test Category'}

    def test_category_creation(self):
        # Create a Category object
        category = models.Category.objects.create(**self.category_data)

        # Query the database to see if the Category object exists
        category_from_db = models.Category.objects.get(cat='Test Category')

        # Check if the Category object was created successfully
        self.assertEqual(category, category_from_db)

    def test_verbose_name_plural(self):
        self.assertEqual(models.Category._meta.verbose_name_plural, 'Categories') """
        
        
    def setUp(self) -> None:
        self.category_name = 'Python'
        self.category = models.Category(cat = self.category_name)
        
    def test_create_category_object_successfully(self):
        self.assertIsInstance(self.category, models.Category)
        
    def test_category_method_str(self):
        self.assertEqual(str(self.category), self.category_name)
        
    def test_category_meta_verbose_name_plural(self):
        name = "Categories"
        self.assertEqual(name, models.Category._meta.verbose_name_plural)
        
        
     # TODO: Test all models