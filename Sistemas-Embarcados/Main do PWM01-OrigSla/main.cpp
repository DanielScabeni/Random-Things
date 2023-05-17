void main()
{
  // Configura o pino RB0 (LED) como saída
  TRISB.f0 = 0;
  // Configura o pino RB1 (botão) como entrada
  TRISB.f1 = 1;
  // Inicializa o LED desligado (LOW)
  PORTB.f0 = 0;
  
  while (1)
  {
    // Lê o estado do botão e armazena na variável 'buttonState'
    unsigned char buttonState = PORTB.f1;
    // Verifica se o botão está pressionado
    //(assumindo que o botão é ativo em nível baixo)
    if (buttonState == 0)
    {
      // Liga o LED (HIGH)
      PORTB.f0 = 1;
    }
    else
    {
      // Desliga o LED (LOW)
      PORTB.f0 = 0;
    }
  }
}