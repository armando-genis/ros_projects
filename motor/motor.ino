int valor;

const int channelPinA = 2;
const int channelPinB = 3;
int valorAnterior = 0;
int valorActual;
int value_channelB;
bool estado;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  // encoder pines
  pinMode(channelPinA, INPUT_PULLUP);
  pinMode(channelPinB, INPUT_PULLUP);
  
  Serial.begin(9600); // open the serial port at 9600 bps:
  // Interrupt
  attachInterrupt(digitalPinToInterrupt(channelPinA), doEncodeA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(channelPinB), doEncodeB, CHANGE);

}

void loop() {
  // put your main code here, to run repeatedly:
  valor = analogRead(A0)/4.01176;
  analogWrite(13, valor);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
  Serial.print(analogRead(A0));
  Serial.print(" -> ");
  Serial.print(valor);
  Serial.print(" -- Sentido:");
  Serial.print(estado);
  Serial.println("");
  



}

void doEncodeA()
{

  valorActual = digitalRead(channelPinA); 

  if (valorActual != valorAnterior) {
    // Serial.println("Son distintos");
    if (valorActual == value_channelB)
      {
        // Izquierda
        estado = 0;
      }
    if (valorActual != value_channelB)
      {
        // Derecha
        estado = 1;
      }
  }  
  else{
    // Serial.println("Son iguales");
  }
    
  valorAnterior = valorActual;

}
void doEncodeB()
{
  value_channelB = digitalRead(channelPinB); 

}
