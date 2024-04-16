import random
import factory
from datetime import datetime
from faker import Faker
from factory.django import DjangoModelFactory

from . import models

faker = Faker()


class GenreMovieFactory(DjangoModelFactory):
    class Meta:
        model = models.GenreMovie
    title = factory.Faker("word")


class GenreMusicFactory(DjangoModelFactory):
    class Meta:
        model = models.GenreMusic
    title = factory.Faker("word")


class ArtistFactory(DjangoModelFactory):
    class Meta:
        model = models.Artist
    
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    nick_name = factory.LazyAttribute(lambda x: '' if random.randint(1, 2)==1 else f"{x.first_name}" if random.randint(1, 2)==1 else f"{x.first_name}-{x.last_name}")
    birth_date = factory.LazyFunction(lambda: faker.date_time_ad(start_datetime=datetime(1925,1,1), end_datetime=datetime(2019,1,1)))


class MovieFactory(DjangoModelFactory):
    class Meta:
        model = models.Movie

    title = factory.LazyAttribute(lambda x: ' '.join([x.capitalize() for x in faker.words(3)]))
    year = factory.LazyFunction(lambda: random.randint(1920, 2020))
    runtime = factory.LazyFunction(lambda: random.randint(80, 210))
    # status = factory.LazyFunction(lambda: random.choice(models.Movie.STATUS_MOVIES)[0]) # پیش فرض گفتم همه ریلیزد باشن بهتره.
    # director # لازم نیست بنویسم. چون فارین کی هست خودش درست میکنه.
    country = factory.Faker("country")
    plot = factory.Faker('paragraph', nb_sentences=5, variable_nb_sentences=True)
    # poster # عکس ها اختیاری بودن. نذاشتم که سنگین نشه.
    rating = factory.LazyFunction(lambda: random.randint(0, 9) + random.randint(0, 10)/10)
    # release_date # اختیاری بود. نذاشتم که خالی باشه.
    # genre # تو فایل ستاپ فیک دیتا مقدار دادم.
    # cast # تو فایل ستاپ فیک دیتا مقدار دادم.


class SerialFactory(DjangoModelFactory):
    class Meta:
        model = models.Serial
    
    title = factory.LazyAttribute(lambda x: ' '.join([x.capitalize() for x in faker.words(3)]))
    number_of_seasons = factory.LazyFunction(lambda: random.randint(1, 7))
    number_of_episodes = factory.LazyFunction(lambda: random.randint(8, 122))
    begin_year = factory.LazyFunction(lambda: random.randint(1950, 2017))
    end_year = factory.LazyAttribute(lambda x: x.begin_year + random.randint(1, 8))
    average_runtime = factory.LazyFunction(lambda: random.randint(20, 70))
    # director # لازم نیست بنویسم. چون فارین کی هست خودش درست میکنه.
    country = factory.Faker("country")
    plot = factory.Faker('paragraph', nb_sentences=5, variable_nb_sentences=True)
    # poster # عکس ها اختیاری بودن. نذاشتم که سنگین نشه.
    rating = factory.LazyFunction(lambda: random.randint(0, 9) + random.randint(0, 10)/10)
    # start_release_date # اختیاری بود. نذاشتم که خالی باشه.
    # end_release_date # اختیاری بود. نذاشتم که خالی باشه.
    # genre # تو فایل ستاپ فیک دیتا مقدار دادم.
    # cast # تو فایل ستاپ فیک دیتا مقدار دادم.


class MusicFactory(DjangoModelFactory):
    class Meta:
        model = models.Music
    
    title = factory.LazyAttribute(lambda x: ' '.join([x.capitalize() for x in faker.words(3)]))
    year = factory.LazyFunction(lambda: random.randint(1920, 2024))
    duration = factory.LazyFunction(lambda: random.randint(60, 3600))
    # main_singer # لازم نیست بنویسم. چون فارین کی هست خودش درست میکنه.
    # file # فایل های صوتی اختیاری بودن. نذاشتم که سنگین نشه.
    lyrics = factory.Faker('paragraph', nb_sentences=8, variable_nb_sentences=True)
    # poster # عکس ها اختیاری بودن. نذاشتم که سنگین نشه.
    # release_date # اختیاری بود. نذاشتم که خالی باشه.
    # genre # تو فایل ستاپ فیک دیتا مقدار دادم.
    # other_singers # تو فایل ستاپ فیک دیتا مقدار دادم.


# این رو کلا تعریف هم نکنیم مشکلی پیش نمیاد. نوشتم که اگه یه وقت خواستیم بدونیم این سه تا فیلد رو داره.
class ImageFactory(DjangoModelFactory):
    class Meta:
        model = models.Image

    # image # عکس های اینجا اجباری بودن. نذاشتم که دیتابیس سنگین نشه.
    # movie # بدون عکس نمیشه این ۲ تا رو گذاشت.
    # serial # بدون عکس نمیشه این ۲ تا رو گذاشت.