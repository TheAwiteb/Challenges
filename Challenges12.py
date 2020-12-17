#X-O GAME
from time import sleep
from random import choice
import os


bord = [
['1','2','3'],
['4','5','6'],
['7','8','9']
]#الطاوبة التي سوف نلعب بها
def print_bord_get_empty(bo): #دالة طباعة الطاولة بشكل منظم للاعب
    unoccupied_place = {} #انشاء دكشنري لحفظ الاماكن الفاضية التي يمكن اللعب بها
    for y in range(3): #انشاء خط الy
        for x in range(3):#انشاء خط الx
            if bo[y][x] != 'X' and bo[y][x] != '+': #اذا الاحداثيات هاذي لاتساوي اكس او زايد (يعني يمكنك تلعب فيها) اضفها الى القائمة
                unoccupied_place[bo[y][x]] = {'y':y,'x':x} #اضافتها الى القائمة
            print(bo[y][x],end='') #نطبع الاحداثي بدون نزول سطر
            if x != 2: #اذا كان احداثي الاكس لا يساوي 2 يعني وصل الى اخر اطبع الخط الذي يفصل بين الارقام
                print('',end=' | ') #طباعة الخط الفاصل
        print('') #عندما ادخل في قيمة y جديدة انزل سطر جديد
    return unoccupied_place #ارجعلي الدكشنري فيه الخانات الي اقدر العب فيها

def checkGame(bo): #دالة للتحقق من قوانين الفوز باللعبة
    for row in bo: #كل ستطر y من الطاولة
        """هاذا قانون اذا كان صف ال y يساون بعضهم يعني حل افقي"""
        if row == [row[0],row[0],row[0]]:
            return True #ارجع قيمة ترو

        """هاذا قانون الحل بطريقة مائلة"""
    if bo[0][0] == bo[1][1] == bo[2][2] or bo[0][2] == bo[1][1] == bo[2][0]:
        return True #ارجع ترو

    else: #اذ لم يكن الحل بطريقة مائلة تحقق اذا كان الحل طولي
        for x in range(0,3):
            if bo[0][x] == bo[1][x] == bo[2][x]: # اذا كان احداثي اكس في y1,y2,y3 نفس القيمة
                return True #ارجع ترو
    return False # اذ لم يتحقق اي شرط يعني مافي فاز ارجع فولس


"""
نظام تحديد اللاعب هنا مختلف شوي
يعني بالبداية يعطي قيمة عشوائي ترو او فولس
واذا كانت القيمة العشوائية ترو يعني الاعب الاول اكس
واذا فولس يعني الاعب الاول (+) وفي اخر الجولة يعكس قيمة البولين
وبكذا يتغير الاعب 
"""
player1OR = choice([1,0]) #اختيار قيمة عشوائية ترو اور فولس

while True:
    sleep(.7) #قبل بداية كل رواند انتظر قبل تنظيف الشاشة
    os.system('cls') #تنظيف الشاشة

    if player1OR: #اذا قيمة الاعب ترو
        player = 'X'
    else: #اذا فولس
        player = '+'

    place = print_bord_get_empty(bord) #تخزين قيمة الاماكن الفاضية في متغير
    if len(place) == 0: #اذا لم يكن هناك مكان
        print("No one won, the result was a draw") #انهي النتيجة بتعادل
        break #اوقف اللعبة

    else: #اذا كان يوجد فيه مكان للعب
        try:
            choose = int(input(f"Choose where you want to place the {player}: ")) #اختيار مكان للعب
        except ValueError: #اذ لم يكن رقم
            print("Sorry enter just number")
            continue #اعد اللوب

        if str(choose) in place: #اذا كان الرقم المدخل تستطيع اللعب فيه
            bord[place[str(choose)]['y']][place[str(choose)]['x']] = player #ضح الاكس او (+) في المكان المختار
        else: #اذ لم يكن في القائمة
            if choose in range(1,10): #اذا كان الرقم من واحد الى تسعة
                print("Sorry this place has been chosen before") #اطبع ان الرقم قد تم اختياره
            else: #اذا كان اكبر من 9
                print("Please choose a number from 1 to 9") #اطبع اختار من 1 الى 9
            continue # تم الرجوع الى اول اللوب عشان لايبدل قيمة الاعب تحت

        if checkGame(bord): #اذا ارجعت دالة التاكد من الفوز ترو
            os.system('cls') # تنظيف الشاشة لطباعة البورد بعد الفوز
            print_bord_get_empty(bord) #طباعة الورد
            print(f"Game over, '{player}' has won",end='') # اخبار من الفائز
            break #اوقف اللعبة

        player1OR = not player1OR # تبديل قيمة الاعب

