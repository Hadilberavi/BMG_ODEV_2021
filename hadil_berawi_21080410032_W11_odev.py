from types import DynamicClassAttribute
#Matrisi tanımlarız ve elemanları içine koyarız.
man = ['majd','ahmad','muru','ali']
# liste ekrana yazdir
print(man)
# kulancidan 4 isim iste
users = input("enter the first name")
#kulanc girdiği isim listeye ekleyiniz ve ekrana yazdir
man.append(users)
print(man)
# liste uzunlugu
print(len(man)) #(len) işlevi dizinin uzunluğunu yazdırmak için kullanılır

#listenin 2. elemanini ekrana yazdiriniz
print('man[1]=',man[1]) #Dizideki herhangi bir öğeye erişmek için, değerini almak veya değiştirmek için, öğenin dizin numarasını kullanırız.
#son elemanini sil
man.pop(-1)   # Sentence(pop), bir diziyi bellekten olduğu gibi silmek veya diziden belirli öğeleri çıkarmak için kullanılır.
print(man)  # Öğeyi sildikten sonra diziyi yazdırmayı tekrarlıyoruz
