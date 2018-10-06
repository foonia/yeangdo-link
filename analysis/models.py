from django.db import models


class SurveyModel(models.Model):
    SEX_CHOICES = (
        ('m', '남자'),
        ('w', '여자'),
    )
    ADDRESS_CHOICES = (
        ('1', '남항동'),
        ('2', '영선제1동'),
        ('3', '영선제2동'),
        ('4', '신선동'),
        ('5', '봉래제1동'),
        ('6', '봉래제2동'),
        ('7', '청학제1동'),
        ('8', '청학제2동'),
        ('9', '동삼제1동'),
        ('10', '동삼제2동'),
        ('11', '동삼제3동'),
    )
    FINAL_EDUCATION_CHOICES = (
        ('e', '초등학교 졸업'),
        ('m', '중학교 졸업'),
        ('h', '고등학교 졸업'),
        ('u', '대학교 졸업'),
    )

    name = models.CharField(max_length=128)
    birth_date = models.DateField()
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default='m',
    )
    address = models.CharField(
        max_length=2,
        choices=ADDRESS_CHOICES,
        default='1',
    )
    address_detail = models.CharField(max_length=256)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(null=True, blank=True)
    final_education = models.CharField(
        max_length=1,
        choices=FINAL_EDUCATION_CHOICES,
        default='e',
    )
    former_occupation = models.CharField(max_length=128, blank=True)
    desired_occupation1 = models.CharField(max_length=128)
    desired_occupation2 = models.CharField(max_length=128, blank=True)
    desired_occupation3 = models.CharField(max_length=128, blank=True)
    desired_Salary = models.PositiveIntegerField(null=True, blank=True)
    etc = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

