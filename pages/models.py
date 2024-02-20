from django.db import models
from django.utils.text import slugify
# Create your models here.
COUNTRY_CHOICES = (
    ('af','Afghanistan'),
    ('ax','Aland Islands'),
    ('al','Albania'),
    ('dz','Algeria'),
    ('as','American Samoa'),
    ('ad','Andorra'),
    ('ao','Angola'),
    ('ai','Anguilla'),
    ('aq','Antarctica'),
    ('ag','Antigua and Barbuda'),
    ('ar','Argentina'),
    ('am','Armenia'),
    ('aw','Aruba'),
    ('au','Australia'),
    ('at','Austria'),
    ('az','Azerbaijan'),
    ('bs','Bahamas'),
    ('bh','Bahrain'),
    ('bd','Bangladesh'),
    ('bb','Barbados'),
    ('by','Belarus'),
    ('be','Belgium'),
    ('bz','Belize'),
    ('bj','Benin'),
    ('bm','Bermuda'),
    ('bt','Bhutan'),
    ('bo','Bolivia, Plurinational State of'),
    ('bq','Bonaire, Sint Eustatius and Saba'),
    ('ba','Bosnia and Herzegovina'),
    ('bw','Botswana'),
    ('bv','Bouvet Island'),
    ('br','Brazil'),
    ('io','British Indian Ocean Territory'),
    ('bn','Brunei Darussalam'),
    ('bg','Bulgaria'),
    ('bf','Burkina Faso'),
    ('bi','Burundi'),
    ('kh','Cambodia'),
    ('cm','Cameroon'),
    ('ca','Canada'),
    ('cv','Cape Verde'),
    ('ky','Cayman Islands'),
    ('cf','Central African Republic'),
    ('td','Chad'),
    ('cl','Chile'),
    ('cn','China'),
    ('cx','Christmas Island'),
    ('cc','Cocos (Keeling) Islands'),
    ('co','Colombia'),
    ('km','Comoros'),
    ('cg','Congo'),
    ('cd','Congo, The Democratic Republic of the'),
    ('ck','Cook Islands'),
    ('cr','Costa Rica'),
    ('ci','Côte dIvoire'),
    ('hr','Croatia'),
    ('cu','Cuba'),
    ('cw','Curaçao'),
    ('cy','Cyprus'),
    ('cz','Czech Republic'),
    ('dk','Denmark'),
    ('dj','Djibouti'),
    ('dm','Dominica'),
    ('do','Dominican Republic'),
    ('ec','Ecuador'),
    ('eg','Egypt'),
    ('sv','El Salvador'),
    ('gq','Equatorial Guinea'),
    ('er','Eritrea'),
    ('ee','Estonia'),
    ('et','Ethiopia'),
    ('fk','Falkland Islands (Malvinas)'),
    ('fo','Faroe Islands'),
    ('fj','Fiji'),
    ('fi','Finland'),
    ('fr','France'),
    ('gf','French Guiana'),
    ('pf','French Polynesia'),
    ('tf','French Southern Territories'),
    ('ga','Gabon'),
    ('gm','Gambia'),
    ('ge','Georgia'),
    ('de','Germany'),
    ('gh','Ghana'),
    ('gi','Gibraltar'),
    ('gr','Greece'),
    ('gl','Greenland'),
    ('gd','Grenada'),
    ('gp','Guadeloupe'),
    ('gu','Guam'),
    ('gt','Guatemala'),
    ('gg','Guernsey'),
    ('gn','Guinea'),
    ('gw','Guinea-Bissau'),
    ('gy','Guyana'),
    ('ht','Haiti'),
    ('hm','Heard Island and McDonald Islands'),
    ('va','Holy See (Vatican City State)'),
    ('hn','Honduras'),
    ('hk','Hong Kong'),
    ('hu','Hungary'),
    ('is','Iceland'),
    ('in','India'),
    ('id','Indonesia'),
    ('ir','Iran, Islamic Republic of'),
    ('iq','Iraq'),
    ('ie','Ireland'),
    ('im','Isle of Man'),
    ('il','Israel'),
    ('it','Italy'),
    ('jm','Jamaica'),
    ('jp','Japan'),
    ('je','Jersey'),
    ('jo','Jordan'),
    ('kz','Kazakhstan'),
    ('ke','Kenya'),
    ('ki','Kiribati'),
    ('kp','Korea, Democratic Peoples Republic of'),
    ('kr','Korea, Republic of'),
    ('kw','Kuwait'),
    ('kg','Kyrgyzstan'),
    ('la','Lao Peoples Democratic Republic'),
    ('lv','Latvia'),
    ('lb','Lebanon'),
    ('ls','Lesotho'),
    ('lr','Liberia'),
    ('ly','Libya'),
    ('li','Liechtenstein'),
    ('lt','Lithuania'),
    ('lu','Luxembourg'),
    ('mo','Macao'),
    ('mk','Macedonia, Republic of'),
    ('mg','Madagascar'),
    ('mw','Malawi'),
    ('my','Malaysia'),
    ('mv','Maldives'),
    ('ml','Mali'),
    ('mt','Malta'),
    ('mh','Marshall Islands'),
    ('mq','Martinique'),
    ('mr','Mauritania'),
    ('mu','Mauritius'),
    ('yt','Mayotte'),
    ('mx','Mexico'),
    ('fm','Micronesia, Federated States of'),
    ('md','Moldova, Republic of'),
    ('mc','Monaco'),
    ('mn','Mongolia'),
    ('me','Montenegro'),
    ('ms','Montserrat'),
    ('ma','Morocco'),
    ('mz','Mozambique'),
    ('mm','Myanmar'),
    ('na','Namibia'),
    ('nr','Nauru'),
    ('np','Nepal'),
    ('nl','Netherlands'),
    ('nc','New Caledonia'),
    ('nz','New Zealand'),
    ('ni','Nicaragua'),
    ('ne','Niger'),
    ('ng','Nigeria'),
    ('nu','Niue'),
    ('nf','Norfolk Island'),
    ('mp','Northern Mariana Islands'),
    ('no','Norway'),
    ('om','Oman'),
    ('pk','Pakistan'),
    ('pw','Palau'),
    ('ps','Palestinian Territory, Occupied'),
    ('pa','Panama'),
    ('pg','Papua New Guinea'),
    ('py','Paraguay'),
    ('pe','Peru'),
    ('ph','Philippines'),
    ('pn','Pitcairn'),
    ('pl','Poland'),
    ('pt','Portugal'),
    ('pr','Puerto Rico'),
    ('qa','Qatar'),
    ('re','Réunion'),
    ('ro','Romania'),
    ('ru','Russian Federation'),
    ('rw','Rwanda'),
    ('bl','Saint Barthélemy'),
    ('sh','Saint Helena, Ascension and Tristan da Cunha'),
    ('kn','Saint Kitts and Nevis'),
    ('lc','Saint Lucia'),
    ('mf','Saint Martin (French part)'),
    ('pm','Saint Pierre and Miquelon'),
    ('vc','Saint Vincent and the Grenadines'),
    ('ws','Samoa'),
    ('sm','San Marino'),
    ('st','Sao Tome and Principe'),
    ('sa','Saudi Arabia'),
    ('sn','Senegal'),
    ('rs','Serbia'),
    ('sc','Seychelles'),
    ('sl','Sierra Leone'),
    ('sg','Singapore'),
    ('sx','Sint Maarten (Dutch part)'),
    ('sk','Slovakia'),
    ('si','Slovenia'),
    ('sb','Solomon Islands'),
    ('so','Somalia'),
    ('za','South Africa'),
    ('gs','South Georgia and the South Sandwich Islands'),
    ('es','Spain'),
    ('lk','Sri Lanka'),
    ('sd','Sudan'),
    ('sr','Suriname'),
    ('ss','South Sudan'),
    ('sj','Svalbard and Jan Mayen'),
    ('sz','Swaziland'),
    ('se','Sweden'),
    ('ch','Switzerland'),
    ('sy','Syrian Arab Republic'),
    ('tw','Taiwan, Province of China'),
    ('tj','Tajikistan'),
    ('tz','Tanzania, United Republic of'),
    ('th','Thailand'),
    ('tl','Timor-Leste'),
    ('tg','Togo'),
    ('tk','Tokelau'),
    ('to','Tonga'),
    ('tt','Trinidad and Tobago'),
    ('tn','Tunisia'),
    ('tr','Turkey'),
    ('tm','Turkmenistan'),
    ('tc','Turks and Caicos Islands'),
    ('tv','Tuvalu'),
    ('ug','Uganda'),
    ('ua','Ukraine'),
    ('ae','United Arab Emirates'),
    ('gb','United Kingdom'),
    ('us','United States'),
    ('um','United States Minor Outlying Islands'),
    ('uy','Uruguay'),
    ('uz','Uzbekistan'),
    ('vu','Vanuatu'),
    ('ve','Venezuela, Bolivarian Republic of'),
    ('vn','Viet Nam'),
    ('vg','Virgin Islands, British'),
    ('vi','Virgin Islands, U.S.'),
    ('wf','Wallis and Futuna'),
    ('eh','Western Sahara'),
    ('ye','Yemen'),
    ('zm','Zambia'),
    ('zw','Zimbabwe')
)

OFFER_TYPES = (
        ('alim', 'Alım Teklifi'),
        ('satis', 'Satış Teklifi'),
    )

BORON_TYPES = (
        ('added', 'added'),
        ('not_added', 'not_added'),
    )


class Company(models.Model):
    
    name = models.CharField(max_length=50)
    address = models.TextField()
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES, default='tr')
    city = models.CharField(max_length=50)
    field_of_activity = models.CharField(max_length=50)
    slug = models.SlugField(default="",null=False)
    web_site = models.CharField(max_length=50)
    sub_company = models.TextField()
    base_customer = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)

    def get_country_display_name(self):
        for code, name in COUNTRY_CHOICES:
            if code == self.country:
                return name
        return None 


class Product(models.Model):
    description = models.CharField(max_length=255, verbose_name="DESCRIPTION")
    quality = models.CharField(max_length=50, verbose_name="QUALITY")
    size = models.CharField(max_length=20, verbose_name="SIZE (mm)")
    color = models.CharField(max_length=20, verbose_name="COLOR (Ral)")
    paint = models.CharField(max_length=10, verbose_name="PAINT(μm)")
    zinc = models.CharField(max_length=10, verbose_name="ZINC(g/sm)")
    gloss = models.CharField(max_length=10, verbose_name="Gloss")
    coil_weight = models.CharField(max_length=10, verbose_name="Coil Weight")
    boron = models.CharField(max_length=50, choices=BORON_TYPES, default='added')
    coil_id = models.CharField(max_length=10, verbose_name="Coil ID")
    # unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="UNIT PRICE (usd/ton)")
    # quantity = models.PositiveIntegerField(verbose_name="Quantity (ton)")

    def __str__(self):
        return self.description
    
    def line_total(self):
        return self.quantity * self.unit_price

class Offer(models.Model):
    OFFER_TYPES = (
        ('alim', 'Alım Teklifi'),
        ('satis', 'Satış Teklifi'),
    )

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    offer_type = models.CharField(max_length=10, choices=OFFER_TYPES)
    products = models.ManyToManyField(Product, through='OfferProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # def update_total_value(self):
    #     total_value = sum(op.product.unit_price * op.quantity for op in self.offerproduct_set.all())
    #     self.total_value = total_value
    #     self.save()

    # def save(self, *args, **kwargs):
    #     self.update_total_value()
    #     super().save(*args, **kwargs)

    # def total_product_prices(self):
    #     total_price = sum(op.line_total() for op in self.offerproduct_set.all())
    #     return total_price

    def __str__(self):
        return f"{self.offer_type} - {self.id}- {self.company.name}"    
    

class OfferProduct(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    offer_product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (usd/ton)")
    destination = models.CharField(max_length=50, verbose_name="Destination")


    def __str__(self):
        return f"{self.product.description} - {self.offer.offer_type} - {self.offer.id}"
    
    # def update_value(self):
    #     self.line_total = self.product.unit_price * self.quantity
    #     self.save()
    #     self.offer.update_total_value()  
        
    
    
    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.offer_product_price
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.line_total = self.line_total()  # Güncel line_total hesaplaması
    #     super().save(*args, **kwargs)



