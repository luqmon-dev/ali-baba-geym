# import random
# olcham = 10
#
# class Alibobo:
#     def __init__(self,name,x,y,):
#         self.name = name
#         self.sogliq = 100
#         self.qurol = 3
#         self.x = x
#         self.y = y
#     def xorjin_ol(self,xorjin):
#         if xorjin.olinganmi == False:
#             self.qurol += xorjin.qurol
#             self.sogliq += xorjin.dori
#             if self.sogliq > 100:
#                 self.sogliq = 100
#             xorjin.olinganmi = True
#             print(f"Xorjin olindi! Qurol: {self.qurol},Sogliq: {self.sogliq}")
#
#     def harakat(self,yonalish):
#         if yonalish=='chap'and self.x> 0:
#             self.x -= 1
#
#         elif yonalish=='ong'and self.x < olcham-1:
#             self.x += 1
#
#         elif yonalish=='tepa' and self.y > 0:
#             self.y -= 1
#
#         elif yonalish=='past' and self.y < olcham-1:
#             self.y += 1
#         else:
#             print("Бу томонга юриб бўлмайди!")
#         print(f"Joylashuv: {self.x}, {self.y}")
#
#     def jang(self,qaroqchi):
#         if self.qurol >0:
#             qaroqchi.sogliq -= 30
#             self.qurol -= 1
#             print(f"Qaroqchi sog'lig'i: {qaroqchi.sogliq}, Qolgan qurol: {self.qurol}")
#         else:
#             print("Qurol tugadi!Xorjinni toping")
#
# class Xorjin:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.qurol = 3
#         self.dori = 30
#         self.olinganmi = False
#
#
# class Qaroqchi:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         self.sogliq = 30
#         self.ziyon = 20
#
#     def hujum(self,ali):
#         ali.sogliq -= self.ziyon
#         print(f"Qaroqchi hujum qildi! Sogliq: {ali.sogliq}")
#     def update(self):
#         yonalish = random.choice(["chap","ong","tepa","past"])
#         self.harakat(yonalish)
#
#     def harakat(self,yonalish):
#         if yonalish=='chap'and self.x> 0:
#             self.x -= 1
#
#         elif yonalish=='ong'and self.x < olcham-1:
#             self.x += 1
#
#         elif yonalish=='tepa' and self.y > 0:
#             self.y -= 1
#
#         elif yonalish=='past' and self.y < olcham-1:
#             self.y += 1
#
#
# class Xazina:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# def maydon_chiz():
#     for y in range(olcham):
#         for x in range(olcham):
#             belgi = "."
#             if xazina.x  == x and xazina.y == y:
#                 belgi = "X"
#             for xorjin in xorjinlar:
#                 if xorjin.x == x and xorjin.y == y and xorjin.olinganmi ==False:
#                     belgi = "H"
#             for qaroqchi in qaroqchilar:
#                 if qaroqchi.x == x and qaroqchi.y == y and qaroqchi.sogliq > 0:
#                     belgi = "Q"
#             if ali.x == x and ali.y == y:
#                 belgi = "A"
#             print(belgi, end = " ")
#         print()
#
# ali = Alibobo("Ali Bobo",0,0)
# xazina = Xazina(9,9)
# xorjinlar = [Xorjin(5,5), Xorjin(2,7), Xorjin(8,3)]
# qaroqchilar = [Qaroqchi(3,3), Qaroqchi(8,8), Qaroqchi(6,6)]
#
# while ali.sogliq > 0:
#     yonalish =input("yonalish kiriting: ")
#     ali.harakat(yonalish)
#
#     for xorjin in xorjinlar:
#         if ali.x == xorjin.x and ali.y == xorjin.y:
#             ali.xorjin_ol(xorjin)
#
#     for qaroqchi in qaroqchilar:
#         if not (ali.x == qaroqchi.x and ali.y == qaroqchi.y):
#             qaroqchi.update()
#         if ali.x == qaroqchi.x and ali.y == qaroqchi.y and qaroqchi.sogliq > 0:
#             qaroqchi.hujum(ali)
#             ali.jang(qaroqchi)
#     maydon_chiz()
#
#     if ali.x == xazina.x and ali.y == xazina.y:
#         print("G'alaba!Ali Bobo xazinani topdi")
#         break
# if ali.sogliq <= 0:
#     print("Ali Bobo halok bo'ldi. Siz yutqazdingiz")
#
#
#





