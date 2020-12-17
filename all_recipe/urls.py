from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("indian/kashmiri", views.kashmiri, name="kashmiri"),
    path("indian/andhra", views.andhra, name="andhra"),
    path("indian/chettinad", views.chettinad, name="chettinad"),
    path("indian/punjabi", views.punjabi, name="punjabi"),
    path("indian/maharashtrian", views.maharashtrian, name="maharashtrian"),
    path("indian/gujarati", views.gujarati, name="gujarati"),

    #ANDHRA
    path("indian/andhra/pepperChicken", views.pepperChicken, name="pepperChicken"),
    path("indian/andhra/andhraChicken", views.andhraChicken, name="andhraChicken"),
    path("indian/andhra/eggCurry", views.eggCurry, name="eggCurry"),
    path("indian/andhra/fishFry", views.fishFry, name="fishFry"),
    path("indian/andhra/mushroom", views.mushroom, name="mushroom"),
    path("indian/andhra/paalPayasam", views.paalPayasam, name="paalPayasam"),

    #CHETTINAD
    path("indian/chettinad/aatukkariKuzhambu", views.aatukkariKuzhambu, name="aatukkariKuzhambu"),
    path("indian/chettinad/chettinadChicken", views.chettinadChicken, name="chettinadChicken"),
    path("indian/chettinad/andhraBhindi", views.andhraBhindi, name="andhraBhindi"),
    path("indian/chettinad/hyderabadiBiriyani", views.hyderabadiBiriyani, name="hyderabadiBiriyani"),
    path("indian/chettinad/panasaPuttu", views.panasaPuttu, name="panasaPuttu"),
    path("indian/chettinad/kebabs", views.kebabs, name="kebabs"),

    #GUJARATI
    path("indian/gujarati/aamShrikand", views.aamShrikand, name="aamShrikand"),
    path("indian/gujarati/dalDhokli", views.dalDhokli, name="dalDhokli"),
    path("indian/gujarati/dhokla", views.dhokla, name="dhokla"),
    path("indian/gujarati/khandvi", views.khandvi, name="khandvi"),
    path("indian/gujarati/thepla", views.thepla, name="thepla"),
    path("indian/gujarati/handvo", views.handvo, name="handvo"),

    #KASHMIRI
    path("indian/kashmiri/dumAloo", views.dumAloo, name="dumAloo"),
    path("indian/kashmiri/khatteBaingan", views.khatteBaingan, name="khatteBaingan"),
    path("indian/kashmiri/muttonRibs", views.muttonRibs, name="muttonRibs"),
    path("indian/kashmiri/nadrooYakhni", views.nadrooYakhni, name="nadrooYakhni"),
    path("indian/kashmiri/roganJosh", views.roganJosh, name="roganJosh"),
    path("indian/kashmiri/saag", views.saag, name="saag"),

    #MAHARASHTRIAN 
    path("indian/maharashtrian/aamti", views.aamti, name="aamti"),
    path("indian/maharashtrian/pavBhaji", views.pavBhaji, name="pavBhaji"),
    path("indian/maharashtrian/pudachiWadi", views.pudachiWadi, name="pudachiWadi"),
    path("indian/maharashtrian/batataVada", views.batataVada, name="batataVada"),
    path("indian/maharashtrian/puranPoli", views.puranPoli, name="puranPoli"),
    path("indian/maharashtrian/misalPav", views.misalPav, name="misalPav"),

    #PUNJABI
    path("indian/punjabi/amritsariFish", views.amritsariFish, name="amritsariFish"),
    path("indian/punjabi/butterChicken", views.butterChicken, name="butterChicken"),
    path("indian/punjabi/choleBhature", views.choleBhature, name="choleBhature"),
    path("indian/punjabi/dalMakhani", views.dalMakhani, name="dalMakhani"),
    path("indian/punjabi/sarsonSaag", views.sarsonSaag, name="sarsonSaag"),
    path("indian/punjabi/tandooriChicken", views.tandooriChicken, name="tandooriChicken"),

    #CONTINENTAL
    path("continental/bruschetta", views.bruschetta, name="bruschetta"),
    path("continental/margherita", views.margherita, name="margherita"),
    path("continental/batterfriedfish", views.batterfriedfish, name="batterfriedfish"),
    path("continental/chickenmanchurian", views.chickenmanchurian, name="chickenmanchurian"),
    path("continental/schezwanfriedrice", views.schezwanfriedrice, name="schezwanfriedrice"),
   
    path("about", views.about, name="about"),
    path("feedback", views.feedback, name="feedback"),
    path("continental", views.continental, name="continental"),
    path("logout", views.logout_view, name="logout")
]