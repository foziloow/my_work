# word="Hello world"
# print(word)

# habar= 10
# print(habar)
# habar=5
# print(habar)


# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"

# print(f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati")


# kocha=input("Kochangiz")
# mahalla=input("Mahallangiz")
# tuman=input("tumaningiz")
# viloyat=input("viloyatingiz")

# print(f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati")

# manzil=f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.title())
# print(manzil.capitalize())


# user=int(input("istalgan son kiriting"))
# print(f" {user} kvadirati {user**2} teng, {user} kubi  {user**3} teng")

# t_yosh=int(input("Yoshingizni Kiriting"))
# print(f"siz {t_yosh - 2024} yilda tug'ilgansiz")

# num=int(input("1 chi raqam yozin"))
# num2=int(input("2 chi raqam yozin"))
# print(f"{num} + {num2} = {num+num2}")
# print(f"{num} - {num2} = {num-num2}")
# print(f"{num} * {num2} = {num*num2}")
# print(f"{num} / {num2} = {num//num2}")

# ismlar=['abror','ali','vali']
# print(f"Salom {ismlar[0]} qalesan {ismlar[1]} nima gap {ismlar[2]}")

# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
# sonlar[0]=10
# sonlar[1]=20
# sonlar[2]=-245
# del sonlar[-2]
# print(sonlar)

# t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
# print(f"Men tatixiy shaxslardan {t_shaxslar.pop(0)} Xurmat qilama,\n\
#       Zamonaviy shaxlarda {z_shaxslar.pop(1)} Yaxshi tanima")

# frinds=[]
# frinds.append("Ali")
# frinds.append("Vali")
# frinds.append("Abror")
# frinds.append("Anvar")
# frinds.append("Akbar")
# print(frinds)

# frinds.remove("Ali")
# frinds.remove("Akbar")
# print(frinds)

# frinds.append("Bilol")
# frinds.insert(0,"Asad")
# frinds.insert(3,"Ayub")
# print(frinds)

# mehmonlar=[]
# mehmonlar.append(frinds.pop(-1))
# mehmonlar.append(frinds.pop(1))
# mehmonlar.append(frinds.pop(2))

# print(mehmonlar)

# davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
# # print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar,reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# # print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# nums=list(range(120,1200))
# print(sum(nums))
# print(max(nums)-min(nums))
# print(len(nums))
# print(nums[0:20])
# print(nums[-20:])

# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

# nonushta=taomlar[:]
# nonushta.remove('osh')
# nonushta.remove('somsa')
# nonushta.insert(0,'non')
# # print(nonushta)
# print(taomlar)
# nonushta=tuple(nonushta)

# print(nonushta)
# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"assalomu aleykum {ism} yaxshi misiz")

# print(f"kod {len(ismlar)} marta takrorlandi")

# nums=list(range(11,100,2))
# for i in nums:
#     print(i**2)
# kino=[]
# for i in range(5):
#     kino.append(input(f'Kino yozin{i+1}'))
# print(kino)
# ism=[]
# user=int(input("Bugu nechta odam bilam gaplashtiz"))
# print(" Ularni ismini yozin")
# for i in range(user):
#     ism.append(input(f'{i+1} ismin yozin'))
# print(f'bugu gaplashgan odamlarzi {ism}')


user=int(input("raqam kiriting"))
if user < 0 :
    print(user+1)
else:
    print(user)