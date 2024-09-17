#include <Servo.h> 
 
Servo myservo; 
Servo myservoDos; 
Servo myservoTres; 
Servo myservoCuatro; 
Servo myservoCinco;  //creamos un objeto servo 
 
void setup() { 
  myservo.attach(3);
  myservoDos.attach(5); 
  myservoTres.attach(6); 

  

   Serial.begin(9600);
} 
 f:\pruebUnoServosArms\pruebUnoServosArms.ino
void loop() { 
  int poUno = analogRead(A0);  // realizamos la lectura del potenciometro
  int anguloUno = map(poUno, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180
  int poDos = analogRead(A1);  // realizamos la lectura del potenciometro
  int anguloDos = map(poDos, 0, 1023, 0 , 180);  // escalamos la lectura a un valor entre 0 y 180
  int poTres = analogRead(A2);  // realizamos la lectura del potenciometro
  int anguloTres = map(poTres, 0, 1023, 0 , 180);  // escalamos la lectura a un valor entre 0 y 180

  myservo.write(anguloUno);  // enviamos el valor escalado al servo
  myservoDos.write(anguloDos);  // enviamos el valor escalado al servo
  myservoTres.write(anguloTres);  // enviamos el valor escalado al servo
  
 
  Serial.print("ánguloUno:  ");
  Serial.println(anguloUno);
  Serial.println("////////////////////");

  Serial.print("ánguloDos:  ");
  Serial.println(anguloDos);
  Serial.println("//////////////////////");

  Serial.print("ánguloTres  :  ");
  Serial.println(anguloTres);
  Serial.println("//////////////////////");



  delay(1000);            
}