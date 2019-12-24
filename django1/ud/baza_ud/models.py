from django.db import models
from django.contrib.auth.models import User
from django.db.models import F



class Position(models.Model):
    name = models.CharField(max_length=20, null=True, verbose_name='Название должности')
    salary =  models.PositiveIntegerField(verbose_name='Оклад')
    description = models.TextField(null=True, verbose_name='Описание')
    duties = models.TextField(null=True, verbose_name='Обязанности')

    class Meta:
        verbose_name =  'Должность'
        verbose_name_plural = 'Должности'
    
    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(max_length=20, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, null=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    pasport_data = models.CharField(max_length=11, null=True, verbose_name='Паспортные данные')
    address = models.CharField(max_length=100, null=True, verbose_name='Адрес')
    phone_num = models.CharField(max_length=12, null=True, verbose_name='Телефон')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Должность')
    active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:     
        verbose_name =  'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def __str__(self):
        return self.get_full_name()
    
class Place(models.Model):
    name = models.CharField(max_length=20, null=True, verbose_name='Название')
    address = models.CharField(max_length=200, null=True, verbose_name='Адрес')
    capacity = models.PositiveIntegerField(verbose_name='Вместимость')
    cost = models.PositiveIntegerField(verbose_name='Стоимость аренды')

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'

    def __str__(self):
        return self.name

class Artist(models.Model):
    first_name = models.CharField(max_length=20, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=20, null=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    nickname = models.CharField(max_length=20, null=True, verbose_name='Творческий псевдоним')
    pasport_data = models.CharField(max_length=11, null=True, verbose_name='Паспортные данные')
    cost = models.PositiveIntegerField(verbose_name='Стоимость')
    rider = models.TextField(null=True, verbose_name='Райдер')
    active = models.BooleanField(default=True, verbose_name='Активен')

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'

    def __str__(self):
        return self.nickname


class Concert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name = 'админ концерта')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Артист')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Площадка')
    description = models.TextField(null=True, verbose_name='Описание')
    date = models.DateField(null=True, verbose_name='Дата')
    time = models.TimeField(null =True, verbose_name='Время')
    ticket = models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'Ссылка на покупку билета')
    # ticket_amount = models.OneToOneField(Place, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Количество билетов')

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'
    
    def get_concert_name(self):
        return f'{self.artist}  {self.date}'

    def __str__(self):
        return self.get_concert_name()

        
class Ad_Agency(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Название')
    concert_agency_staff = models.ManyToManyField('Staff', verbose_name='Ответственный сотрудник концертного агенства')

    class Meta:
        verbose_name = 'Рекламаное агенство'
        verbose_name_plural = 'Рекламные агенства'
    
    def __str__(self):
        return self.name

class Ad_Type(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name='Тип рекламы')
    description = models.TextField(null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Вид рекламы'
        verbose_name_plural = 'Виды рекламы'

    def __str__(self):
        return self.name


class Ad(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Концерт')
    ad_agency = models.ForeignKey(Ad_Agency, on_delete=models.CASCADE, blank=True, verbose_name='Рекламное агенство')
    ad_type = models.ForeignKey(Ad_Type, on_delete=models.CASCADE, blank=True, verbose_name='Вид рекламы')
    cost = models.PositiveIntegerField(verbose_name='Стоимость')
    description = models.TextField(null=True, verbose_name='Описание')
    amount = models.CharField(max_length=200, null=True, verbose_name='Количество')

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'

    def get_ad_name(self):
        return f'{self.concert}  {self.ad_type}'

    def __str__(self):
        return self.get_ad_name()

    
