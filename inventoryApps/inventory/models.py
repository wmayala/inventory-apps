from django.db import models

# Create your models here.
status = (
    ('1', 'Activo'),
    ('0', 'Inactivo'),
)

type_dev = (
    ('1', 'Desarrollador'),
    ('2', 'Soporte'),
)

type_admin = (
        ('1', 'Principal'),
        ('2', 'Suplente'),
)

class Developers(models.Model):
    dev_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    type = models.CharField(max_length = 1, choices = type_dev, default = '1')
    status = models.CharField(max_length = 1, default = '1')
    created_at = models.DateTimeField('created_at', auto_now_add = True)
    updated_at = models.DateTimeField('updated_at', auto_now = True)
    
    def __str__(self):
        return self.developers
    
    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'
        ordering = ['name']

class Admins(models.Model):    
    admin_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    type = models.CharField(max_length = 1, choices = type_admin, default = '1')
    status = models.CharField(max_length = 1, default = '1')
    created_at = models.DateTimeField('created_at', auto_now_add = True)
    updated_at = models.DateTimeField('updated_at', auto_now = True)
    
    def __str__(self):
        return self.admins
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        ordering = ['name']

class Units(models.Model):
    unit_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    status = models.CharField(max_length = 1, default = '1')
    created_at = models.DateTimeField('created_at', auto_now_add = True)
    updated_at = models.DateTimeField('updated_at', auto_now = True)
    
    def __str__(self):
        return self.units
    
    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        ordering = ['name']
    
class Applications(models.Model):
    app_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 125)
    description = models.CharField(max_length = 255)
    lang_back = models.CharField(max_length = 125)
    lang_front = models.CharField(max_length = 125)
    dev_site = models.CharField(max_length = 125)
    prod_site = models.CharField(max_length = 125)
    doc_site = models.CharField(max_length = 125)
    server = models.CharField(max_length = 125)
    pub_date = models.DateField()
    status = models.CharField(max_length = 1, choices = status, default = '1')
    created_at = models.DateTimeField('created_at', auto_now_add = True)
    updated_at = models.DateTimeField('updated_at', auto_now = True)
    
    developer = models.ForeignKey(Developers, on_delete = models.CASCADE)
    admin = models.ForeignKey(Admins, on_delete = models.CASCADE)
    unit = models.ForeignKey(Units, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.applications
    
    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'
        ordering = ['name']
        

        
