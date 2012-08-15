#include "oinkoink.h"

// Pinbelegung
int spk = 7;	//Lautsprecher
int led = 8;	//Leuchte
int sw = 12;	//Schalter
int sws = 0;	//Zustand des Schalters
int stdd = 75;	//Standardmäßige Pause

int melodie[] = 
{	N_CS4, N_F4, N_GS4, 0, N_CS5, N_GS4, N_CS5
};

int dauer[] =
{	8, 8, 8, 128, 4, 8, 3
};

void jingle()
{	for(int ton = 0; ton < (sizeof(melodie)/sizeof(int)); ton++)
	{	int laenge = 1000/dauer[ton];
		int pause = laenge * 1.25;
		tone(spk, melodie[ton], laenge);
		delay(pause);
		noTone(spk);
  	}
  	ledblink(0);
}

void ledblink(int i)
{	if(i)
	{	tone(spk, N_CS5); delay(stdd); noTone(spk);
		tone(spk, N_GS4); delay(stdd); noTone(spk);
		tone(spk, N_CS5); delay(stdd); noTone(spk);
	}
	analogWrite(led, 255); delay(stdd);
	analogWrite(led, 0); delay((stdd * 4 / 3)); // Nette Art 100 zu schreiben, oder was?
	analogWrite(led, 255); delay(stdd);
	analogWrite(led, 0);

        delay(1000);
	
}

void setup()
{	pinMode(sw, INPUT);
	ledblink(1);
}

void loop()
{	sws = digitalRead(sw);
	delay(10);
	if(sws)
	{	jingle();
	}
}
