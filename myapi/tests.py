from django.test import TestCase
from django.urls import reverse
from .models import Movie, Artist
from django.contrib.auth import get_user_model


class MyAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist1 = Artist.objects.create(
            first_name="Jon", last_name="Favreau", birth_date="1966-10-19"
        )
        cls.artist2 = Artist.objects.create(
            first_name="Robert",
            last_name="Downey",
            nick_name="Robert Downey Jr.",
            birth_date="1965-04-04",
        )
        cls.artist3 = Artist.objects.create(first_name="Gwyneth", last_name="Paltrow")
        cls.movie = Movie.objects.create(
            title="A new Movie",
            year=2024,
            runtime=112,
            status="released",
            director=cls.artist1,
            country="USA",
            plot="A man goes to a park and story begins...",
            rating=7.3,
        )
        cls.movie.cast.set(
            [cls.artist1, cls.artist2, cls.artist3]
        )  # این رو اجازه نمیده موقع تعریف فیلم بذاریم. به خاطر منی تو منی بودن. خودش میگه که باید از تابع ست استفاده کنیم به جاش.
        cls.admin = get_user_model().objects.create_superuser(
            username="admin", password="admin", email="a@b.com"
        )

    def test_get_first_page_by_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_movies_by_url(self):
        response = self.client.get("/movies/")
        self.assertEqual(response.status_code, 200)

    # def test_get_movies_by_url_give_me_error(
    #     self,
    # ):  # این رو عمدا اشتباه زدم که ارور بگیریم. اگه نمیخوایم بگیریم باید یو آر ال درست باشه.
    #     response = self.client.get("movies/")
    #     self.assertEqual(response.status_code, 200)

    def test_get_movies_by_name(self):
        response = self.client.get(
            reverse("movie-list")
        )  # اسمی که خودمون بهش داده بودیم تهش یه دش لیست اضافه میکنیم این میشه اسمی که برای لیست ویوش در نظر میگیره. برای دیتیل ویو هم همین به علاوه دش دیتیل که تو مثال بعدی میبینیم
        self.assertEqual(response.status_code, 200)

    def test_get_movies_detail_by_name(self):
        response = self.client.get(
            reverse("movie-detail", args=[1])
        )  # این طوری دیگه ارور نمیده و پاس میشه. چون تو دیتابیس تست تازه یه آرتیست ساختیم و یه فیلم که کارگردانش همون هست و جزییات فیلم ۱ رو میتونه به ما بده. اما اگه بزنیم فیلم ۲۰ بهمون ارور ۴۰۴ میده چون وجود نداره
        self.assertEqual(response.status_code, 200)

    def test_get_first_name_of_director(self):
        response = self.client.get(reverse("movie-detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        name = data.get("director_info").get("first_name")
        self.assertEqual(name, self.movie.director.first_name)  # OK
        # self.assertEqual(name, "Ali")  # Fail

    def test_get_nick_name_of_second_cast(self):
        response = self.client.get(reverse("movie-detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        name = data.get("cast")[1].get("nick_name")
        self.assertEqual(name, self.artist2.nick_name)  # OK
        # self.assertEqual(name, self.artist1.nick_name)  # Fail

    def test_get_404_if_page_not_exists(self):
        response = self.client.get(reverse("movie-detail", args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_is_posting_a_movie_prohibited(self):
        response = self.client.post(reverse("movie-list"), args=[self.movie])
        self.assertEqual(
            response.status_code, 401
        )  # چون شخص عادی نباید بتونه پست بسازه

    def test_login_as_super_user(self):
        response = self.client.login(username="admin", password="admin")
        self.assertTrue(response)

    # def test_posting_a_movie(self):
    #     response = self.client.post("/auth/jwt/create", "admin", "admin")
    #     print(response)
    #     self.assertEqual(response.status_code, 200)

    # print(response.context)
    # response = self.client.post(reverse("movie-list"), args=[self.movie])
