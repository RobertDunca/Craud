from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # photo = models.ImageField(upload_to='images/')
    user_is_organiser = models.BooleanField(default=False)
    website_url = models.CharField(max_length=225, null=True, blank=True)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    long = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Restaurant(models.Model):
    restaurant_options = (('fd', 'Fine Dining'), ('cd', 'Casual Dining'), ('cc', 'Contemporary Casual'),
                          ('fs', 'Family Style'), ('fc', 'Fast Casual'), ('ff', 'Fast Food'), ('c', 'Cafe'),
                          ('b', 'Buffet'), ('ft', 'Food Truck'))

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=6, choices=restaurant_options)
    description = models.TextField()
    # photo = models.ImageField(upload_to='images/')
    website_url = models.CharField(max_length=225, null=True, blank=True)
    contact_num = models.CharField(max_length=20)
    address = models.CharField(max_length=50, null=True, blank=True)
    long = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class ThingToDo(models.Model):
    category_options = (('entertainment', 'Entertainment'), ('cinema', 'Cinema'), ('sport', 'Sport'),
                        ('attractions', 'Attractions'), ('museums', 'Museums'),
                        ('shopping', 'Shopping'), ('other', 'Other'))

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=13, choices=category_options)
    description = models.TextField()
    # photo = models.ImageField(upload_to='images/')
    website_url = models.CharField(max_length=225, null=True, blank=True)
    contact_num = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    long = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
