#include <Servo.h> 
 //PRUEBAS CON POTENCIÓMETRO
Servo myservoUno; //Base
Servo myservoDos; //Altura
Servo myservoTres; //Estiramiento 
Servo myservoCuatro; //Rotación garra
Servo myservoCinco; //Garra

void setup() { 
  myservoUno.attach(3); 
  myservoDos.attach(5);
  myservoTres.attach(6);
  myservoCuatro.attach(9);
  myservoCinco.attach(10);
  Serial.begin(9600);
} 
 
void loop() { 
  int poUno = analogRead(A0);  // realizamos la lectura del potenciometro
  int anguloUno = map(poUno, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180

  int poDos = analogRead(A1);  // realizamos la lectura del potenciometro
  int anguloDos = map(poDos, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180

  int poTres = analogRead(A2);  // realizamos la lectura del potenciometro
  int anguloTres = map(poTres, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180

  int poCuatro = analogRead(A3);  // realizamos la lectura del potenciometro
  int anguloCuatro = map(poCuatro, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180

  int poCinco = analogRead(A4);  // realizamos la lectura del potenciometro
  int anguloCinco = map(poCinco, 0, 1023, 0, 180);  // escalamos la lectura a un valor entre 0 y 180

  myservoUno.write(anguloUno);  // enviamos el valor escalado al servo
  myservoDos.write(anguloDos);  // enviamos el valor escalado al servo
  myservoTres.write(anguloTres);  // enviamos el valor escalado al servo
  myservoCuatro.write(anguloCuatro);  // enviamos el valor escalado al servo
  myservoCinco.write(anguloCinco);  // enviamos el valor escalado al servo
  Serial.print("ánguloUno:  ");
  Serial.println(anguloUno);  
  Serial.println("////////////////////");
  Serial.print("ánguloDos:  ");
  Serial.println(anguloDos);  
  Serial.println("////////////////////");
  Serial.print("ánguloTres:  ");
  Serial.println(anguloTres);  
  Serial.println("////////////////////");
  Serial.print("ánguloCuatro:  ");
  Serial.println(anguloCuatro);  
  Serial.println("////////////////////");
  Serial.print("ánguloCinco:  ");
  Serial.println(anguloCinco);  
  Serial.println("////////////////////");
  delay(1000);                
}