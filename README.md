# Krypto Discord BOT



## Beschreibung:
Mit diesem Skript werden stündlich die aktuellen Kurse auf Discord in ein Channel gesendet und es werden immer nur die letzten 24 h der Kurse angezeigt.
In die Channels darf nicht vom User geschrieben werden oder etwas gelöscht werden, was der Bot geschrieben hat. Derzeit ist Bitcoin, Dogecoin, Ethereum und Litcoin implementiert. Durch Kopieren oder löschen der einzelnen Teile können Kurse hinzugefügt werden oder entfernt werden.



## Verzeichnis:
> **Schnellster Start:** Quick-Start-Vorbereitung
* [Beschreibung](#Beschreibung)
* [Verzeichnis](#Verzeichnis)
* [Vorbereitung](#Vorbereitung)
  * [Quick-Start-Vorbereitung](#Quick-Start-Vorbereitung)
  * [Weitere Vorbereitung](#Weitere-Vorbereitung)
* [Kompatibilität](#Kompatibilität)
  * [Client Betriebsysteme](#Client-Betriebsysteme)
  * [Server Betriebsysteme](#Server-Betriebsysteme)
  * [Komiler Version](#Kompiler-Version)
  * [Verwendete Bibliotheken](#Verwendete-Bibliotheken)
* [Licenze](#Licenze)

## Vorbereitung:

### Quick-Start-Vorbereitung:
1. Erstellung des Bots auf Discord
2. Bot auf Server mit Admin rechten einladen 
3. Als erstest müssen die Platzhalter durch die API-Keys ersetzt werden 
   [Krypto Key](Bitcoin.de), [Discord Bot Key](https://www.youtube.com/watch?v=4TSBD53e5No&list=PLNmsVeXQZj7rI3usLYlWhsjdFJ-MER_pU)
4. Im nächsten Schritt müssen die Channels auf dem Server erstellt werden und für jede einzelne Kryptowährung die Channel ID im Code eingefügt werden
5. Danach kann durch einmaliges laufen mit Platzhalter.py die Messages in die Channels versendet werden
6. Die Messages können jetzt mit ihrer ID in den Code Verarbeitung.py eingesetzt werden.
7. Jetzt muss main_bot.py und Verarbeitung.py auf den Server im selben Ordner hochgeladen werden und main_bot.py ausgeführt werden.
   > Verarbeitung.py muss im selben Ordner sein wie main_bot.py!
> Ab hier kein Quick-Vorbereitung mehr!

### Weitere Vorbereitung: 
6. Hinzufügen oder Entfernen von Kryptowährungen, indem Teile Kopiert werden oder entfernt werden -> Oder Ersetzung im Link die Kryptowährung

## Kompatibilität:

### Client Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Windows|Windows 10|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows|Windows 11|![funk](https://img.shields.io/badge/checks-passing-green)|
|Arch Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|CentOS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Elementary OS|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Fedora|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Gentoo Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Kali Linux|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Mojave|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS High Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|macOS Sierra|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|OS X El Capitan|aktuelleste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#
### Server Betriebsysteme:
|Betriebsystem|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Ubuntu|aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|
|Debian|aktuellste Version|![funk](https://img.shields.io/badge/checks-passing-green)|
|Windows Server| aktuellste Version|![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

#

### Kompiler Version:
|Kompiler|Version|Test Ergebnis|
|:---:|:---:|:---:|
|Python| 3.9 |![funk](https://img.shields.io/badge/checks-passing-green)|
|Python| 3.10 |![funk](https://img.shields.io/badge/checks-passing-green)|
|Python| aktuellste Version |![funk_n](https://img.shields.io/badge/checks-not%20tested-red)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

### Verwendete Bibliotheken:
|Bibliothek|Version|Test Ergebnis|
|:---:|:---:|:---:|
|datetime| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|requests| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|pycord| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|
|asyncio| aktuellste Version |![funk](https://img.shields.io/badge/checks-passing-green)|

> Wurde getestet: ![funk](https://img.shields.io/badge/checks-passing-green) | Wurde noch nicht getestet: ![funk_n](https://img.shields.io/badge/checks-not%20tested-red)

## Licenze:

Die Lizenz zur weiter Verwendung dieses Projektes, wird durch das **Creative Common** Model angegeben. 
Bei Ablehnung jeglicher Verwendung durch meinerseits mit den Piktogrammen oder Sie möchten das Projekt in einer Form verwenden, die nicht hier genannt wurde, muss vor 
der Benutzung des Projektes die Zustimmung eingeholt werden.

|Verwendet|Piktogramm|Bezeichnung|Verlinkung|
|:---:|:---:|:---:|:---:|
|:x:|![Licenze_eins](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png)|Namensnennung 4.0 International|[Details](https://creativecommons.org/licenses/by/4.0/legalcode.de)|
|:x:|![Licenze_zwei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)|Namensnennung-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de)|
|:x:|![Licenze_drei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nd.png)|Namensnennung-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nd/4.0/legalcode.de)|
|:x:|![Licenze_vier](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.eu.png)|Namensnennung-Nicht kommerziell 4.0 International|[Details](https://creativecommons.org/licenses/by-nc/4.0/legalcode.de)|
|:heavy_check_mark:|![Licenze_fünf](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png)|	Namensnennung-Nicht kommerziell-Share Alike 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de)|
|:x:|![Licenze_sex](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.eu.png)|	Namensnennung-Nicht kommerziell-Keine Bearbeitungen 4.0 International|[Details](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.de)|

> Verwendete Licenze: :heavy_check_mark: Nicht verwendete Licenze: :x:
