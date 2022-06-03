# ITASCII2HDF5

Speichern von InfraTec ASCII-Bildreihen in HDF5.

## Warum?

HDF5 ist quelloffen und lässt sich problemlos mit vielen Programmiersprachen öffnen (bspw. Python und Matlab). Der Speicherplatz ist deutlich geringer (ungefähr 1/7 der ASCII-Dateien). Die Bilder lassen sich einzeln aus dem Containerformat öffnen, d. h. wenn man sich ein Bild anschauen möchte, muss man nicht immer alle in den Arbeitsspeicher laden. Zudem werden die Metadaten direkt mitgespeichert.

## Wie?

Die ASCII-Dateien müssen mittels IRBIS3 exportiert werden (Reiter Sequenz -> Export). 

Es muss eine aktuelle Python 3 Version installiert werden. Anschließend mittels pip die fehlenden Pakete installieren:

```bash
pip install -r requirements.txt
```

Das Skript [ASCII2HDF.py](https://github.com/MT-MRT/ITASCII2HDF5/blob/main/ASCII2HDF.py) wandelt vorhandene ASCII-Dateien um. Dort muss der Ordner ausgewählt werden, in dem alle zusammenzuführenden ASCII-Dateien liegen. Bitte keine anderen Dateien im Ordner speichern. Außerdem den Dateinamen wählen. Anschließend kann das Skript gestartet werden:

```bash
cd pfad/zu/dem/skript
python3 ASCII2HDF.py
```

[openHDF.py](https://github.com/MT-MRT/ITASCII2HDF5/blob/main/openHDF.py) zeigt ein Beispiel, wie mit Python alle Bilder in einem HDF5-Container nacheinander geöffnet und angezeigt werden.
