from django.db import models
from django.core.validators import RegexValidator

class Genders (models.Model):
    class Meta:
        db_table = 'tbl_genders'

    gender_id = models.BigAutoField(primary_key=True, blank=False) # gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) # gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

class Users (models.Model):
    class Meta:
        db_table = 'tbl_users'

    user_id = models.BigAutoField(primary_key=True, blank=False) # user_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    full_name = models.CharField(max_length=55, blank=False) # full_name VARCHAR(255) NOT NULL
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE) # gender_id BIGINT NOT NULL // FOREIGN KEY (gender_id) REFERENCES tbl_genders(gender_id) ON DELETE CASCADE
    birth_date = models.DateField(blank=False) # birth_date DATE NOT NULL
    address = models.CharField(max_length=255, blank=False) # address VARCHAR(255) NOT NULL
    contact_number = models.CharField(max_length=11, blank=False, validators=[RegexValidator(regex=r'^\d{11}$')]) # contact_number VARCHAR(20) NOT NULL   
    email = models.EmailField(max_length=255, blank=False) # email VARCHAR(255) DEFAULT NULL
    username = models.CharField(max_length=255, blank=False, unique=True) # username VARCHAR(255) NOT NULL UNIQUE
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    password = models.CharField(max_length=255, blank=False) # password VARCHAR(255) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

