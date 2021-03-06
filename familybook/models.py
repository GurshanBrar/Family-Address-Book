from django.db import models
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
COUNTRIES = (
        ('AD', _('Andorra')),
        ('AE', _('United Arab Emirates')),
        ('AF', _('Afghanistan')),
        ('AG', _('Antigua & Barbuda')),
        ('AI', _('Anguilla')),
        ('AL', _('Albania')),
        ('AM', _('Armenia')),
        ('AN', _('Netherlands Antilles')),
        ('AO', _('Angola')),
        ('AQ', _('Antarctica')),
        ('AR', _('Argentina')),
        ('AS', _('American Samoa')),
        ('AT', _('Austria')),
        ('AU', _('Australia')),
        ('AW', _('Aruba')),
        ('AZ', _('Azerbaijan')),
        ('BA', _('Bosnia and Herzegovina')),
        ('BB', _('Barbados')),
        ('BD', _('Bangladesh')),
        ('BE', _('Belgium')),
        ('BF', _('Burkina Faso')),
        ('BG', _('Bulgaria')),
        ('BH', _('Bahrain')),
        ('BI', _('Burundi')),
        ('BJ', _('Benin')),
        ('BM', _('Bermuda')),
        ('BN', _('Brunei Darussalam')),
        ('BO', _('Bolivia')),
        ('BR', _('Brazil')),
        ('BS', _('Bahama')),
        ('BT', _('Bhutan')),
        ('BV', _('Bouvet Island')),
        ('BW', _('Botswana')),
        ('BY', _('Belarus')),
        ('BZ', _('Belize')),
        ('CA', _('Canada')),
        ('CC', _('Cocos (Keeling) Islands')),
        ('CF', _('Central African Republic')),
        ('CG', _('Congo')),
        ('CH', _('Switzerland')),
        ('CI', _('Ivory Coast')),
        ('CK', _('Cook Iislands')),
        ('CL', _('Chile')),
        ('CM', _('Cameroon')),
        ('CN', _('China')),
        ('CO', _('Colombia')),
        ('CR', _('Costa Rica')),
        ('CU', _('Cuba')),
        ('CV', _('Cape Verde')),
        ('CX', _('Christmas Island')),
        ('CY', _('Cyprus')),
        ('CZ', _('Czech Republic')),
        ('DE', _('Germany')),
        ('DJ', _('Djibouti')),
        ('DK', _('Denmark')),
        ('DM', _('Dominica')),
        ('DO', _('Dominican Republic')),
        ('DZ', _('Algeria')),
        ('EC', _('Ecuador')),
        ('EE', _('Estonia')),
        ('EG', _('Egypt')),
        ('EH', _('Western Sahara')),
        ('ER', _('Eritrea')),
        ('ES', _('Spain')),
        ('ET', _('Ethiopia')),
        ('FI', _('Finland')),
        ('FJ', _('Fiji')),
        ('FK', _('Falkland Islands (Malvinas)')),
        ('FM', _('Micronesia')),
        ('FO', _('Faroe Islands')),
        ('FR', _('France')),
        ('FX', _('France, Metropolitan')),
        ('GA', _('Gabon')),
        ('GB', _('United Kingdom (Great Britain)')),
        ('GD', _('Grenada')),
        ('GE', _('Georgia')),
        ('GF', _('French Guiana')),
        ('GH', _('Ghana')),
        ('GI', _('Gibraltar')),
        ('GL', _('Greenland')),
        ('GM', _('Gambia')),
        ('GN', _('Guinea')),
        ('GP', _('Guadeloupe')),
        ('GQ', _('Equatorial Guinea')),
        ('GR', _('Greece')),
        ('GS', _('South Georgia and the South Sandwich Islands')),
        ('GT', _('Guatemala')),
        ('GU', _('Guam')),
        ('GW', _('Guinea-Bissau')),
        ('GY', _('Guyana')),
        ('HK', _('Hong Kong')),
        ('HM', _('Heard & McDonald Islands')),
        ('HN', _('Honduras')),
        ('HR', _('Croatia')),
        ('HT', _('Haiti')),
        ('HU', _('Hungary')),
        ('ID', _('Indonesia')),
        ('IE', _('Ireland')),
        ('IL', _('Israel')),
        ('IN', _('India')),
        ('IO', _('British Indian Ocean Territory')),
        ('IQ', _('Iraq')),
        ('IR', _('Islamic Republic of Iran')),
        ('IS', _('Iceland')),
        ('IT', _('Italy')),
        ('JM', _('Jamaica')),
        ('JO', _('Jordan')),
        ('JP', _('Japan')),
        ('KE', _('Kenya')),
        ('KG', _('Kyrgyzstan')),
        ('KH', _('Cambodia')),
        ('KI', _('Kiribati')),
        ('KM', _('Comoros')),
        ('KN', _('St. Kitts and Nevis')),
        ('KP', _('Korea, Democratic People\'s Republic of')),
        ('KR', _('Korea, Republic of')),
        ('KW', _('Kuwait')),
        ('KY', _('Cayman Islands')),
        ('KZ', _('Kazakhstan')),
        ('LA', _('Lao People\'s Democratic Republic')),
        ('LB', _('Lebanon')),
        ('LC', _('Saint Lucia')),
        ('LI', _('Liechtenstein')),
        ('LK', _('Sri Lanka')),
        ('LR', _('Liberia')),
        ('LS', _('Lesotho')),
        ('LT', _('Lithuania')),
        ('LU', _('Luxembourg')),
        ('LV', _('Latvia')),
        ('LY', _('Libyan Arab Jamahiriya')),
        ('MA', _('Morocco')),
        ('MC', _('Monaco')),
        ('MD', _('Moldova, Republic of')),
        ('MG', _('Madagascar')),
        ('MH', _('Marshall Islands')),
        ('ML', _('Mali')),
        ('MN', _('Mongolia')),
        ('MM', _('Myanmar')),
        ('MO', _('Macau')),
        ('MP', _('Northern Mariana Islands')),
        ('MQ', _('Martinique')),
        ('MR', _('Mauritania')),
        ('MS', _('Monserrat')),
        ('MT', _('Malta')),
        ('MU', _('Mauritius')),
        ('MV', _('Maldives')),
        ('MW', _('Malawi')),
        ('MX', _('Mexico')),
        ('MY', _('Malaysia')),
        ('MZ', _('Mozambique')),
        ('NA', _('Namibia')),
        ('NC', _('New Caledonia')),
        ('NE', _('Niger')),
        ('NF', _('Norfolk Island')),
        ('NG', _('Nigeria')),
        ('NI', _('Nicaragua')),
        ('NL', _('Netherlands')),
        ('NO', _('Norway')),
        ('NP', _('Nepal')),
        ('NR', _('Nauru')),
        ('NU', _('Niue')),
        ('NZ', _('New Zealand')),
        ('OM', _('Oman')),
        ('PA', _('Panama')),
        ('PE', _('Peru')),
        ('PF', _('French Polynesia')),
        ('PG', _('Papua New Guinea')),
        ('PH', _('Philippines')),
        ('PK', _('Pakistan')),
        ('PL', _('Poland')),
        ('PM', _('St. Pierre & Miquelon')),
        ('PN', _('Pitcairn')),
        ('PR', _('Puerto Rico')),
        ('PT', _('Portugal')),
        ('PW', _('Palau')),
        ('PY', _('Paraguay')),
        ('QA', _('Qatar')),
        ('RE', _('Reunion')),
        ('RO', _('Romania')),
        ('RU', _('Russian Federation')),
        ('RW', _('Rwanda')),
        ('SA', _('Saudi Arabia')),
        ('SB', _('Solomon Islands')),
        ('SC', _('Seychelles')),
        ('SD', _('Sudan')),
        ('SE', _('Sweden')),
        ('SG', _('Singapore')),
        ('SH', _('St. Helena')),
        ('SI', _('Slovenia')),
        ('SJ', _('Svalbard & Jan Mayen Islands')),
        ('SK', _('Slovakia')),
        ('SL', _('Sierra Leone')),
        ('SM', _('San Marino')),
        ('SN', _('Senegal')),
        ('SO', _('Somalia')),
        ('SR', _('Suriname')),
        ('ST', _('Sao Tome & Principe')),
        ('SV', _('El Salvador')),
        ('SY', _('Syrian Arab Republic')),
        ('SZ', _('Swaziland')),
        ('TC', _('Turks & Caicos Islands')),
        ('TD', _('Chad')),
        ('TF', _('French Southern Territories')),
        ('TG', _('Togo')),
        ('TH', _('Thailand')),
        ('TJ', _('Tajikistan')),
        ('TK', _('Tokelau')),
        ('TM', _('Turkmenistan')),
        ('TN', _('Tunisia')),
        ('TO', _('Tonga')),
        ('TP', _('East Timor')),
        ('TR', _('Turkey')),
        ('TT', _('Trinidad & Tobago')),
        ('TV', _('Tuvalu')),
        ('TW', _('Taiwan, Province of China')),
        ('TZ', _('Tanzania, United Republic of')),
        ('UA', _('Ukraine')),
        ('UG', _('Uganda')),
        ('UM', _('United States Minor Outlying Islands')),
        ('US', _('United States of America')),
        ('UY', _('Uruguay')),
        ('UZ', _('Uzbekistan')),
        ('VA', _('Vatican City State (Holy See)')),
        ('VC', _('St. Vincent & the Grenadines')),
        ('VE', _('Venezuela')),
        ('VG', _('British Virgin Islands')),
        ('VI', _('United States Virgin Islands')),
        ('VN', _('Viet Nam')),
        ('VU', _('Vanuatu')),
        ('WF', _('Wallis & Futuna Islands')),
        ('WS', _('Samoa')),
        ('YE', _('Yemen')),
        ('YT', _('Mayotte')),
        ('YU', _('Yugoslavia')),
        ('ZA', _('South Africa')),
        ('ZM', _('Zambia')),
        ('ZR', _('Zaire')),
        ('ZW', _('Zimbabwe')),
        ('ZZ', _('Unknown or unspecified country')),
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='images/', default='images/blank_profile_pic.png')
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField()
    street_address = models.CharField(
        max_length=100, help_text='Street address following house number')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5, verbose_name="Zip Code")
    country = models.CharField(max_length=2, choices=COUNTRIES)
    phone_number = models.CharField(max_length=16, verbose_name="Phone Number")

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_address(self):
        return f"{self.street_address}, {self.city} {self.state}, {self.zip_code}"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('profile-detail')

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='images/', default='images/blank_profile_pic.png')
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    email = models.EmailField()
    street_address = models.CharField(
        max_length=100, help_text='Street address following house number')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5, verbose_name="Zip Code")
    country = models.CharField(max_length=2, choices=COUNTRIES)
    phone_number = models.CharField(max_length=16, verbose_name="Phone Number")

    def get_absolute_url(self):
        return reverse('entry-detail', args=[str(self.id)])

    def get_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_address(self):
        return f'{self.street_address}, {self.city} {self.state}, {self.zip_code}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name', 'first_name']
