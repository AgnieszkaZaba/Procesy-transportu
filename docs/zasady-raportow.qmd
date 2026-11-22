---
title: "Zasady przygotowywania i oceniania raportów"
subtitle: "Modelowanie Procesów Transportu w Środowisku"
lang: pl
format:
  pdf:
    toc: false
    number-sections: true
---

# Cel raportów

Raporty stanowią dokumentację przeprowadzonych ćwiczeń
laboratoryjnych i są, zgodnie z sylabusem przedmiotu,
podstawą oceny pracy studentów i studentek.
Raport powinien dokumentować wykonane zadania,
przedstawiać uzyskane wyniki oraz umożliwiać
odtworzenie przeprowadzonych symulacji na podstawie
załączonego kodu.

# Forma raportu
Raport należy przygotować w postaci pliku PDF wygenerowanego
na podstawie kodu źródłowego. Osoby korzystające z notebooków Jupyterowych mogą wykorzystać
narzędzia takie jak [Quarto](https://quarto.org/) lub `nbconvert`.

(Mamy wtedy pewność,
że przedstawione wykresy i wyniki zostały wygenerowane
za pomocą kodu oraz że można je odtworzyć).

# Zawartość raportu

1. Imię i nazwisko, nazwę zajęć, numer raportu i datę. 
2. Tytuł oraz krótki opis celu ćwiczenia: 
Raport powinien zawierać tytuł oraz jedno zdanie określające,
jakie zagadnienie jest analizowane.
Przykład:
*Modelowanie ruchów Browna dla różnych rozkładów prawdopodobieństwa.*

3. Kod źródłowy w raporcie lub w osobnym pliku.
Kod powinien umożliwiać odtworzenie przedstawionych wyników.
Należy zadbać o:

   - czytelność i uporządkowanie kodu;
   - odpowiednie nazewnictwo zmiennych;
   - możliwość ponownego uruchomienia symulacji.

4. Ponumerowane i opisane wykresy lub tabele. 
Raport powinien zawierać wykresy lub tabele prezentujące wyniki przeprowadzonych symulacji i analiz.
Każdy wykres powinien:

   - posiadać numer i tytuł;
   - zawierać legendę, jeśli jest potrzebna;
   - mieć opisane osie wraz z jednostkami fizycznymi;
   - być czytelny i odpowiednio sformatowany;
   - umożliwiać rozróżnienie wyników otrzymanych dla różnych parametrów symulacji.

    Należy stosować grafikę wektorową, 
    która zapewnia dobrą czytelność po powiększeniu i podczas drukowania.
    Jeżeli przedstawiane są analogiczne wykresy dla
    różnych parametrów, np. liczby kroków, mnożnika
    lub czasu symulacji, różnice muszą być jednoznacznie
    zaznaczone na wykresie albo w jego opisie.
    
    Przykład:
    
    ```python
    plt.title(f"Ruch Browna dla N={N} cząstek")
    ```

    Każdy wykres powinien być uzupełniony jednym zdaniem opisu 
    lub komentarza, zawierającym odniesienie do jego numeru.

5. Wnioski w maksymalnie jednym akapicie.
Raport powinien kończyć się krótkimi wnioskami
dotyczącymi wykonanego zadania (max jeden akapit).

Należy uwzględnić w szczególności:

- czy symulacja przebiegła poprawnie;
- czy wyniki są zgodne z oczekiwaniami teoretycznymi;
- czy wystąpiły błędy lub problemy z działaniem kodu;
- czy kod działa poprawnie dla wszystkich analizowanych przypadków.

Jeżeli wystąpiły problemy, należy je krótko opisać zamiast pomijać nieudane przypadki.

# Zasady oceniania i poprawy

Raport może zostać:

- **Przyjęty** — jeśli spełnia wymagania formalne i merytoryczne, a autor lub autorka potrafi wyjaśnić przedstawione wyniki i działanie kodu.
- **Nieprzyjęty** — jeśli nie spełnia istotnych wymagań, zawiera wyniki, których nie można odtworzyć, lub autor albo autorka nie potrafi wyjaśnić przedstawionej pracy.

Student lub studentka powinni znać i rozumieć kod oraz potrafić
wyjaśnić sposób uzyskania przedstawionych wyników.
Jeżeli podczas prezentacji autor lub autorka nie potrafi
wyjaśnić podstawowych elementów raportu,
działania kodu lub interpretacji wykresów,
może to stanowić podstawę do nieprzyjęcia raportu i
konieczności jego poprawy.

Nieprzyjęty raport można poprawić i zaprezentować na kolejnych zajęciach.
Za opóźnienie w oddaniu raportu może zostać obniżona ocena.
