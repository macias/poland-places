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
curl 'https://moyastacja.pl/mapa' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/json' -H 'Origin: https://moyastacja.pl' -H 'Connection: keep-alive' -H 'Referer: https://moyastacja.pl/mapa' -H 'Cookie: PHPSESSID=5f79571df4043aacc17c7bda601601de; _ga_C8R5YN224J=GS1.1.1660918294.1.1.1660918338.0.0.0; _ga=GA1.2.1011989688.1660918295; _gid=GA1.2.325263434.1660918296; _gat_gtag_UA_112556703_1=1; _gat_UA-112556703-1=1; _fbp=fb.1.1660918296803.1549341459' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers' --data-raw '{"controller":"Main","action":"GetMap"}' > moya.json
```

*Yes, nothing like making world a better place.*

Then run:
```
./shops.py moya < moya.json  > moya.kml
```

Please note output will contain only manned ones.

### Circle K

Retrieve Circle K stations only (excluding TIR and Express ones) by executing:
```
curl 'https://www.circlek.pl/wyszukaj-stacje' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://www.circlek.pl' -H 'Connection: keep-alive' -H 'Referer: https://www.circlek.pl/wyszukaj-stacje' -H $'Cookie: _fbp=fb.1.1660918450268.72188719; CookieConsent={stamp:\'3wr1yy0gpGQA0sGFLXX5xgICXzQVnPUmj+AcyVqaEu0qMOblQtIryQ==\'%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cver:1%2Cutc:1660918460332%2Cregion:\'pl\'}; _gcl_au=1.1.876072264.1660918461; _ga=GA1.1.1432840077.1660918462; _gid=GA1.2.1951645745.1660918462; visitor_id934173=171117472; visitor_id934173-hash=637bff068aadc38aecd04e847ad79fa5cac5e9ac52006260ab37953e98cb898a9be08d78569098a946f42868dd802845aed73abe; _ga_BYD2EBTLRT=GS1.1.1660936154.3.0.1660936154.0.0.0; AMCV_69F83E625E9932000A495E14%40AdobeOrg=359503849%7CMCIDTS%7C19224%7CMCMID%7C87750715433958135714062286142339562421%7CMCAAMLH-1661523276%7C6%7CMCAAMB-1661523276%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1660925676s%7CNONE%7CMCSYNCSOP%7C411-19231%7CvVersion%7C5.0.1; AMCVS_69F83E625E9932000A495E14%40AdobeOrg=1; _gat_gtag_UA_34402764_26=1; _gat_gtag_UA_34402764_41=1' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data-raw 'phrase=&manned=1&op=Pobierz+wyniki+wyszukiwania&form_build_id=form-eYBmmc_QRrBYWGfCfB8Z3F308XGAjOcXkJmIAb5L3O0&form_id=sim_search_form' > circlek.csv
```

Then run:
```
./shops.py circlek < circlek.csv  > circlek.kml
```


