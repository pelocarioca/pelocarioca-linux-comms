/*
  The circuit:
  - +V connection of the PING))) attached to +5V
  - GND connection of the PING))) attached to ground
  - SIG connection of the PING))) attached to digital pin 7


 VCC -> +5V
 Trig -> D3
 Echo -> D2
 Gnd -> Gnd

 Yellow -> D7
 Red -> +5V
 Brown -> Gnd

Para el código del sensor ultrasónico:
  created 3 Nov 2008
  by David A. Mellis
  modified 30 Aug 2011
  by Tom Igoe
  modified 15 Jan 2022
  by Cassiopea Acebes
*/

/*Se definen los pines que se van a 
utilizar y se declaran las variables
globales, también se incluye la 
librería de control del servo*/

#include <Servo.h>


#define echoPin 2 // Pin D2 (Echo)
#define trigPin 3 // Pin D3 (Trig)
#define servPin 7 // Pin D7 (Serv)

long duration; // Tiempo de viaje del sonido
int distancia; // Distancia detectada en cada instante

long s; // Cociente del detector
int base = 1184; // Distancia base del detector (zona de detección vacía)
int permisividad = 20; //Varianza de la distancia
int giro = 90; // Grados de giro del servo

/*Esta línea inicia el servo en la vabiable
servo, que se utilizará para su control*/

Servo servo;

void setup() {

  /*Se comienzan las salidas por consola 
  por el el terminal serial, de esta forma
  se podrán ver y analizar las lecturas que 
  tome el sensor, el estado del servo y otra 
  información de relevancia*/

  Serial.begin(9600);

  /*Para la toma de medidas se declaran los
  Pins del sensor como de salida y entrada
  y se le asigna al servo el pin definido
  
  El brazo del servo se pone a cero*/

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  servo.attach(servPin); //Servo al pin declarado

  servo.write(0); //Hace el cero del brazo del servo
  
}

/*Se declara el loop principal
del programa, en este se va a 
primero tomar una medida de la 
distancia al detector, se muestra
por el monitor serial y se declara 
el estado de la zona de detección.

Con este estado se mueve el brazo 
del servo los grados anteriormente
declarados.*/

void loop() {
  float average = calc_average();
  medir();
  bool state = detect(average, base);
  Serial.print("Cociente: ");
  Serial.print(s);
  Serial.print("  Distancia: ");
  Serial.print(distancia);
  Serial.print("  Average: ");
  Serial.println(average);
  
  mover(state, giro);
}

/*Esta función controla el movimiento
del servo, toma un valor booleano,
que se toma como el estado de la zona
y los grados que se va a mover el servo.
Segun el estado se abrirá el brazo o
se pondrá a cero*/

void mover(bool check,int grados){
  if (check) {
    //Serial.println("Accionando brazo.");
    servo.write(grados);
  } else {
    //Serial.println("Recogiendo brazo.");
    servo.write(0);
  }
}

/*Esta función controla la detección
de personas en la zona de detección.
Toma como valores la distancia medida
en un momento determinado y la compara 
con la base declarada. Usando la 
fórmula anteriormente descrita emite
un true para la detección y un false
como estado natural*/

bool detect(long detect, int base){
    s = pow(((detect - base)/permisividad), 2);
    if (s >= 1){
        return true;
    } else {
        return false;
    }
} 

/*Esta función controla el sensor 
y determina la distancia en todo 
momento, para ello baja el voltaje 
del pin de trigger, le da un pequeño
delay y lo activa durante un breve
período de tiempo, tras el cual 
vuelve a bajar su voltaje.

Una vez hecho esto lee la subida 
de voltaje por el pin de echo, este
será el tiempo de la onda de sonido
en ir y volver del sensor, se calcula 
la distnacia como la mitad de la 
duración multiplicado por un cierto
cociente obtenido de: 
v(m/s)*1/1000(s/us)*100/1(cm/m) = 0.034(cm/us)*/

float calc_average()
{
  static float average = -1.0 ;
  if (average == -1.0)  // special case for first reading.
  {
    average = medir() ;
    return average ;
  }
  average += 0.25 * (medir() - average) ;  // 0.1 for approx 10 sample averate, 0.01 for 100 sample etc.
  return average ;
}

long medir(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(200);//200
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distancia = duration * 0.034 / 2; 
  return distancia;
}
