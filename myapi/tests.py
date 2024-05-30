from django.test import TestCase
from django.urls import reverse
from .models import Movie, Artist

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
        artist1 = Artist.objects.create(first_name="David", last_name="Newman", nick_name="DaNewman")
        Movie.objects.create(
            title="A new Movie",
            year=2024,
            runtime=112,
            status="released",
            director=artist1,
            country="USA",
            plot="A man goes to a park and story begins...",
            rating=7.3
        )
        response = self.client.get(reverse('movie-detail', args=[1])) # این طوری دیگه ارور نمیده و پاس میشه. چون تو دیتابیس تست تازه یه آرتیس ساختیم و یه فیلم که کارگردانش همون هست و جزییات فیلم ۱ رو میتونه به ما بده. اما اگه بزنیم فیلم ۲۰ بهمون ارور ۴۰۴ میده چون وجود نداره
        self.assertEqual(response.status_code, 200)
        