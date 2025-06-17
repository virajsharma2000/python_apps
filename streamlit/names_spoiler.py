import streamlit as st

animals = [
    "bakri",        # meh meh karta rahta hai bina wajah
    "billi",        # sab kuch gira deti hai raat ko
    "kauwa",        # subah-subah chillata hai jaise alarm clock
    "ullu",         # raat bhar aankhen phaad ke dekhta hai
    "bandar",       # sab cheez utha ke le jaata hai
    "saanp",        # chupke se aa ke dara deta hai
    "kachhua",      # itna slow ki gussa aa jaye
    "lombdi",       # hamesha chalak banne ki acting karta hai
    "magarmach",    # jhoote aansu baha ke sabko bewakoof banata hai
    "tota",         # har baat baar-baar dohrata hai, irritating!
    "bhed",         # apna dimaag kabhi nahi lagata, sabke peeche chalta hai
    "oont",         # muh fula ke baitha rehta hai, attitude se
    "machhli",      # pakdo toh fisl jaati hai, chup bhi nahi rehti
    "murgi",        # subah se bukk bukk karte rehti hai
    "kabootar",     # bina invite ke chhat pe aa jaata hai
    "gadha",        # kuch bhi samjhao, kuch farq nahi padta
    "tiddi",        # jhund mein aake sab kuch chaba jaati hai
]

animal_comments = {
    "bakri": "meh meh karta rehta hai bina mic ke, jaise sabko disturb karna mission ho",
    "billi": "raat ko ninja ban ke sab kuch gira deta hai aur fir innocent ban jaata hai",
    "kauwa": "subah 4 baje se hi live concert shuru, bina ticket ke",
    "ullu": "raat bhar aankhen phaad ke sabko jhaankta rehta hai, jaise spy ban gaya ho",
    "bandar": "jo cheez haath lage, usi se stunts shuru – circus khud hi ban jaata hai",
    "saanp": "aata hi nahi, par jab aata hai toh seedha heart attack deta hai",
    "kachhua": "internet se bhi slow, chalte chalte neend aa jaye",
    "lombdi": "itni chaalu ki khud ko hi scam kar de ek din",
    "magarmach": "aansu se drama karta hai, asli kaam bas emotion ka scam hai",
    "suar": "jahaan jaaye, wahin party ban jaati hai – lekin gandi wali",
    "tota": "jo suna, wahi repeat karta hai 24x7 – jaise broken Alexa ho",
    "bhed": "apna kuch nahi, bas dusro ke peechhe chalta rehta hai jaise auto mode",
    "oont": "muh aise fulaata hai jaise usko WiFi ka password nahi mila ho",
    "machhli": "chup bhi nahi rehti, aur haath bhi nahi aati – ultra slippery personality",
    "murgi": "roz subah chilla chilla ke sabka mood kharaab kar deti hai, bina reason",
    "kabootar": "random chhat pe land karta hai, bina visa ke guest ban jaata hai",
    "gadha": "kitna bhi samjha lo, system update kabhi hota hi nahi",
    "tiddi": "jhund mein aake sab kuch chaba jaati hai – friendship, lunch, mood"
}

def spoil_name(name):
 name = name.lower()
 
 animal_name = animals[sum(ord(char) for char in name.replace(' ', '')) % len(animals)]
 spoiled_name = name.split()[0] + ' ' + animal_name + ' ' + name.split()[1]
 
 description = animal_comments[animal_name]

 return (spoiled_name, description)


st.title('Names Spoiler special friend\'s mood spoiler')

name = st.text_input('Enter a name')

if st.button('Spoil Name'):
 spoiled_name, description = spoil_name(name)

 st.subheader('name - ' + spoiled_name)
 st.subheader('description - ' + description)
 


