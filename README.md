# Krypto Discord BOT

## Beschreibung:
Mit diesem Skript werden stündlich die aktuellen Kurse auf Discord in einen Channel gesendet. Es werden immer nur die letzten 24 Stunden der Kurse angezeigt.  
In den Channels darf nicht vom User geschrieben werden oder etwas gelöscht werden, was der Bot geschrieben hat. Derzeit sind Bitcoin, Dogecoin, Ethereum und Litecoin implementiert.  


## Verzeichnis:
> **Schnellster Start:** Quick-Start-Vorbereitung

* [Beschreibung](#Beschreibung)
* [Verzeichnis](#Verzeichnis)
* [Vorbereitung](#Vorbereitung)
  * [Quick-Start-Vorbereitung](#Quick-Start-Vorbereitung)
  * [Weitere Vorbereitung](#Weitere-Vorbereitung)
* [Kompatibilität](#Kompatibilität)
  * [Client-Betriebssysteme](#Client-Betriebssysteme)
  * [Server-Betriebssysteme](#Server-Betriebssysteme)
  * [Compiler-Version](#Compiler-Version)
  * [Verwendete Bibliotheken](#Verwendete-Bibliotheken)
* [Lizenz](#Lizenz)

## Vorbereitung:

### Quick-Start-Vorbereitung:
1. Erstellung des Bots auf Discord
2. Bot auf Server mit Administratorrechten einladen
3. Als erstes müssen die Platzhalter durch die API-Keys ersetzt werden  
   [Krypto Key](Bitcoin.de), [Discord Bot Key](https://www.youtube.com/watch?v=4TSBD53e5No&list=PLNmsVeXQZj7rI3usLYlWhsjdFJ-MER_pU)
4. Im nächsten Schritt müssen die Channels auf dem Server erstellt werden. Für jede einzelne Kryptowährung muss die Channel-ID im Code eingefügt werden
5. Danach kann durch einmaliges Ausführen von `Platzhalter.py` die Nachrichten in die Channels gesendet werden
6. Die Nachrichten können jetzt mit ihrer ID in den Code `Verarbeitung.py` integriert werden
7. Nun müssen `main_bot.py` und `Verarbeitung.py` auf den Server im selben Ordner hochgeladen werden, und `main_bot.py` muss ausgeführt werden.  
   > `Verarbeitung.py` muss im selben Ordner wie `main_bot.py` sein!

> Ab hier folgt keine Quick-Start-Vorbereitung mehr!

### Weitere Vorbereitung:
6. Hinzufügen oder Entfernen von Kryptowährungen, indem Teile des Codes kopiert oder entfernt werden – oder die Kryptowährung im Link ersetzt wird.

## Kompatibilität:

### Client-Betriebssysteme:
| Betriebssystem | Version                | Test-Ergebnis    |
|:--------------:|:----------------------:|:----------------:|
| Windows        | Windows 10             | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| Windows        | Windows 11             | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| Arch Linux     | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| CentOS         | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Debian         | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Elementary OS  | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Fedora         | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Gentoo Linux   | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Kali Linux     | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS Mojave   | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS High Sierra | neueste Version      | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| macOS Sierra   | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| OS X El Capitan | neueste Version       | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |

> Getestet: ![funkt](https://img.shields.io/badge/checks-passing-green) | Noch nicht getestet: ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red)

### Server-Betriebssysteme:
| Betriebssystem | Version                | Test-Ergebnis    |
|:--------------:|:----------------------:|:----------------:|
| Ubuntu         | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |
| Debian         | neueste Version        | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| Windows Server | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |

> Getestet: ![funkt](https://img.shields.io/badge/checks-passing-green) | Noch nicht getestet: ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red)

### Compiler-Version:
| Compiler       | Version                | Test-Ergebnis    |
|:--------------:|:----------------------:|:----------------:|
| Python         | 3.9                    | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| Python         | 3.10                   | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| Python         | neueste Version        | ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red) |

> Getestet: ![funkt](https://img.shields.io/badge/checks-passing-green) | Noch nicht getestet: ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red)

### Verwendete Bibliotheken:
| Bibliothek     | Version                | Test-Ergebnis    |
|:--------------:|:----------------------:|:----------------:|
| datetime       | neueste Version        | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| requests       | neueste Version        | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| pycord         | neueste Version        | ![funkt](https://img.shields.io/badge/checks-passing-green) |
| asyncio        | neueste Version        | ![funkt](https://img.shields.io/badge/checks-passing-green) |

> Getestet: ![funkt](https://img.shields.io/badge/checks-passing-green) | Noch nicht getestet: ![nicht getestet](https://img.shields.io/badge/checks-not%20tested-red)

## Lizenz:

Die Lizenz zur weiteren Verwendung dieses Projektes wird durch das **Creative Commons**-Modell geregelt.  
Falls du die Verwendung in einer Weise planst, die nicht durch die hier angegebenen Lizenzen abgedeckt ist oder du eine andere Verwendung wünschst, musst du vor der Nutzung des Projektes meine Zustimmung einholen.

| Verwendet | Piktogramm | Bezeichnung | Verlinkung |
|:--------:|:----------:|:-----------:|:---------:|
| :x:      | ![Lizenz_eins](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png) | Namensnennung 4.0 International | [Details](https://creativecommons.org/licenses/by/4.0/legalcode.de) |
| :x:      | ![Lizenz_zwei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png) | Namensnennung-ShareAlike 4.0 International | [Details](https://creativecommons.org/licenses/by-sa/4.0/legalcode.de) |
| :x:      | ![Lizenz_drei](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nd.png) | Namensnennung-Keine Bearbeitungen 4.0 International | [Details](https://creativecommons.org/licenses/by-nd/4.0/legalcode.de) |
| :x:      | ![Lizenz_vier](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc.eu.png) | Namensnennung-Nicht kommerziell 4.0 International | [Details](https://creativecommons.org/licenses/by-nc/4.0/legalcode.de) |
| :heavy_check_mark: | ![Lizenz_fünf](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.eu.png) | Namensnennung-Nicht kommerziell-ShareAlike 4.0 International | [Details](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.de) |
| :x:      | ![Lizenz_sechs](http://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.eu.png) | Namensnennung-Nicht kommerziell-Keine Bearbeitungen 4.0 International | [Details](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.de) |

> Verwendete Lizenz: :heavy_check_mark: | Nicht verwendete Lizenzen: :x:
