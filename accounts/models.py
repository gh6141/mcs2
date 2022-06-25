from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Shokugyo(models.Model):
    shokugyo = models.CharField('職業', max_length=128)                                    
    def __str__(self):
        return self.shokugyo

class Shumi(models.Model):
    shumi = models.CharField('趣味', max_length=128)                                    
    def __str__(self):
        return self.shumi

class Nenrei(models.Model):
    nenrei = models.CharField('年齢', max_length=40)                                    
    def __str__(self):
        return self.nenrei

class Kenmei(models.Model):
    kenmei = models.CharField('県名', max_length=20)                                    
    def __str__(self):
        return self.kenmei

class Seibetu(models.Model):
    seibetu = models.CharField('性別', max_length=10)                                    
    def __str__(self):
        return self.seibetu

class Tabako(models.Model):
    tabako = models.CharField('たばこ', max_length=40)                                    
    def __str__(self):
        return self.tabako

class Osake(models.Model):
    osake = models.CharField('お酒', max_length=40)                                    
    def __str__(self):
        return self.osake

class Kekkonreki(models.Model):
    kekkonreki = models.CharField('結婚歴', max_length=20)                                    
    def __str__(self):
        return self.kekkonreki

class Kodomo(models.Model):
    kodomo = models.CharField('子供', max_length=20)                                    
    def __str__(self):
        return self.kodomo


class User(AbstractBaseUser,PermissionsMixin):
    username_validator=ASCIIUsernameValidator()
    username=models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists.")
        },
    )
    nickname_validator=ASCIIUsernameValidator()
    nickname=models.CharField(
        _('nickname'),
        max_length=150,
        unique=True,
        validators=[nickname_validator],
        error_messages={
            'unique': _("A user with that nickname already exists.")
        },
    )
    email=models.EmailField(_('email address'),blank=False)
    nenrei = models.ForeignKey( Nenrei,verbose_name="年齢",on_delete=models.PROTECT)
    shussin = models.ForeignKey( Kenmei,verbose_name="出身",on_delete=models.PROTECT)
    kyojuchi = models.ForeignKey( Kenmei,verbose_name="居住地",on_delete=models.PROTECT)
    shokugyo = models.ForeignKey( Shokugyo,verbose_name="職業",on_delete=models.PROTECT)
    shumi = models.ForeignKey( Shumi,verbose_name="趣味",on_delete=models.PROTECT)

    self_introduction=models.CharField(_('self introduction'),max_length=512,blank=True)
    doi_flg=models.BooleanField(
        _('accept'),
        default=False,
    )


    profile_photo1=models.ImageField(_('profile photo1'),upload_to='profile_photos1',
    null=True,blank=True)
    profile_photo2=models.ImageField(_('profile photo2'),upload_to='profile_photos2',
    null=True,blank=True)
    profile_photo3=models.ImageField(_('profile photo3'),upload_to='profile_photos3',
    null=True,blank=True)
    profile_photo4=models.ImageField(_('profile photo4'),upload_to='profile_photos4',
    null=True,blank=True)
    profile_photo5=models.ImageField(_('profile photo5'),upload_to='profile_photos5',
    null=True,blank=True)

    tabako = models.ForeignKey( Tabako,verbose_name="たばこ",on_delete=models.PROTECT)
    osake = models.ForeignKey( Osake,verbose_name="お酒",on_delete=models.PROTECT)
    kekkonreki = models.ForeignKey( Kekkonreki,verbose_name="結婚歴",on_delete=models.PROTECT)
    kodomo = models.ForeignKey( Kodomo,verbose_name="子供",on_delete=models.PROTECT)

    """
ユーザー名
ニックネーム
Email（プロフィールには入れない）
年齢　20歳から79歳まで 選択肢
性別
出身　～県　選択肢
居住地　県名　選択肢
職種　
＊営業
事務・管理
企画・マーケティング・経営・管理職
サービス・販売・外食
理美容・エステ・ネイル関係
Web・インターネット・ゲーム
クリエイティブ（メディア・アパレル・デザイン）
専門職（コンサルタント・士業・金融・不動産）
ITエンジニア（システム開発・SE・インフラ）
エンジニア（機械・電気・電子・半導体・制御）
素材・化学・食品・医薬品技術職
建築・土木技術職
技能工・設備・交通・運輸
医療・福祉・介護
教育・保育・公務員・農林水産・その他

趣味（選択肢）
好きなこと・メッセージ欄

利用規約とプライバシーポリシーに同意 チェック
プロフィール画像を入れる5枚
タバコ：すう、もともとすわない、禁煙している
お酒：のむ（毎日、週数回程度、月数回程度）、のまない
結婚歴：未婚、死別、離婚
子供：　なし　同居中　別居中


"""


    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined=models.DateTimeField(_('date joined'),default=timezone.now)

    objects=UserManager()

    EMAIL_FIELD='email'
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    class Meta:
        verbose_name=_('user')
        verbose_name_plural=_('users')
        db_table='users'
        swappable='AUTH_USER_MODEL'

    def clean(self):
        super().clean()
        self.email=self.__class__.objects.normalize_email(self.email)

    def email_user(self,subject,message,from_email=None,**kwargs):
        send_mail(subject,message,from_email,[self.email],**kwargs)


