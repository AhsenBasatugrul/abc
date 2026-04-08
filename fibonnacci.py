def fibonacci(n):
    a, b = 0, 1
    liste = []
    for i in range(n):
        liste.append(a)
        a, b = b, a + b
    return liste

intput = int(input("Kaç tane fibonacci sayısını görmek istersiniz: "))
print(fibonacci(intput)) 
print(f"Fibonacci sayısı: {fibonacci(intput)}")
<<<<<<< HEAD
print("ASdf")
=======
print("deneme123")
>>>>>>> 970d44e3e9c0777298ecb0af0db21f027c41547e
