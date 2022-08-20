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

Retrieve [all the shops data](https://www.rossmann.pl/shops/api/shops). Then run:
```
./shops.py rossmann < shops.json  > rossmann.kml
```

### Żabka

Retrieve [all the shops data](https://www.zabka.pl/ajax/shop-clusters.json). Then run:
```
./shops.py zabka < shop-clusters.json  > zabka.kml
```

### Moya

Retrieve all stations by executing:
```
curl 'https://moyastacja.pl/mapa' -H 'Content-Type: application/json' --data-raw '{"controller":"Main","action":"GetMap"}' > moya.json
```

Then run:
```
./shops.py moya < moya.json  > moya.kml
```

Please note output will contain only manned ones.

### Circle K

Retrieve Circle K stations only (excluding TIR and Express ones) by executing:
```
curl 'https://www.circlek.pl/wyszukaj-stacje' --data-raw 'phrase=&manned=1&op=Pobierz+wyniki+wyszukiwania&form_build_id=form-eYBmmc_QRrBYWGfCfB8Z3F308XGAjOcXkJmIAb5L3O0&form_id=sim_search_form' > circlek.csv
```

or simply go to [Circle K webpage](https://www.circlek.pl/wyszukaj-stacje), filter out the stations, select "Additional options" ("Opcje dodatkowe")
and click on "Download search results" ("Pobierz wyniki wyszukiwania").

Then run:
```
./shops.py circlek < circlek.csv  > circlek.kml
```


