from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class SnacksTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 


    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html") 
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_detail_status_code(self):
        url = reverse('detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200) 


    def test_snack_detail_template(self):
        url = reverse('detail')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html") 
        self.assertTemplateUsed(response, "snack_detail.html") 
        
         
