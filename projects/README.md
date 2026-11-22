# Zajęcia projektowe: Modelowanie Procesów Transportu w Środowisku

zajęcia w semstrze zimowym 26/27
poniedziałki

- 8:00 - 10:15 --- gr. 2; s. 30b, D10 
- 12:15 - 14:30 --- gr. 1; s. 206, D10

## Wymagania
Projekt ma być ciekawy i nie musi być bardzo skomplikowany.
Projekt jest rozszerzeniem jednego z zagadnień omawiany w trakcie semestru na zajęciach laboratoryjny. 
Projekty są realizowane indywidualnie, 
 możliwa jest współpraca nad kodem, który jest wspólny dla kilku zagadnień 
 (proszę ustalać szczegóły z prowadzacą).

### Wymagania merytoryczne
1. Projekt omawia realne zjawisko występujące w środowisku: pytanie badawcze.
2. Należy wykorzystać rzeczywiste dane: pomiarowe, wymagania dotyczące np. stężeń, dane z publikacji dot. zjawiska.
3. Model testujemy pod kątem: stabilności, zbieżności, poprawności wyników.
4. 

### Wymagania techniczne
1. Kod projektu dostępny jest przez platformę **GitHub**.
2. Raport `pdf` lub `html` jest generowany automatycznie przez **GitHub Action**
   (przykładowy workflow dostępny jest w tym repozytorium: .github/workflows/render.yml)
3. Jednostki fizyczne są użyte np. przez pakiet `pint`, przeprowadzona jest analiza wymiarowości.
4. Stałe fizyczne przechowywane są w jednym katalogu (np. `from collections import namedtuple`).

### Plan spotkań

- **23.11.2026 (1h)** 
  - Prowadząca: przedstawienie wymagań dotyczących projektów
  - S: zapoznanie się z propozycją tematów 
  - S: przygotowanie repozytorium na GitHubie, udostępnienie `@AgnieszkaZaba`
- **30.11.2026**
  - S: Krótka prezentacja tematu (3 min, jeden slajd, generowany z notebooka przez Quarto)
    - Jakie pytanie badawcze?
    - Jakie dane będą potrzebne, z czego możemy skorzystać? 
    - Jakie metody będą wykorzystane?
  - S: Praca nad projektem, konfiguracja workflow z generowaniem raportu
- **07.12.2026**
  - S: Prezentacje postępów (5 min): 
    - co wyszło? 
    - czym chcę się pochwalić?
    - co jest jeszcze wyzwaniem? 
  - S: Praca nad projektami
  - Prowadząca: metody analizy metod numerycznych - przypomnienie
- **14.12.2026** 
  - S: Oddanie projektów, prezentacja wyników (15 min + 5 min)
  - P&S: dyskusja.
    
## Przykładowe tematy:

1. Modelowanie znacznika w rzece:
   - Kocinka (dopasowanie krzywej do danych),
   - rozszerzenie zagadnienia o dodanie losowości dla dyfuzji z różnych rozkładów,
   - rozważenie zagadnienia w dwóch wymiarach, uwzględniając zmienne koryto rzeki, meandry (wpływające na przepływ),
   - dodanie zależności od nasłonecznienia dla znaczników biologicznych.

2. Transport w powietrzu:
   - modelowanie zanieczyszczenia z komina uwzględniając prędkość wiatru

3. Transport ciepła w glebie:
   - modelowanie ciepła dla innych planet i porównanie: Mars, Wenus - znalezienie nasłonecznienia, specyfikacji gleby itp,
   - modelowanie ciepła na Ziemi uwzględniając atmosferę, zmienne warunki dobowe itp. (porównanie z danymi),
   - modelowanie w dwóch wymiarach (istotne np. przy pompach ciepła),
   - wpływ wilgotności gleby na przewodność cieplną,
   - wpływ rodzaju gruntu (piasek, glina, gleba organiczna). 

4. Transport wody w glebie 
   - modelowanie transportu wody z określaniem wieku wody (średniego czasu przebywania), 
   - intensywność opadów a transport wodny,
