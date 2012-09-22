#include <Servo.h>

#define NL_POS 90

struct uber
{	int tpin;	//Taster Pin
	int pos;	//Position (0-180)
	int spin;	//Servo Pin
	Servo s;	//Servus
};

uber up = {2, NL_POS, 11};
uber down = {3, NL_POS, 11};
uber left = {4, NL_POS, 10};
uber right = {5, NL_POS, 9};

void stelle(struct uber u)
{	u.s.write(u.pos);
}

void lese(struct uber u)
{	int state = digitalRead(u.tpin);
	if((state == HIGH) && (u.pos <= 180))
	{	u.pos++;
	}
	else if(u.pos >= 0)
	{	u.pos--;
	}
	else
	{	return;
	}
}

void setup()
{	up.s.attach(up.spin);
	down.s.attach(down.spin);
	left.s.attach(left.spin);
	right.s.attach(right.spin);
}

void loop()
{ lese(up);	stelle(up);
	lese(down);	stelle(down);
	lese(left);	stelle(left);
	lese(right);	stelle(right);
}
