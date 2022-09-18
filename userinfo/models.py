from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# User Information Model
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_%(class)ss')
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT,  related_name='updated_%(class)ss', null=True, blank=True)


class UserInfo(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    about_me = models.CharField(max_length=250)
    banner_image = models.URLField(max_length=350)
    footer_image = models.URLField(max_length=350)
    facebook_id = models.URLField(max_length=200)
    linked_id = models.URLField(max_length=200)
    github_id = models.URLField(max_length=200)
    cv_link = models.URLField(max_length=350)


class Services(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_service')
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=350)

class Portfolio(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_portfolio')
    project_name = models.CharField(max_length=150)
    project_img = models.URLField(max_length=350)
    preview_link = models.URLField(max_length=350)
    github_link = models.URLField(max_length=350)


class Education(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_education')
    degree_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    institute = models.CharField(max_length=250)
    start_year = models.IntegerField()
    passing_year = models.IntegerField()
    short_brief = models.TextField(max_length=350)


class ProfessionalSkills(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_skill')
    skill_logo = models.URLField(max_length=250)
    skill_name = models.CharField(max_length=100)


class Experince(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_experience')
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    join_year = models.IntegerField()
    resign_year = models.IntegerField()
    responsibility = models.TextField(max_length=350)
    company_logo = models.URLField(max_length=250)


class ClientFeedback(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_feedback')
    client_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    client_photo = models.URLField(max_length=350)

    job_title = models.CharField(max_length=250)
    market_place = models.CharField(max_length=150)
    contract_start = models.DateField()
    contract_end = models.DateField()
    rating = models.FloatField()
    feedback = models.TextField(max_length=350)


class ContactRequest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_request')
    name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=350)



