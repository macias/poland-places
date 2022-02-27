# Poland — places

Useful maps for your bikepacking trips (in Poland) — see it at
[Google Maps](https://www.google.com/maps/d/edit?mid=1l2Pl5J3VAosJ-ESXrLPnW0w6s7h-yeNe&usp=sharing).
Please note some of the remainings are already gone.

See my PL/EN [blog](https://przypadkopis.wordpress.com/) for other, various in nature, resources.

## Romanesque trail

Based on [Szlak romański](https://turystyczneszlaki.pl/szlak-romanski/) with corrections using Google satellite maps
and [Polish wikipedia](https://pl.wikipedia.org/wiki/Szlak_Roma%C5%84ski_w_Polsce). There are still few places which
I was unable to pinpoint (marked with “?”) and one place which is probably an error (romanesque signpost in Stare Miasto;
actually the artifact is located in Konin).

**Links**:

* EN/PL [Polish monuments](https://zabytek.pl/)
* PL [Styl romański w Wielkopolsce](https://wielkopolskaciekawie.pl/bez-kategorii/styl-romanski-w-wielkopolsce/)

## Teutonic castles trail

Initial, well prepared map was taken from [Zamki krzyżackie w Polsce – mapa](https://discover.pl/mapa-zamkow-krzyzackich-w-polsce/),
later on new entries were added using following sources. For actual mapping Google Maps and OpenStreetMap were used. “KW” suffix denotes castles of Warmia Chapter.

**Links**:

* PL [Zamki znane i nieznane](https://zamkiobronne.pl/)
* EN/PL [Castles in Poland](http://www.polishcastles.eu/)
* PL [Szlak Zamków Krzyżackich](https://kujawsko-pomorskie.travel/pl/content/szlak-zamkow-krzyzackich)
* EN/PL [Polish Gothic Castles](https://zamkigotyckie.org.pl/en)
* PL [Kociewie24](https://kociewie24.eu/)
* PL [naKole](http://www.nakole.net/)
* PL [Zamkomania](https://zamkomania.pl/)
* PL [Gniew: Nasze Miasto](https://gniew.naszemiasto.pl/)
* PL [Średniowieczna architektura obronna](https://zamkidwory.forumoteka.pl/)
* EN/PL [Wikimapia](http://wikimapia.org/)
* PL [Rotmanka](http://zamki.rotmanka.com/)

## Eagles' Nests trail

All places follow [the list at Wikipedia](https://pl.wikipedia.org/wiki/Orle_Gniazda). Some additional information regarding
locations are from [Odtur](https://odtur.pl/atrakcje/gieblo-zamek-w-gieble-nieistniejacy-47573.html),
[Eksploratorzy](https://eksploratorzy.com.pl/viewtopic.php?f=99&t=19155), [Strażnicy Czasu](http://www.straznicyczasu.pl/viewtopic.php?t=2012),
[Jurainfo](https://www.jurainfo.pl/p/1,straznica-obronna-na-kamieniu-mirow-kolo-czestochowy),
[Polskie zamki](https://www.zamki.pl/?idzamku=wiesiolka), [Zamki znane i nieznane](https://zamkiobronne.pl/zamek/brzeznica/)
and [Fotowojaże](https://fotowojaze.pl/zloty-potok/).

## Shop networks

Not a sightseeing but useful to have it.

### Rossmann

Retrieve [all the shops data](https://www.rossmann.pl/shops/api/shops). Assuming you saved the data to
"rossmann_shops.json" file, execute:

```
./shops.py rossmann < rossmann_shops.json  > rossmann_shops.kml
```

### Żabka

Retrieve [all the shops data](https://www.zabka.pl/ajax/shop-clusters.json). Assuming you saved the data to
"zabka_shops.json" file, execute:

```
./shops.py zabka < zabka_shops.json  > zabka_shops.kml
```

