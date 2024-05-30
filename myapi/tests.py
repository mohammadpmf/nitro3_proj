from django.test import TestCase
from django.urls import reverse

class MyAPITest(TestCase):
    def test_get_first_page_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_movies_by_url(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)
    
    # def test_get_movies_by_url_give_me_error(self): # این رو عمدا اشتباه زدم که ارور بگیریم. اگه نمیخوایم بگیریم باید یو آر ال درست باشه.
    #     response = self.client.get('movies/')
    #     self.assertEqual(response.status_code, 200)

    def test_get_movies_by_name(self):
        response = self.client.get(reverse('movie-list')) # اسمی که خودمون بهش داده بودیم تهش یه دش لیست اضافه میکنیم این میشه اسمی که برای لیست ویوش در نظر میگیره. برای دیتیل ویو هم همین به علاوه دش دیتیل که تو مثال بعدی میبینیم
        self.assertEqual(response.status_code, 200)

    def test_get_movies_detail_by_name(self):
        response = self.client.get(reverse('movie-detail', args=[1])) # ارور میده. چون یه دیتابیس تست تازه میسازه و توش هیچ فیلمی نیست. پس ۴۰۴ میده. پس باید یه نمونه بسازیم
        self.assertEqual(response.status_code, 200)
        