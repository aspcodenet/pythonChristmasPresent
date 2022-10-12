# Skapa en klass ChristmasPresent. Den ska ha Name och ett Price (vad den kostar) 
# Skapa en klass Person. Den ska ha Name och en lista med julklappar. Gör också så att det går att lägga till julklappar, och räkna fram totalen (vad alla personens julklappar kostar)
# Skapa nu (i main) tre personer.  Skapa några julklappar för varje person och skriv en loop som går igenom alla personer,
# skriver ut dess namn och vad dess julklappar kostar.    OBS: tänk på god OOP.  
# Exempel på hur programmet ska se ut när man kör det:
# Stefan - ska få julklappar för totalt 4815kr
# Kerstin - ska få julklappar för totalt 15kr
# Oliver - ska få julklappar för totalt 1112 kr 

from person import Person
from christmaspresent import ChristmasPresent

p1 = Person("Stefan")
present = ChristmasPresent("PS5", 4800)
p1.AddChristmasPresent( present  )
p1.AddChristmasPresent( ChristmasPresent("Telefon", 500)  )

p2 = Person("Kerstin")
p2.AddChristmasPresent( ChristmasPresent("Penna", 15)  )

p3 = Person("Oliver")
p3.AddChristmasPresent( ChristmasPresent("Dator", 15000)  )


personLista = [p1,p2,p3]
for p in personLista:
    print(f"{p.GetName()} - ska få julklappar för totalt {p.GetTotal()}kr")
