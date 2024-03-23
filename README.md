# kiwi2Radio
![sysoverview](https://github.com/BM45/kiwi2Radio/blob/main/pics4www/systemoverview.jpg)

kiwi2Radio ist ein in Python geschriebener experimenteller HF-Mapper und KiwiSDR-Abstimmprogramm für alte Radios. Das Prinzip ist eine plattformunabhängige Abwandlung der inet2RF - Funktion aus den Projekten iRadio/iRadioMini und iRadioAndroid. https://github.com/BM45/iRadioAndroid#aussendung-des-internetradioprogramms-an-alte-radios

Durch die Rückführung des Ausgabesignals eines irgendwo auf der Welt stehenden KiwiSDR - entsprechend der eingestellten Frequenz eines lokalen Radios - entsteht der Eindruck, als würde man mit dem heimischen Empfänger durch die Radiobänder entfernter Länder kurbeln. Die Rückführung des Signals kann dabei in NF-, ZF- oder HF-Lage für das lokale Radio erfolgen, je nach verwendeter Technik. Zur Erfassung der Lokaloszillatorfrequenz des Radios sollte ein Frequenzzähler/Frequenzmesser benutzt werden, der den erfassten Wert über eine serielle Schnittstelle zu kiwi2Radio übertragen kann. Für ein authentisches Abschtimmgefühl sollte dabei die Grenze von 10 Messwerten pro Sekunde nicht unterschritten werden. Die Übertragung des Messwertes erfolgt an kiwi2Radio standardmäßig in 115200 Bit/s über '/dev/ttyUSB0'. Beide Parameter können jedoch über Aufrufparameter verändert werden. 

Die Übertragung des Frequenzwertes erfolgt als Float-Wert mit dem Kommando FRX=Lo_Frequenz in einer Auflösung bis drei Nachkommastellen. In einer typischen Arduino-Anwendung kann dies also mit dem Befehl `Serial.println("FRX="+String(f));` erreicht werden.


### Installation / Aufruf

Da kiwi2Radio in Python geschrieben ist, benötigt man auf dem ausführenden Rechner eine Python3-Umgebung (inklusive python3-tk und der Audiobibliothek portaudio).
Zusätzlich werden die Python-Libs pyserial numpy scipy sounddevice pygame requests xmltodict justext benötigt. Diese Erweiterungen kann man zum Beispiel über das Kommando pip install nachrüsten (pip für Python muss dafür installiert sein).

Nach dem Klonen sollten die Python-Scripte (sofern sie das nicht schon sind) im Ordner kiwi2Radio ausführbar gemacht werden.

`cd kiwi2Radio` 

`chmod +x *.py`


Die eigentliche Clientsoftware kiwi2Radio.py kann unterschiedlich aufgerufen werden:

`./kiwi2Radio.py  --kiwiserver Serveradresse --kiwiport Port_des_KiwiSDR`

Änderungen an der Schnittstelle für die Zuführung der Messergebnisse des Lokalsozillator werden durch die Parameter --serialdev=PORT und --serialbitrate=RATE erreicht.
Informationen zu weiteren Parametern erhält man mit dem Aufruf von `./kiwi2Radio.py --help`


Nach dem Start sieht man die Benutzeroberfläche des Empfängers. 

![clientview](https://github.com/BM45/kiwi2Radio/blob/main/pics4www/clientview.jpg)

Den aktuell gemessenen Frequenzwert des lokalen Radios sieht man numerisch im oberen Hauptbereich der Anwendung und grafisch durch dem Marker in der Spektrumsanzeige. Mit der Taste z kann zwischen laufender und zentrierter Anzeige des Markers gewechselt werden. Die Demodulationsart wird automatisch der aktuell eingestellten Frequenz angepasst, händische Übersteuerungen sind durch Tastendrücke möglich. Eine Übersicht gibt es im HELP-Menu. 

Man kann kiwi2Radio auch mit einer Liste von akutellen KiwiSDRs starten. Dazu muss zunächst mit

`./kiwiinternetdb.py`

eine aktualisiere Liste von KiwiSDRs angelegt werden. 

Danach kann kiwi2Radio einfach durch den Aufruf 

`./kiwi2Radio.py` 

gestartet werden. Der zu verbindende Server wird im Anschluss ausgewählt.

![clientdbview](https://github.com/BM45/kiwi2Radio/blob/main/pics4www/clientdbview.jpg)

Über die Taste Q kann während des laufenden Betriebs auf andere weltweite Server umgeschaltet werden (sofern diese freie Plätze haben). Am lokalen Radio hat man damit die Möglichkeit für vergleichenden Empfang auf unterschiedlichen Erdteilen.



