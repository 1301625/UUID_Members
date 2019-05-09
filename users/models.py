
# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
#from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import UserManager as AuthUserManager
import uuid
# Create your models here.

from django.conf import settings

class UserManager(AuthUserManager):
    use_in_migrations=True
    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError('이메일 입력 오류')
        email = self.normalize_email(email)
        user =self.model(email=email , **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)     #스태프권한
        extra_fields.setdefault('is_superuser',False) #슈퍼유저권환
        return super()._create_user(email,password, **extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('슈퍼유저는 staff권한을 가져야합니다')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('슈퍼유저는 슈퍼유저권한을 가져야합니다')
        return super()._create_user(email,password, **extra_fields)


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)
    email = models.EmailField(_('email address'),unique=True)
    nick_name = models.CharField(_('nick_name'),max_length=150,blank=True)
    username= models.CharField(max_length=40,unique=False,default='')

    is_staff= models.BooleanField(
        _('staff_status'),
        default=False,
        help_text=_('사용자가 이 관리 사이트에 로그인 할 수 있는지 여부를 지정합니다.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('이 사용자를 활성 상태로 처리해야하는지 여부를 지정합니다'
        '계정을 삭제하는 대신이 항목을 선택 해제하십시오'
        ),
    )

    object=UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name= '%s'%(self.nick_name)
        return full_name.strip() #strip :공백 지우기

    def get_short_name(self):
        return self.nick_name


#프로필 생성
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    profile_website_url= models.URLField(blank=True , null=True)
    profile_blog = models.URLField(blank=True , null=True)
    profile_birthday = models.DateField(blank=True, null=True)

    profile_image = models.ImageField(blank=True, upload_to='user_image', null=True)
    #profile_image = models.ImageField(blank=True, upload_to='user_image/%Y/%m/%d')


