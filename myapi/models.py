from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class GenreMovie(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class GenreMusic(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Artist(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nick_name = models.CharField(max_length=256, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.nick_name != "":
            return self.nick_name
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    STATUS_IN_DEVELOPMENT = 'develope'  # 8 characters
    STATUS_PRE_PRODUCTION = 'pre'       # 3 characters
    STATUS_FILMING = 'filming'          # 7 characters
    STATUS_POST_PRODUCTION = 'post'     # 4 characters
    STATUS_RELEASED = 'released'        # 8 characters
    # The maximum characters of different STATUS is 8 characters
    STATUS_MOVIES = (
        (STATUS_IN_DEVELOPMENT  , 'In development'),
        (STATUS_PRE_PRODUCTION  , 'Pre production'),
        (STATUS_FILMING         , 'Filming'),
        (STATUS_POST_PRODUCTION , 'Post production'),
        (STATUS_RELEASED        , 'Released'),
    )
    title = models.CharField(max_length=256)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1920), MaxValueValidator(2030)])
    runtime = models.PositiveIntegerField() # in minutes
    status = models.CharField(max_length=8, choices=STATUS_MOVIES, default=STATUS_RELEASED)
    director = models.ForeignKey(to=Artist, on_delete=models.PROTECT, related_name='movies_directed')
    country = models.CharField(max_length=64, blank=True)
    plot = models.TextField(blank=True)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMovie, blank=True, related_name='movies')
    cast = models.ManyToManyField(to=Artist, blank=True, related_name='movies')
    datetime_created = models.DateTimeField(auto_now_add=True, null=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})"


class Serial(models.Model):
    title = models.CharField(max_length=256)
    number_of_seasons = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    number_of_episodes = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    begin_year = models.PositiveIntegerField(validators=[MinValueValidator(1920)])
    end_year = models.PositiveIntegerField(validators=[MinValueValidator(1920)], blank=True, null=True)
    average_runtime = models.PositiveIntegerField() # in minutes
    director = models.ForeignKey(to=Artist, on_delete=models.PROTECT, related_name='series_directed')
    country = models.CharField(max_length=64, blank=True)
    plot = models.TextField(blank=True)
    poster = models.ImageField(upload_to='serial_posters/', blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    start_release_date = models.DateField(blank=True, null=True)
    end_release_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMovie, blank=True, related_name='series')
    cast = models.ManyToManyField(to=Artist, blank=True, related_name='series')
    datetime_created = models.DateTimeField(auto_now_add=True, null=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        if self.end_year is None:
            return f"{self.title} ({self.begin_year})"
        return f"{self.title} ({self.begin_year}-{self.end_year})"


class Music(models.Model):
    title = models.CharField(max_length=256)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2025)])
    duration = models.PositiveIntegerField() # in seconds
    main_singer = models.ForeignKey(to=Artist, on_delete=models.PROTECT, related_name='main_musics')
    file= models.FileField(upload_to='music/', blank=True, null=True)
    lyrics = models.TextField(blank=True)
    poster = models.ImageField(upload_to='music_posters/', blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMusic, blank=True, related_name='musics')
    other_singers = models.ManyToManyField(to=Artist, blank=True, related_name='musics')
    datetime_created = models.DateTimeField(auto_now_add=True, null=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.title} {self.main_singer} {self.year}"


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    serial = models.ForeignKey(to=Serial, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    
    def clean(self):
        super().clean()
        if self.movie in [None, ''] and self.serial in [None, '']:
            raise ValidationError("You should choose a Movie or a Serial!\nBoth can't be Null!")
        elif self.movie not in [None, ''] and self.serial not in [None, '']:
            raise ValidationError("You should choose exactly a Movie or a Serial!\nYou can't choose an image for both of them!")
        
    def __str__(self):
        if self.movie not in [None, '']:
            return f"A picture of {self.movie}"
        return f"A picture of {self.serial}"


class Staff(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True, unique=True)

    def __str__(self):
        temp = f"{self.user.username}"
        if self.user.first_name.strip()!='' or self.user.last_name.strip()!='':
            temp += f" (Name: {self.user.first_name.strip()} {self.user.last_name.strip()})"
        return temp

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(to=Staff, on_delete=models.SET_NULL, related_name='comments', blank=True, null=True)
    text = models.TextField()
    is_active = models.BooleanField(default=False)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    serial = models.ForeignKey(to=Serial, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    music = models.ForeignKey(to=Music, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    
    def clean(self):
        super().clean()
        if self.movie in [None, ''] and self.serial in [None, ''] and self.music in [None, '']:
            raise ValidationError("You should choose exactly a Movie, Serial or Music!\nAll of them can't be Null!")
        elif self.movie not in [None, ''] and self.serial not in [None, ''] and self.music not in [None, '']:
            raise ValidationError("You should choose exactly a Movie, Serial or Music!\nYou can't write a comment for all of them!")
        elif (self.movie in [None, ''] and self.serial not in [None, ''] and self.music not in [None, '']) or \
            (self.movie not in [None, ''] and self.serial in [None, ''] and self.music not in [None, '']) or \
            (self.movie not in [None, ''] and self.serial not in [None, ''] and self.music in [None, '']):
            raise ValidationError("You should choose exactly a Movie, Serial or Music!\nYou can't write a comment for two of them!")
        if self.user == None:
            raise ValidationError("You should choose Who has commented!")
        
    def __str__(self):
        if self.user == None:
            return 'Ananymous User'
        if self.user.full_name.strip() not in [None, '']:
            temp = self.user.full_name.strip()
        else:
            temp = self.user.phone_number
        temp += f": {self.text[:30]}"
        if len(self.text)>30:
            temp += '...'
        return temp