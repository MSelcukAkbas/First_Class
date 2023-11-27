import time
while True:
    try:
        vize_notu = int(input("Vize notu: "))
        assert 0 <= vize_notu <= 100
        final_notu = int(input("Final notu: "))
        assert 0 <= final_notu <= 100
        break
    except (ValueError, AssertionError):
        print("Geçersiz not! , Tekrar deneyin.")
ortalama = (vize_notu * 0.4) + (final_notu * 0.6)
if ortalama >= 90 :
    print("not: AA - 4.00")
    time.sleep(5)
elif ortalama >= 85 :
    print("not: BA - 3.50")
    time.sleep(5)
elif ortalama >= 80  :
    print("not: BB - 3.00")
    time.sleep(5)
elif ortalama >= 70 :
    print("not: CB - 2.5")
    time.sleep(5)
elif ortalama >= 60 :
    print("not: CC - 2.00")
    time.sleep(5)
elif ortalama >= 55 :
    print("not: DC - 1.50")
    time.sleep(5)   
elif ortalama >= 50 :
    print("not: DD - 1.00")
    time.sleep(5)
elif ortalama >= 40:
    print("not: FD - 0.50")
    time.sleep(5)
elif ortalama >= 0 : 
    print("not: FF - 0.00")
    time.sleep(5)