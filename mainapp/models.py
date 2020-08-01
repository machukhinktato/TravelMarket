from django.db import models


class ListOfCountries(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Regions(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название проживания', max_length=128, unique=True)
    image = models.ImageField(upload_to='accommodation_img', blank=True)
    short_desc = models.TextField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    room_desc = models.TextField(verbose_name='краткое описание комнаты', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(
        verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    availability = models.PositiveIntegerField(verbose_name='количество свободных номеров')
    is_active = models.BooleanField(verbose_name='активна', default=True)

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by('country', 'regions', 'name')

    def __str__(self):
        return f'{self.name} ({self.country.name})'


# class Bookings(models.Model):
#     hotel = models.ForeignKey(Accommodation, on_delete=models.CASCADE, default='')
#     date = models.DateField()  # date of booking
#     # room = models.ForeignKey(Room, on_delete=models.CASCADE)  # room which we are trying to book
#     client_name = models.CharField(max_length=100)
#     client_email = models.CharField(max_length=100)  # client's email
#     phone_number = models.CharField(max_length=20,  verbose_name="Client's phone number")
#     time = models.CharField(max_length=50, choices=arrival_time,
#                             default='12:00')  # approximate time of check in
#     comments = models.CharField(max_length=500)  # client's requests
#     country = models.CharField(max_length=50, choices=country_dict,
#                                default='Russia')
#     address = models.CharField(max_length=100)  # client's address of living
#
#     def __str__(self):
#         return 'Room Booking {} - {}'.format(self.room.name, self.room.hotel.name)
