from django.test import TestCase
from api.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """"
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test category default name

        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):

    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='All', slug='All')
        self.data1 = Product.objects.create(category_id=2, name='django product', slug='django product',
                                            price='20.00', product_image='pants', created_by_id=1)

    def test_model_product_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django product')
