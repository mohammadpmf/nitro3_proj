from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


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
    release_date = models.DateTimeField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMovie, blank=True, related_name='movies')
    cast = models.ManyToManyField(to=Artist, blank=True, related_name='movies')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

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
    start_release_date = models.DateTimeField(blank=True, null=True)
    end_release_date = models.DateTimeField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMovie, blank=True, related_name='series')
    cast = models.ManyToManyField(to=Artist, blank=True, related_name='series')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

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
    release_date = models.DateTimeField(blank=True, null=True)
    genre = models.ManyToManyField(to=GenreMusic, blank=True, related_name='musics')
    other_singers = models.ManyToManyField(to=Artist, blank=True, related_name='musics')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

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


##################################################################################### v1 which is canceled #####################################################################################
# class Tag(models.Model):
#     name = models.CharField(max_length=64)

# class Photo(models.Model):
#     IMAGE_FORMAT_CHOICES = (
#         ('jpg', 'jpg'),
#         ('jpeg', 'jpeg'),
#         ('gif', 'gif'),
#         ('ico', 'ico'),
#         ('bmp', 'bmp'),
#         ('png', 'png'),
#         ('tiff', 'tiff'),
#         ('webp', 'webp'),
#         ('svg', 'svg'),
#         ('tga', 'tga'),
#         ('wbmp', 'wbmp'),
#         ('other', 'other'),
#     )

#     title = models.CharField(max_length=64)
#     image = models.ImageField(upload_to='photos/')
#     views = models.PositiveIntegerField(default=0)
#     datetime_created = models.DateTimeField(auto_now_add=True)
#     dimension = models.CharField(max_length=64)
#     width = models.PositiveIntegerField()
#     height = models.PositiveIntegerField()
#     image_format = models.CharField(max_length=8, choices=IMAGE_FORMAT_CHOICES)
#     tags = models.ManyToManyField("app.Model")


# class Video(models.Model):
#     VIDEO_FORMAT_CHOICES = (
#         ('mp4', 'mp4'),
#         ('mkv', 'mkv'),
#         ('flv', 'flv'),
#         ('mov', 'mov'),
#         ('avi', 'avi'),
#         ('mpg', 'mpg'),
#         ('ogv', 'ogv'),
#         ('webm', 'webm'),
#         ('wmv', 'wmv'),
#         ('3gp', '3gp'),
#         ('other', 'other'),
#     )

#     title = models.CharField(max_length=64)
#     image = models.ImageField(upload_to='photos/')
#     video= models.FileField(upload_to='videos/')
#     views = models.PositiveIntegerField(default=0)
#     datetime_created = models.DateTimeField(auto_now_add=True)
#     resolution = models.CharField(max_length=64)
#     width = models.PositiveIntegerField()
#     height = models.PositiveIntegerField()
#     video_format = models.CharField(max_length=8, choices=VIDEO_FORMAT_CHOICES)
#     duration = models.TimeField()
#     tags = models.ManyToManyField("app.Model")
#     # frame_rate = models.PositiveIntegerField()


# class Music(models.Model):
#     MUSIC_FORMAT_CHOICES = (
#         ('mp3', 'mp3'),
#         ('wav', 'wav'),
#         ('wma', 'wma'),
#         ('ogg', 'ogg'),
#         ('m4a', 'm4a'),
#         ('aac', 'aac'),
#         ('other', 'other'),
#     )

#     title = models.CharField(max_length=64)
#     image = models.ImageField(upload_to='photos/')
#     file= models.FileField(upload_to='music/')
#     views = models.PositiveIntegerField(default=0)
#     datetime_created = models.DateTimeField(auto_now_add=True)
#     music_format = models.CharField(max_length=8, choices=MUSIC_FORMAT_CHOICES)
#     duration = models.TimeField()
#     tags = models.ManyToManyField("app.Model")
#     bit_rate = models.PositiveIntegerField()
