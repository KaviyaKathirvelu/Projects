from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
        self.data2 = Category.objects.create(name='django', slug='django')
        self.data3 = Category.objects.create(name='django', slug='django')
        self.data4 = Category.objects.create(name='django', slug='django')
        self.data5 = Category.objects.create(name='django', slug='django')



    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data1 = self.data1
        data2 = self.data2
        data3 = self.data3
        data4 = self.data4
        data5 = self.data5
        self.assertEqual(str(data1), 'english')
        self.assertEqual(str(data2), 'maths')
        self.assertEqual(str(data3), 'social')
        self.assertEqual(str(data4), 'science')
        self.assertEqual(str(data5), 'hindi')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data1 = self.data1
        response = self.client.post(reverse('store:category_list', args=[data1.slug]))
        self.assertEqual(response.status_code, 200)

        data2 = self.data2
        response = self.client.post(
            reverse('store:category_list', args=[data2.slug]))
        self.assertEqual(response.status_code, 200)

        data3 = self.data3
        response = self.client.post(
            reverse('store:category_list', args=[data3.slug]))
        self.assertEqual(response.status_code, 200)

        data4 = self.data4
        response = self.client.post(
            reverse('store:category_list', args=[data4.slug]))
        self.assertEqual(response.status_code, 200)

        data5 = self.data5
        response = self.client.post(
            reverse('store:category_list', args=[data5.slug]))
        self.assertEqual(response.status_code, 200)
     
     
class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='english', created_by_id=1,
                                            slug='django-beginners',price='50.00', image='django')
        self.data2 = Product.objects.create(category_id=1, title='maths', created_by_id=1,
                                            slug='django-beginners',price='90.00', image='django')
        self.data3 = Product.objects.create(category_id=1, title='social', created_by_id=1,
                                            slug='django-beginners',price='80.00', image='django')
        self.data4 = Product.objects.create(category_id=1, title='science', created_by_id=1,
                                            slug='django-beginners',price='80.00', image='django')
        self.data5 = Product.objects.create(category_id=1, title='hindi', created_by_id=1,
                                            slug='django-beginners',price='92.00', image='django')


    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributs
        """
        data1 = self.data1
        data2 = self.data2
        data3 = self.data3
        data4 = self.data4
        data5 = self.data5
        self.assertTrue(isinstance(data1, Product))
        self.assertTrue(isinstance(data2, Product))
        self.assertTrue(isinstance(data3, Product))
        self.assertTrue(isinstance(data4, Product))
        self.assertTrue(isinstance(data5, Product))
        self.assertEqual(str(data1), 'english')
        self.assertEqual(str(data2), 'maths')
        self.assertEqual(str(data3), 'social')
        self.assertEqual(str(data4), 'science')
        self.assertEqual(str(data5), 'hindi')
 
    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data1 = self.data1
        url = reverse('store:product_detail', args=[data1.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data1.slug]))
        self.assertEqual(response.status_code, 200)

        data2 = self.data2
        url = reverse('store:product_detail', args=[data2.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data2.slug]))
        self.assertEqual(response.status_code, 200)

        data3 = self.data3
        url = reverse('store:product_detail', args=[data3.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data3.slug]))
        self.assertEqual(response.status_code, 200)

        data4 = self.data4
        url = reverse('store:product_detail', args=[data4.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data4.slug]))
        self.assertEqual(response.status_code, 200)

        data5 = self.data5
        url = reverse('store:product_detail', args=[data5.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data5.slug]))
        self.assertEqual(response.status_code, 200)

       
    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data1 = Product.products.all()
        self.assertEqual(data1.count(), 1)
        data2 = Product.products.all()
        self.assertEqual(data2.count(), 1)
        data3 = Product.products.all()
        self.assertEqual(data3.count(), 1)
        data4 = Product.products.all()
        self.assertEqual(data4.count(), 1)
        data5 = Product.products.all()
        self.assertEqual(data5.count(), 1)
    
    