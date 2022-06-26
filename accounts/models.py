from lib2to3.pgen2.token import SEMI
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import datetime

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力して下さい')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=Trueである必要があります。')
        return self._create_user(username, email, password, **extra_fields)


    """
Email（プロフィールには入れない）
年齢　20歳から79歳まで 選択肢

好きなこと・メッセージ欄

利用規約とプライバシーポリシーに同意 チェック
プロフィール画像を入れる5枚

"""
SEX=(('male','男性'),('female','女性'))
SHUMI=(('supotu','スポーツ（観覧も含む）'),('geijutu','美術・演劇・映画・音楽等鑑賞'),('ongaku','楽器演奏・カラオケ・ダンス等'),('shodo','書道・華道・茶道等'),('shugei','和裁・洋裁・手芸等'),('ryori','料理・菓子作り'),('engei','園芸・ガーデニング・畑'),('sosaku','日曜大工・絵画・彫刻・陶芸等'),('shasin','写真撮影'),('bungei','詩・和歌・俳句・小説'),('dokusho','読書'),('game','囲碁・将棋・ゲーム等'),('kengaku','動植物園・水族館等見学'),('camp','キャンプ'),('other','その他'))
SGYO=(('eigyo','営業'),('','事務・管理'),('kikaku','企画・マーケティング・経営・管理職'),('sabisu','サービス・販売・外食'),('ribiyo','理美容・エステ・ネイル関係'),('web','Web・インターネット・ゲーム'),
     ('creative','クリエイティブ（メディア・アパレル・デザイン）'),('senmonshoku','専門職（コンサルタント・士業・金融・不動産）'),('it','ITエンジニア（システム開発・SE・インフラ）'),
     ('enjinia','エンジニア（機械・電気・電子・半導体・制御）'),('sozai','素材・化学・食品・医薬品技術職'),('kenchiku','建築・土木技術職'),('ginoko','技能工・設備・交通・運輸'),('iryo','医療・福祉・介護'),
     ('sonota','教育・保育・公務員・農林水産・その他'))
KMEI=(('hokkaido','北海道'),('aomori','青森県'),('iwate','岩手県'),('miyagi','宮城県'),('akita','秋田県'),('yamagata','山形県'),('hukusima','福島県'),('ibaraki','茨城県'),('tochigi','栃木県'),('gunma','群馬県'),
      ('saitama','埼玉県'),('chiba','千葉県'),('tokyo','東京都'),('kanagawa','神奈川県'),('niigata','新潟県'),('toyama','富山県'),('isikawa','石川県'),('hukui','福井県'),('yamanasi','山梨県'),('nagano','長野県'),
      ('gihu','岐阜県'),('sizuoka','静岡県'),('aichi','愛知県'),('mie','三重県'),('siga','滋賀県'),('kyoto','京都府'),('osaka','大阪府'),('hyogo','兵庫県'),('nara','奈良県'),('wakayama','和歌山県'),
      ('tottori','鳥取県'),('simane','島根県'),('okayama','岡山県'),('hirosima','広島県'),('yamaguchi','山口県'),('tokusima','徳島県'),('kagawa','香川県'),('ehime','愛媛県'),('kochi','高知県'),('hukuoka','福岡県'),
      ('saga','佐賀県'),('nagasaki','長崎県('),('kumamoto','熊本県'),('ooita','大分県'),('miyazaki','宮崎県'),('kagosima','鹿児島県'),('okinawa','沖縄県'))
TBAKO=(('suu','吸う'),('motomoto','もともと吸わない'),('kinen','禁煙している'))
OSAKE=(('mainichi','毎日飲む'),('shuichi','週数回程度飲む'),('tukiichi','月数回程度飲む'),('nomanai','飲まない'))
KREKI=(('mikon','未婚'),('sibetu','死別'),('rikon','離婚'))
KDOMO=(('nasi','なし'),('dokyo','同居中'),('bekkyo','別居中'))

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
    sex=models.CharField(_('seibetu'),max_length=10,choices=SEX,blank=True)
    nenrei = models.CharField(_('nenrei'),max_length=40,blank=True)
    date_of_birth = models.DateField(_('dateofbirth'), default=datetime.date.today)
    shussin = models.CharField(_('shussin'),max_length=40,choices=KMEI,blank=True)
    kyojuchi = models.CharField(_('kyojuchi'),max_length=40,choices=KMEI,blank=True)
    shokugyo = models.CharField(_('shokugyo'),max_length=40,choices=SGYO,blank=True)
    shumi = models.CharField(_('shumi'),max_length=40,choices=SHUMI,blank=True)

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

    tabako = models.CharField(_('tabako'),max_length=40,choices=TBAKO,blank=True)
    osake = models.CharField(_('osake'),max_length=40,choices=OSAKE,blank=True)

    kekkonreki = models.CharField(_('kekkonreki'),max_length=40,choices=KREKI,blank=True)
    kodomo = models.CharField(_('kodomo'),max_length=40,choices=KDOMO,blank=True)




    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined=models.DateTimeField(_('date joined'),default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

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


