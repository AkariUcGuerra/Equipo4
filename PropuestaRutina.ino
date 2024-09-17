 #include <Servo.h> 
 
Servo myservo; 
Servo myservoDos; 
Servo myservoTres; 
Servo myservoCuatro; 
Servo myservoCinco;  //creamos un objeto servo 
byte sabor=0;

void setup() { 
  myservo.attach(3); 
  myservoDos.attach(5); 
  myservoTres.attach(6); 
 
} 

//Función para el inicio
void inicio() {
  delay(1000);
  myservo.write(90);  
  delay(1000);
  myservoDos.write(90);
  delay(1000);
  myservoTres.write(150);
  delay(1000);
}

//Función para recoger
void recoger() {
  delay(1000);
  myservo.write(178);  
  delay(1000);
  myservoDos.write(100);
  delay(1000);
  myservoTres.write(140);
  delay(1000);
}

void loop() {
  //Este solo es mientras esta lo de la red (aun no estan los azules)
  sabor=1;
  
  //Sabor 1
  if(sabor==1){
    inicio();
    recoger();
    myservo.write(178);  
    myservoDos.write(100);
    myservoTres.write(127);
    //Entregar
    myservo.write(110);  
    myservoDos.write(80);
    myservoTres.write(125);
    inicio();

  }

  //Sabor 2
  if(sabor==2){
    inicio();
    recoger();
    myservo.write(178);  
    myservoDos.write(100);
    myservoTres.write(127);
    //Entregar
    myservo.write(90);  
    myservoDos.write(80);
    myservoTres.write(125);
    inicio();

  }

  //Sabor 3
  if(sabor==3){
    inicio();
    recoger();
    myservo.write(178);  
    myservoDos.write(100);
    myservoTres.write(127);
    //Entregar
    myservo.write(50);  
    myservoDos.write(80);
    myservoTres.write(125);
    inicio();

  }

  //Sabor 4
  if(sabor==4){
    inicio();
    recoger();
    myservo.write(178);  
    myservoDos.write(100);
    myservoTres.write(127);
    //Entregar
    myservo.write(20);  
    myservoDos.write(80);
    myservoTres.write(125);
    inicio();

  }

 
}
