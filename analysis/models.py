from django.db import models

class Survey(models.Model):
    SEX_CHOICES = (
        ('남', '남'),
        ('여', '여'),
    )
    ADDRESS_CHOICES = (
        ('남항동', '남항동'),
        ('영선제1동', '영선제1동'),
        ('영선제2동', '영선제2동'),
        ('영선제3동', '영선제3동'),
        ('영선제4동', '영선제4동'),
        ('대평동', '대평동'),
        ('신선동', '신선동'),
        ('봉래동', '봉래동'),
        ('청학동', '청학동'),
        ('동삼동', '동삼동'),
        ('대교', '대교'),
    )
    FINAL_EDUCATION_CHOICES = (
        ('무학', '무학'),
        ('초등학교 졸업', '초등학교 졸업'),
        ('중학교 졸업', '중학교 졸업'),
        ('고등학교 졸업', '고등학교 졸업'),
        ('대학교 졸업', '대학교 졸업'),
        ('대학교 석사', '대학교 석사'),
        ('대학교 박사', '대학교 박사'),
    )

    name = models.CharField(max_length=128, verbose_name='이름')
    age = models.CharField(max_length=8, verbose_name='나이')
    sex = models.CharField(
        max_length=10,
        blank=True,
        choices=SEX_CHOICES,
        default='남',
        verbose_name='성별',
    )
    address = models.CharField(
        max_length=10,
        blank=True,
        choices=ADDRESS_CHOICES,
        default='남항동',
        verbose_name='주소(행정구역)',
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name='전화번호')
    email = models.EmailField(null=True, blank=True, verbose_name='이메일')
    final_education = models.CharField(
        max_length=10,
        blank=True,
        choices=FINAL_EDUCATION_CHOICES,
        default='무학',
        verbose_name='최종학력',
    )
    former_occupation = models.CharField(max_length=128, blank=True, verbose_name='이전직업')
    desired_occupation1 = models.CharField(max_length=128, verbose_name='1.희망직업(필수)')
    desired_occupation2 = models.CharField(max_length=128, blank=True, verbose_name='2.희망직업')
    desired_occupation3 = models.CharField(max_length=128, blank=True, verbose_name='3.희망직업')
    desired_salary = models.PositiveIntegerField(null=True, blank=True, verbose_name='희망월급')
    etc = models.TextField(blank=True, verbose_name='기타사항')
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated = models.DateTimeField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return self.name



# class Survey(models.Model):
#     SEX_CHOICES = (
#         ('m', '남'),
#         ('w', '여'),
#     )
#     ADDRESS_CHOICES = (
#         ('1', '남항동'),
#         ('2', '영선제1동'),
#         ('3', '영선제2동'),
#         ('4', '영선제3동'),
#         ('5', '영선제4동'),
#         ('6', '대평동'),
#         ('7', '신선동'),
#         ('8', '봉래동'),
#         ('9', '청학동'),
#         ('10', '동삼동'),
#         ('11', '대교'),
#     )
#     FINAL_EDUCATION_CHOICES = (
#         ('1', '무학'),
#         ('2', '초등학교 졸업'),
#         ('3', '중학교 졸업'),
#         ('4', '고등학교 졸업'),
#         ('5', '대학교 졸업'),
#         ('6', '대학교 석사'),
#         ('7', '대학교 박사'),
#     )
#
#     name = models.CharField(max_length=128, verbose_name='이름')
#     age = models.CharField(max_length=8, verbose_name='나이')
#     sex = models.CharField(
#         max_length=1,
#         blank=True,
#         choices=SEX_CHOICES,
#         default='m',
#         verbose_name='성별',
#     )
#     address = models.CharField(
#         max_length=2,
#         blank=True,
#         choices=ADDRESS_CHOICES,
#         default='0',
#         verbose_name='주소(행정구역)',
#     )
#     phone = models.CharField(max_length=20, blank=True, verbose_name='전화번호')
#     email = models.EmailField(null=True, blank=True, verbose_name='이메일')
#     final_education = models.CharField(
#         max_length=1,
#         blank=True,
#         choices=FINAL_EDUCATION_CHOICES,
#         default='e',
#         verbose_name='최종학력',
#     )
#     former_occupation = models.CharField(max_length=128, blank=True, verbose_name='이전직업')
#     desired_occupation1 = models.CharField(max_length=128, verbose_name='1.희망직업(필수)')
#     desired_occupation2 = models.CharField(max_length=128, blank=True, verbose_name='2.희망직업')
#     desired_occupation3 = models.CharField(max_length=128, blank=True, verbose_name='3.희망직업')
#     desired_salary = models.PositiveIntegerField(null=True, blank=True, verbose_name='희망월급')
#     etc = models.TextField(blank=True, verbose_name='기타사항')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
#     updated = models.DateTimeField(auto_now=True, verbose_name='수정일')
#
#     def __str__(self):
#         return self.name
#
#
#
