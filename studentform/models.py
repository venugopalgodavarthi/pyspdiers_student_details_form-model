from django.db import models

# Create your models here.

class form(models.Model):
    full_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    dob=models.DateField()
    phone=models.BigIntegerField()
    email=models.EmailField()
    ten_th=models.CharField(max_length=20)
    puc=models.CharField(max_length=20)
    diploma=models.CharField(max_length=15)
    aggregate_12=models.FloatField()
    aggregate_diploma=models.FloatField()
    yop_12=models.IntegerField()
    yop_diploma=models.IntegerField()
    diploma_college=models.CharField(max_length=50)
    diploma_branch=models.CharField(max_length=50)
    diploma_branch_other=models.CharField(max_length=50)
    degree=models.CharField(max_length=10)
    degree_branch=models.CharField(max_length=20)
    degree_branch_other=models.CharField(max_length=50)
    agreegate_degree=models.FloatField()
    degree_yop=models.DateField()
    uni_name=models.CharField(max_length=50)
    usn=models.CharField(max_length=30)
    clg_name=models.CharField(max_length=50)
    place_clg=models.CharField(max_length=50)
    backlog=models.CharField(max_length=5)
    current_backlog=models.CharField(max_length=5)
    gap_in_degree=models.CharField(max_length=5)
    master=models.CharField(max_length=10)
    master_qualification=models.CharField(max_length=20)
    master_degree=models.CharField(max_length=20)
    other_master_degree=models.CharField(max_length=20)
    aggrigate_master=models.IntegerField()
    master_yop=models.DateField()
    master_uni_name=models.CharField(max_length=50)
    master_usn=models.CharField(max_length=50)
    master_clg_name=models.CharField(max_length=50)
    Master_clg_place=models.CharField(max_length=30)
    master_fail_clear=models.CharField(max_length=10)
    master_existing_backlog=models.CharField(max_length=5)
    year_gap_master=models.CharField(max_length=5)
    certificate=models.CharField(max_length=30)
    ready_to_relocate=models.CharField(max_length=5)
    Location=models.CharField(max_length=150)
    you_have_passport=models.CharField(max_length=10)
    you_have_pancard=models.CharField(max_length=10)
    you_have_adharcard=models.CharField(max_length=10)
    aadhar_no=models.BigIntegerField()
    father_name=models.CharField(max_length=30)
    house_no=models.CharField(max_length=30)
    street_no=models.CharField(max_length=30)
    area_name=models.CharField(max_length=30)
    pincode=models.IntegerField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    
    
    
    
