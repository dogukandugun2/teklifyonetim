from django.shortcuts import render,redirect
from .models import Company,Offer,OfferProduct,Product
from django.http import JsonResponse
import random
from django.contrib.admin.models import LogEntry
from collections import defaultdict
from .models import Company, COUNTRY_CHOICES
from django.contrib.auth.decorators import login_required

global_country_names = ['Andorra', 'French Southern and Antarctic Lands', 'Laos', 'Canada', 'Nigeria', 'Vanuatu', 'Czechia', 'Malawi', 'Mali', 'Iceland', 'Norway', 'Saint Vincent and the Grenadines', 'Guadeloupe', 'Chile', 'Bermuda', 'Kuwait', 'Dominica', 'Montenegro', 'United States Virgin Islands', 'Cameroon', 'Sri Lanka', 'China', 'Bangladesh', 'Sweden', 'Grenada', 'Turkey', 'Guinea', 'Tanzania', 'Rwanda', 'Singapore', 'Morocco', 'Saint Barthélemy', 'Iraq', 'Brunei', 'Isle of Man', 'North Korea', 'Iran', 'Curaçao', 'Paraguay', 'Albania', 'Tajikistan', 'Bolivia', 'Austria', 'Saint Kitts and Nevis', 'United States Minor Outlying Islands', 'Colombia', 'Kosovo', 'Belize', 'Guinea-Bissau', 'Marshall Islands', 'Myanmar', 'French Polynesia', 'Brazil', 'Croatia', 'Somalia', 'Afghanistan', 'Anguilla', 'Cook Islands', 'Western Sahara', 'New Zealand', 'Eritrea', 'Cambodia', 'Bahamas', 'Belarus', 'Norfolk Island', 'Tuvalu', 'South Georgia', 'Mauritania', 'New Caledonia', 'Bulgaria', 'Mozambique', 'Niue', 'Estonia', 'Italy', 'Malta', 'Slovenia', 'India', 'Peru', 'Burundi', 'Lithuania', 'United States', 'Honduras', 'Tonga', 'Saudi Arabia', 'Suriname', 'Qatar', 'Saint Helena, Ascension and Tristan da Cunha', 'Gibraltar', 'Northern Mariana Islands', 'Mauritius', 'Barbados', 'Réunion', 'British Indian Ocean Territory', 'Syria', 'Egypt', 'São Tomé and Príncipe', 'Kiribati', 'Timor-Leste', 'Lesotho', 'Solomon Islands', 'Libya', 'South Korea', 'Liechtenstein', 'Nicaragua', 'Ecuador', 'Maldives', 'Algeria', 'Kyrgyzstan', 'Finland', 'Antarctica', 'Kenya', 'Cuba', 'Montserrat', 'Poland', 'Åland Islands', 'Ethiopia', 'Togo', 'Bosnia and Herzegovina', 'Uruguay', 'Guam', 'Cape Verde', 'Chad', 'Vatican City', 'Palau', 'Haiti', 'Yemen', 'Eswatini', 'Zimbabwe', 'Greece', 'Israel', 'Saint Martin', 'Antigua and Barbuda', 'Cyprus', 'Sint Maarten', 'Monaco', 'Fiji', 'Ukraine', 'Martinique', 'Hong Kong', 'Portugal', 'Bhutan', 'Nepal', 'France', 'Ireland', 'United Arab Emirates', 'Guernsey', 'Saint Lucia', 'Dominican Republic', 'Serbia', 'Botswana', 'Ivory Coast', 'Ghana', 'Comoros', 'Azerbaijan', 'United Kingdom', 'Central African Republic', 'Palestine', 'Caribbean Netherlands', 'Taiwan', 'Pitcairn Islands', 'San Marino', 'Svalbard and Jan Mayen', 'Djibouti', 'Wallis and Futuna', 'Denmark', 'Papua New Guinea', 'Madagascar', 'Bouvet Island', 'Hungary', 'Tokelau', 'Trinidad and Tobago', 'Gambia', 'Luxembourg', 'Cocos (Keeling) Islands', 'Republic of the Congo', 'Argentina', 'DR Congo', 'Greenland', 'Jordan', 'Belgium', 'Switzerland', 'Indonesia', 'Lebanon', 'Malaysia', 'Cayman Islands', 'Slovakia', 'Armenia', 'Christmas Island', 'Mongolia', 'Saint Pierre and Miquelon', 'Japan', 'South Africa', 'Philippines', 'Micronesia', 'Germany', 'Latvia', 'Jamaica', 'Macau', 'Nauru', 'Faroe Islands', 'Guyana', 'Burkina Faso', 'Sudan', 'Russia', 'Mayotte', 'Australia', 'Liberia', 'Mexico', 'Tunisia', 'Aruba', 'Kazakhstan', 'Oman', 'French Guiana', 'Niger', 'Turkmenistan', 'Sierra Leone', 'Samoa', 'Senegal', 'Georgia', 'Namibia', 'South Sudan', 'Thailand', 'Bahrain', 'Heard Island and McDonald Islands', 'Falkland Islands', 'Jersey', 'Vietnam', 'Guatemala', 'Moldova', 'North Macedonia', 'Uzbekistan', 'Romania', 'Uganda', 'El Salvador', 'Zambia', 'Gabon', 'Equatorial Guinea', 'Spain', 'Netherlands', 'British Virgin Islands', 'Benin', 'Pakistan', 'Panama', 'Turks and Caicos Islands', 'Angola', 'American Samoa', 'Venezuela', 'Costa Rica', 'Puerto Rico', 'Seychelles']
global_coordinate = [[42.5, 1.5], [-49.25, 69.167], [18.0, 105.0], [60.0, -95.0], [10.0, 8.0], [-16.0, 167.0], [49.75, 15.5], [-13.5, 34.0], [17.0, -4.0], [65.0, -18.0], [62.0, 10.0], [13.25, -61.2], [16.25, -61.583333], [-30.0, -71.0], [32.33333333, -64.75], [29.5, 45.75], [15.41666666, -61.33333333], [42.5, 19.3], [18.35, -64.933333], [6.0, 12.0], [7.0, 81.0], [35.0, 105.0], [24.0, 90.0], [62.0, 15.0], [12.11666666, -61.66666666], [39.0, 35.0], [11.0, -10.0], [-6.0, 35.0], [-2.0, 30.0], [1.36666666, 103.8], [32.0, -5.0], [18.5, -63.41666666], [33.0, 44.0], [4.5, 114.66666666], [54.25, -4.5], [40.0, 127.0], [32.0, 53.0], [12.116667, -68.933333], [-23.0, -58.0], [41.0, 20.0], [39.0, 71.0], [-17.0, -65.0], [47.33333333, 13.33333333], [17.33333333, -62.75], [19.3, 166.633333], [4.0, -72.0], [42.666667, 21.166667], [17.25, -88.75], [12.0, -15.0], [9.0, 168.0], [22.0, 98.0], [17.6797, 149.4068], [-10.0, -55.0], [45.16666666, 15.5], [10.0, 49.0], [33.0, 65.0], [18.25, -63.16666666], [-21.23333333, -159.76666666], [24.5, -13.0], [-41.0, 174.0], [15.0, 39.0], [13.0, 105.0], [25.0343, -77.3963], [53.0, 28.0], [-29.03333333, 167.95], [-8.0, 178.0], [-54.5, -37.0], [20.0, -12.0], [-21.5, 165.5], [43.0, 25.0], [-18.25, 35.0], [-19.03333333, -169.86666666], [59.0, 26.0], [42.83333333, 12.83333333], [35.9375, 14.3754], [46.11666666, 14.81666666], [20.0, 77.0], [-10.0, -76.0], [-3.5, 30.0], [56.0, 24.0], [38.0, -97.0], [15.0, -86.5], [-20.0, -175.0], [25.0, 45.0], [4.0, -56.0], [25.5, 51.25], [-15.95, -5.72], [36.13333333, -5.35], [15.2, 145.75], [-20.28333333, 57.55], [13.16666666, -59.53333333], [-21.15, 
55.5], [-6.0, 71.5], [35.0, 38.0], [27.0, 30.0], [1.0, 7.0], [1.41666666, 173.0], [-8.83333333, 125.91666666], [-29.5, 28.5], [-8.0, 159.0], [25.0, 17.0], [37.0, 127.5], [47.26666666, 9.53333333], [13.0, -85.0], [-2.0, -77.5], [3.25, 73.0], [28.0, 3.0], [41.0, 75.0], [64.0, 26.0], [-90.0, 0.0], [1.0, 38.0], [21.5, -80.0], [16.75, -62.2], [52.0, 20.0], [60.116667, 19.9], [8.0, 38.0], [8.0, 1.16666666], [44.0, 18.0], [-33.0, -56.0], [13.46666666, 144.78333333], [16.5388, 23.0418], [15.0, 19.0], [41.9, 12.45], [7.5, 134.5], [19.0, -72.41666666], [15.0, 48.0], [-26.5, 31.5], [-20.0, 30.0], [39.0, 
22.0], [31.47, 35.13], [18.0708, 63.0501], [17.05, -61.8], [35.0, 33.0], [18.033333, -63.05], [43.73333333, 7.4], [17.7134, 178.065], [49.0, 32.0], [14.666667, -61.0], [22.267, 114.188], [39.5, -8.0], [27.5, 90.5], [28.0, 84.0], [46.0, 2.0], [53.0, -8.0], [24.0, 54.0], [49.46666666, -2.58333333], [13.88333333, -60.96666666], [19.0, -70.66666666], [44.0, 21.0], [-22.0, 24.0], [8.0, -5.0], [8.0, -2.0], [-12.16666666, 44.25], [40.5, 47.5], [54.0, -2.0], [7.0, 21.0], [31.9, 35.2], [12.18, -68.25], [23.5, 121.0], [-25.06666666, -130.1], [43.76666666, 12.41666666], [78.0, 20.0], [11.5, 43.0], [-13.3, -176.2], [56.0, 10.0], [-6.0, 147.0], [-20.0, 47.0], [54.4208, 3.3464], [47.0, 20.0], [-9.0, -172.0], [10.6918, -61.2225], [13.46666666, -16.56666666], [49.75, 6.16666666], [12.1642, 96.871], [-1.0, 15.0], [-34.0, -64.0], [0.0, 25.0], [72.0, -40.0], [31.0, 36.0], [50.83333333, 4.0], [47.0, 8.0], [-5.0, 120.0], [33.83333333, 35.83333333], [2.5, 112.5], [19.3133, -81.2546], [48.66666666, 19.5], [40.0, 45.0], [-10.5, 105.66666666], [46.0, 105.0], [46.83333333, -56.33333333], [36.0, 138.0], [-29.0, 24.0], [13.0, 122.0], [6.91666666, 158.25], [51.0, 9.0], [57.0, 25.0], [18.25, -77.5], [22.16666666, 113.55], [-0.53333333, 166.91666666], [62.0, -7.0], [5.0, -59.0], [13.0, -2.0], [15.0, 30.0], [60.0, 100.0], [-12.83333333, 45.16666666], [-27.0, 133.0], [6.5, -9.5], [23.0, -102.0], [34.0, 9.0], [12.5, -69.96666666], [48.0196, 66.9237], [21.0, 57.0], [4.0, -53.0], [16.0, 8.0], [40.0, 60.0], [8.5, -11.5], [-13.58333333, -172.33333333], [14.0, -14.0], [42.0, 43.5], [-22.0, 17.0], [7.0, 30.0], [15.0, 100.0], [26.0, 50.55], [53.0818, 73.5042], [-51.75, -59.0], [49.25, -2.16666666], [16.16666666, 107.83333333], [15.5, -90.25], [47.0, 29.0], [41.83333333, 22.0], [41.0, 64.0], [46.0, 25.0], [1.0, 32.0], [13.83333333, -88.91666666], [-15.0, 30.0], [-1.0, 11.75], [2.0, 10.0], [40.0, -4.0], [52.5, 5.75], [18.431383, -64.62305], [9.5, 2.25], [30.0, 70.0], [9.0, -80.0], [21.75, -71.58333333], [-12.5, 18.5], [-14.33333333, -170.0], [8.0, -66.0], [10.0, -84.0], [18.25, -66.5], [-4.58333333, 55.66666666]]

def get_coordinates(country_name):
    global global_country_names, global_coordinate
    
    try:
        # Verilen ülkenin indeksini bulma
        index = global_country_names.index(country_name)

        # İlgili indekse karşılık gelen koordinatları alma
        coordinates = global_coordinate[index]

        return coordinates
    except ValueError:
        # Eğer ülke ismi dizide bulunamazsa ValueError hatası alırız.
        return None




@login_required
def homepage(request):

    toplam_satis_sayisi = Offer.objects.filter(offer_type='satis').count()
    toplam_alis_sayisi = Offer.objects.filter(offer_type='alim').count()

    offer_logs = LogEntry.objects.filter(content_type__model='offer').order_by('-action_time')
    
    print("*****************************")
    
    for log in offer_logs:
        print(log)
        print(log.action_time)
       
    
    

    existing_factories = Company.objects.all()
    array_country_names = []
    array_country_coordinates = []

    for factory in existing_factories:
        # print("*******************************************")
        country_name = factory.get_country_display_name()
        array_country_names.append(country_name)
        array_country_coordinates.append(get_coordinates(country_name))
        
    print(array_country_coordinates)
    cauntry_zip = zip(array_country_names,array_country_coordinates)
    context = {
        'toplam_satis_sayisi': toplam_satis_sayisi,
        'toplam_alis_sayisi': toplam_alis_sayisi,
        'country_zip': cauntry_zip,
        'recent_actions': offer_logs,
    }

    return render(request,'index.html',context)

@login_required
def yenileme_endpoint(request):
    # Burada istediğiniz işlemleri gerçekleştirin ve yeni içeriği oluşturun
    celik_fiyat = "500,"
    celik_fiyat = celik_fiyat + str(random.randint(0,100))
    print(celik_fiyat)
    aliminyum_fiyat = "500,"
    aliminyum_fiyat = aliminyum_fiyat + str(random.randint(0,100))
    print(aliminyum_fiyat)
    

    return JsonResponse({'celik_fiyat': celik_fiyat,'aliminyum_fiyat':aliminyum_fiyat})

@login_required
def company(request):
    query = request.GET.get('q')

    if query:
        # Eğer bir arama sorgusu varsa, şirketleri isme göre filtrele
        companys = Company.objects.filter(name__icontains=query)
        
    else:
        # Eğer arama sorgusu yoksa, tüm şirketleri getir
        companys = Company.objects.all()
    
    offers = Offer.objects.all()

    print("-----------------------------------------------------")
    for offer in offers:
        print("asd")
        print(repr(offer.total_value))

    

    return render(request, 'company.html', {'companys': companys, 'query': query})

@login_required
def company_detail(request,desc):

    get_company_object = Company.objects.get(slug=desc)
    country_display_name = get_company_object.get_country_display_name()
    company_offers = Offer.objects.filter(company=get_company_object)
    print(get_company_object.name)


    return render(request, 'company_detail.html', {"get_company_object": get_company_object, "country_display_name": country_display_name,"company_offers":company_offers})

@login_required
def offer(request):
    companies = Company.objects.all()
    if request.method == 'POST':
        
        company_id = request.POST.get('company_id')  # Örneğin, company_id'nin formdan alındığını varsayalım
        offer_type = request.POST.get('offer_type')  # Örneğin, offer_type'ın formdan alındığını varsayalım

        # Şirket ve teklif tipine bağlı olarak yeni bir Offer oluştur
        company = Company.objects.get(id=company_id)
        new_offer = Offer.objects.create(company=company, offer_type=offer_type)
        # new_offer.update_total_value()
        print(company_id)
        print(offer_type)

        return redirect('offer')
    

    query = request.GET.get('q')
    offers = []
    offer_type = ""
    if query:
        if query=='alim':
            # Eğer bir arama sorgusu varsa, şirketleri isme göre filtrele
            offers = Offer.objects.filter(offer_type='alim').order_by('-id')
            offer_type='Alım'
        elif query == 'satis':
            # Eğer arama sorgusu yoksa, tüm şirketleri getir
            offers = Offer.objects.filter(offer_type='satis').order_by('-id')
            offer_type='Satış'
    else:
        offers = Offer.objects.all().order_by('-id')
    

    return render(request,'offer.html',{'offers':offers,"offer_type":offer_type,'companies': companies})

from django.shortcuts import get_object_or_404

@login_required
def delete_offer(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)

    if request.method == 'POST':
        # Offer'ı sil
        offer.delete()
        return redirect('offer')  # Silme işleminden sonra bir sayfaya yönlendirme yapabilirsiniz

    return render(request, 'confirm_delete_offer.html', {'offer': offer})

@login_required
def offer_detail(request,desc):
    
     
    get_offer_object = Offer.objects.get(pk=desc)
    company = get_offer_object.company
    country_name = company.get_country_display_name()
    total_prize = 0

    offer_products = OfferProduct.objects.filter(offer=get_offer_object)
    for offer_product in offer_products:
        print(offer_product.line_total)
        total_prize = total_prize + offer_product.line_total
        print("-------------------")

    print(total_prize)
    # total_price = get_offer_object.total_product_prices()  # Teklifteki tüm ürünlerin fiyatlarının toplamını alalım
    # print(f"Toplam fiyat: {total_price}")

    # for offer_product in offer_products:
    #     product = offer_product.product
    #     print(f"{product.description}: {offer_product.line_total()}")

         

    return render(request,'offer_detail.html',{"get_offer_object":get_offer_object,"country_name":country_name,"offer_products":offer_products,"total_prize":total_prize})

@login_required
def offer_change(request,desc):

    if request.method == 'POST':
        
        product_id = request.POST.get('product_id')  # Örneğin, company_id'nin formdan alındığını varsayalım
        offer_id = request.POST.get('offer_id')
        adet = int(request.POST.get('adet'))
        fiyat = float(request.POST.get('fiyat'))
        print(fiyat)
        print(type(fiyat))

        offer = Offer.objects.get(id=offer_id)
        product = Product.objects.get(id=product_id)

        offer_product = OfferProduct.objects.create(offer=offer, product=product, quantity=adet,offer_product_price=fiyat)
        
        # new_offer.update_total_value()
        print(product_id)
        print(offer_id)
        print(adet)
        

        # return redirect('offer')

    all_product = Product.objects.all()
    get_offer_object = Offer.objects.get(pk=desc)
    # get_offer_object.update_total_value()

    company = get_offer_object.company
    country_name = company.get_country_display_name()
    
    offer = Offer.objects.get(pk=desc)  # Örnek bir offer ID'si
    offer_products = OfferProduct.objects.filter(offer=offer)

    # for offer_product in offer_products:
    #     product = offer_product.product
    #     print(product.description)  # veya 

    return render(request,"offer_change.html",{"get_offer_object":get_offer_object,"country_name":country_name,"offer_products":offer_products,"all_product":all_product})

@login_required
def product_delete_from_offer(request, offer_id, product_id):

    if request.method == 'POST':
        # Silme işlemini gerçekleştir
        offer_product = OfferProduct.objects.get(offer__id=offer_id, product__id=product_id)
        offer_product.delete()
        print("*****************")
        # İşlem tamamlandıktan sonra istediğiniz sayfaya yönlendirme yapabilirsiniz
        return redirect('offer_change', desc=offer_id)
    
 
from django.db.models import Sum  # Sum fonksiyonunu import et

@login_required
def product_statistic(request):
    if request.method == 'GET':
        selected_product_id = request.GET.get('product_id', None)
        if selected_product_id:
            # Ürünleri al
            products = Product.objects.all()

            # İstenen ürünle ilişkili teklif ürünlerini getir
            offer_products = OfferProduct.objects.filter(product_id=selected_product_id)

            # En son hangi teklifte olduğunu bul
            latest_offer = offer_products.latest('offer__created_at')

            # En ucuz teklifi bul
            cheapest_offer = offer_products.order_by('offer_product_price').first()

            # En fazla adet hangi teklifte olduğunu bul
            most_quantity_offer = offer_products.values('offer_id').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
            most_quantity_offer_id = most_quantity_offer['offer_id']
            most_quantity_offer = Offer.objects.get(pk=most_quantity_offer_id)

            print(selected_product_id)
            secilen_urun = Product.objects.get(id = selected_product_id)

            context = {
                'selected_product_id': selected_product_id,
                'latest_offer': latest_offer.offer,
                'cheapest_offer': cheapest_offer.offer,
                'most_quantity_offer': most_quantity_offer,
                'products': products,
                'secilen_urun' : secilen_urun
            }
            return render(request, 'product_statistic.html', context)
    
    # Eğer bir ürün seçilmediyse veya HTTP GET isteği değilse, sadece ürünleri göster
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_statistic.html', context)

import pandas as pd

@login_required
def view_excel(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        df.drop(df.tail(1).index, inplace=True)
        print(df)
        company_name=""
        flag = 0
        
        for index, row in df.iterrows():
            if flag == 0:
                company_name = row["Manufacturer"]
                print(company_name)
                company = get_object_or_404(Company, name=company_name)
                offer = Offer.objects.create(offer_type='alim', company=company)
                flag = 1
            
            # Ürünün daha önce eklenip eklenmediğini kontrol ediyoruz
            product, created = Product.objects.get_or_create(
                boron=row["Boron"],
                coil_id=row["Coil ID"],
                gloss=row["Gloss"],
                size=row['Size'],
                color=row['Colour'],
                zinc=row['Zinc Coating gsm'],
                paint=str(row['Top Paint mikron']) + " & " + str(row['Back Paint mikron']),
                defaults={
                    'description': str(row['Coil ID']) + " - " + str(row['Gloss']) + " - " + str(row['Coil Weight']) + " - " + str(row['Size']) + " - " + str(row['Colour']),
                    'coil_weight': row['Coil Weight'],
                }
            )
            
            # OfferProduct'u oluşturuyoruz veya varsa güncelliyoruz
            offer_product, created = OfferProduct.objects.get_or_create(
                offer=offer,
                product=product,
                defaults={
                    'quantity': row["Weight (Ton)"],
                    'offer_product_price': row['Price-09.02.24'],
                    'destination': row['Destination']
                }
            )    

        # DataFrame'i HTML'e dönüştürme
        html_table = df.to_html()

        return render(request, 'view_excel.html', {'html_table': html_table})

    # # Son 3 teklifi al
    # latest_offers = Offer.objects.order_by('-created_at')[:3]

    # # Her bir ürün için en ucuz teklifleri bul
    # cheapest_offers = find_cheapest_offer_for_each_product(latest_offers)

    # for i, cheapest_offer in enumerate(cheapest_offers, start=1):
    #     product_description = cheapest_offer['offer'].offerproduct_set.first().product.description
    #     print(f"{i}. Ürün: {product_description}, En Ucuz Teklif: {cheapest_offer['offer']}, Fiyat: {cheapest_offer['price']}")
    


    return render(request, 'view_excel.html')

@login_required
def get_best_offer(request):
    if request.method == 'GET':
        adet = request.GET.get('adet', None)
        if adet:
            print("***********************")
            # Son 3 teklifleri almak için
            latest_offers = Offer.objects.order_by('-created_at')[:int(adet)]

            # Her ürün için en uygun fiyatı ve teklif bilgilerini depolamak için bir sözlük oluştur
            best_prices = {}
            
            for offer in latest_offers:
                for offer_product in offer.offerproduct_set.all():
                    product_name = offer_product.product.description
                    price = offer_product.offer_product_price

                    if product_name not in best_prices or price < best_prices[product_name]["price"]:
                        best_prices[product_name] = {"price": price, "offer": offer}

            return render(request, 'get_best_offer.html', {'best_prices': best_prices})
        
    
    return render(request, 'get_best_offer.html')



# from collections import defaultdict

# def find_cheapest_offer_for_each_product(offers):
#     cheapest_offers = defaultdict(lambda: {'offer': None, 'price': float('inf')})

#     for offer in offers:
#         for offer_product in offer.offerproduct_set.all():
#             product_id = offer_product.product.id
#             price = offer_product.offer_product_price
#             if price < cheapest_offers[product_id]['price']:
#                 cheapest_offers[product_id] = {'offer': offer, 'price': price}

#     # Sadece en ucuz teklifleri al
#     unique_cheapest_offers = list(cheapest_offers.values())

#     # Fiyata göre sırala
#     sorted_cheapest_offers = sorted(unique_cheapest_offers, key=lambda x: x['price'])

#     return sorted_cheapest_offers
