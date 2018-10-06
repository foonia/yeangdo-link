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

    name = models.CharField(max_length=128, verbose_name='이름')
    birth_date = models.DateField(verbose_name='생일')
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default='m',
        verbose_name='성별',
    )
    address = models.CharField(
        max_length=2,
        choices=ADDRESS_CHOICES,
        default='1',
        verbose_name='주소(행정구역)',
    )
    address_detail = models.CharField(max_length=256, verbose_name='상세주소')
    phone = models.CharField(max_length=20, blank=True, verbose_name='전화번호')
    email = models.EmailField(null=True, blank=True, verbose_name='이메일')
    final_education = models.CharField(
        max_length=1,
        choices=FINAL_EDUCATION_CHOICES,
        default='e',
        verbose_name='최종학력',
    )
    former_occupation = models.CharField(max_length=128, blank=True, verbose_name='이전직업')
    desired_occupation1 = models.CharField(max_length=128, verbose_name='1.희망직업(필수)')
    desired_occupation2 = models.CharField(max_length=128, blank=True, verbose_name='2.희망직업')
    desired_occupation3 = models.CharField(max_length=128, blank=True, verbose_name='3.희망직업')
    desired_Salary = models.PositiveIntegerField(null=True, blank=True, verbose_name='희망월급')
    etc = models.TextField(blank=True, verbose_name='기타사항')
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated = models.DateTimeField(auto_now=True, verbose_name='수정일')

