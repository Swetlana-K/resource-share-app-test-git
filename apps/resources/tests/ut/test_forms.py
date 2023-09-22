from django.test import TestCase
from apps.resources.form import PostResourceForm

class TestPostResourceForm(TestCase):
    # unit test 1
    def test_from_is_valid_method_return_true_for_good_data(self):
        # Arrange
        data = {
            'title':'Python fpr beginners',
            'link':'http://python.com',
            'description' : "Best resource for beginners and free",
            
        }
        # Act
        form = PostResourceForm(data=data)
        
        # Assert
        self.assertTrue(form.is_valid())
        
    def test_form_not_valid_when_link_is_missing(self):
        # Arrange
        data = {
            'title':'Python fpr beginners',
            # 'link':'http://python.com',
            'description' : "Best resource for beginners and free",
            
        }
        # Act
        form = PostResourceForm(data=data)
        form.is_valid()
        
        # Assert
        #self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['link'], ['This field is required.'])
        
    def test_form_not_valid_when_link_is_missing(self):
        # Arrange
        data = {
            'title': 'Python for beginners',
            # 'link': 'http://python.com',
            'description': "Best resource for beginners and free",
        }
        # Act
        form = PostResourceForm(data=data)
        form.is_valid()
        
        # Assert
        self.assertEqual(form.errors['link'], ['This field is required.'])