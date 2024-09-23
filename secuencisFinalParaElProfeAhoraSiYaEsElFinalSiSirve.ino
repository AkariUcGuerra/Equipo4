#include <Servo.h>
Servo servoUno;     //Base
Servo servoDos;     //Altura
Servo servoTres;    //Estira
Servo servoCuatro;  //Gira garra
Servo servoCinco;   //Abre o cierra garra
byte ang;
byte sabor;

void setup() {
  // put your setup code here, to run once:
  servoUno.attach(3);
  servoDos.attach(6);
  servoTres.attach(9);
  servoCuatro.attach(10);
  servoCinco.attach(11);
}

void moverServoSuave(Servo& servo, int posicionFinal, int tiempo) {
  byte posicionInicial = servo.read();                // Obtener la posición actual del servo
  byte pasos = abs(posicionFinal - posicionInicial);  // Calcular cuántos pasos hay que dar
  byte intervalo = tiempo / pasos;                    // Calcular el tiempo entre cada paso

  for (int i = 0; i <= pasos; i++) {
    // Calcular la nueva posición
    int nuevaPosicion = posicionInicial + (posicionFinal - posicionInicial) * i / pasos;
    servo.write(nuevaPosicion);  // Mover el servo a la nueva posición
    delay(intervalo);            // Esperar el tiempo entre pasos
  }
}

void inicio() {
  moverServoSuave(servoUno, 0, 500);      // Mover servoUno a 0 en 1 segundo
  moverServoSuave(servoDos, 90, 1000);     // Mover servoDos a 90 en 1 segundo
  moverServoSuave(servoTres, 120, 1000);   // Mover servoTres a 120 en 1 segundo
  moverServoSuave(servoCuatro, 90, 1000);  // Mover servoCuatro a 90 en 1 segundo
  moverServoSuave(servoCinco, 90, 1000);   // Mover servoCinco a 90 en 1 segundo
  moverServoSuave(servoCinco, 120, 1000);  // Mover servoCinco a 120 en 1 segundo
}


//Agarra boing y lo alza:
void agarrarBoing() {
  for (ang = 120; ang > 10; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoCinco.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 120; ang > 95; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoTres.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);

  for (ang = 90; ang > 49; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoCuatro.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 90; ang > 85; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoDos.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 0; ang < 50; ang++) {
    //manda el angulo al servo de 180  hacia 0
    servoUno.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 95; ang > 68; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoTres.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 10; ang < 130; ang++) {
    //manda el angulo al servo de 180  hacia 0
    servoCinco.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
  for (ang = 85; ang > 60; ang--) {
    //manda el angulo al servo de 180  hacia 0
    servoDos.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);

  for (ang = 68; ang < 120; ang++) {
    //manda el angulo al servo de 180  hacia 0
    servoTres.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);

  for (ang = 60; ang < 80; ang++) {
    //manda el angulo al servo de 180  hacia 0
    servoDos.write(ang);
    //Este delay controla la velocidad a la que se mueve
    delay(50);
  }
  delay(500);
}
void entrega() {
  if (sabor == 10) {
    delay(500);
    moverServoSuave(servoUno, 2, 1000);      // Mover servoUno a 0 en 1 segundo
    moverServoSuave(servoCuatro, 95, 1000);  // Mover servoCuatro a 90 en 1 segundo
    moverServoSuave(servoTres, 80, 1000);    // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 89, 1000);     // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoTres, 70, 1000);    // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 110, 1000);    // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoCinco, 10, 1000);   // Mover servoCinco a 90 en 1 segundo
    moverServoSuave(servoTres, 120, 1000);   // Mover servoTres a 120 en 1 segundo
  }
  delay(500);
  if (sabor == 20) {
    delay(500);
    moverServoSuave(servoUno, 24, 1000);      // Mover servoUno a 0 en 1 segundo
    moverServoSuave(servoCuatro, 124, 1000);  // Mover servoCuatro a 90 en 1 segundo
    moverServoSuave(servoTres, 80, 1000);     // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 89, 1000);      // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoTres, 65, 1000);     // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 110, 1000);     // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoCinco, 10, 1000);    // Mover servoCinco a 90 en 1 segundo
    moverServoSuave(servoTres, 120, 1000);    // Mover servoTres a 120 en 1 segundo
  }
  delay(500);
  if (sabor == 30) {
    delay(500);
    moverServoSuave(servoUno, 40, 1000);      // Mover servoUno a 0 en 1 segundo
    moverServoSuave(servoCuatro, 132, 1000);  // Mover servoCuatro a 90 en 1 segundo
    moverServoSuave(servoTres, 65, 1000);     // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 75, 1000);      // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoTres, 60, 1000);     // Mover servoTres a 120 en 1 segundo
    moverServoSuave(servoDos, 100, 1000);     // Mover servoDos a 90 en 1 segundo
    moverServoSuave(servoCinco, 10, 1000);    // Mover servoCinco a 90 en 1 segundo
    moverServoSuave(servoTres, 120, 1000);    // Mover servoTres a 120 en 1 segundo
  }
  delay(500);
}

void loop() {
  delay(3000);
  inicio();
  delay(3000);
  agarrarBoing();
  delay(3000);
  sabor = 30;
  delay(1000);
  entrega();
  delay(3000);
  inicio();
  delay(3000);
  agarrarBoing();
  delay(3000);
  sabor = 20;
  delay(1000);
  entrega();
  delay(3000);
  inicio();
  delay(3000);
  agarrarBoing();
  delay(3000);
  sabor = 10;
  delay(1000);
  entrega();
  delay(1000);
  
  
}
