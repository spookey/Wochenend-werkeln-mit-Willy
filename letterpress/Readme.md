Letterpress Megaphony
=====================

So richtig Python kann ich ja nicht, aber da nur Übung den Meister macht habe ich mal eben ein kleines Script geschrieben, dass einem so richtig arg bei Letterpress schummeln lässt..

**Du willst auch schummeln?**
*Dann brauchst du ein Wörterbuch!*

Als erstes wird die Letterpress.ipa mit dem Entpacker des Vertrauens ausgepackt, dann finden sich unter ./Payload/Letterpress.app/o/ eine menge Textdateien. Dies ist das Wörterbuch für Letterpress.

Um sich sein eigenes zu backen reicht eigentlich

`cat *.txt > dict.txt`

Die dict.txt kommt zusammen mit dem Script in den selben Pfad, dann müsste alles laufen.
Als Resultat werden Textdateien mit möglichen Kombinationen (über 8 Buchstaben) erzeugt.


Viel Spaß!
	
	/*
	* ----
	* "THE BEER-WARE LICENSE" (Revision 42):
	* <frieder.griesshammer@der-beweis.de> wrote this file. As long as you retain this notice you
	* can do whatever you want with this stuff. If we meet some day, and you think
	* this stuff is worth it, you can buy me a beer in return. Frieder Griesshammer
	* ----
	*/
