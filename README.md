
# Tracking

A biblioteca **Tracking** é projetada para facilitar o rastreamento de características do corpo em imagens com **Mediapipe**. Ela fornece uma estrutura organizada para manipular e acessar pontos de referência, bem como suas coordenadas em 2D e 3D.



## Instalação

Para instalar a biblioteca, utilize o seguinte comando:

```bash
  pip install tracking
```
    
## Exemplos

Desenhando as mãos de uma imagem local
```python
import cv2
from tracking.hand_tracking import Tracking # Importando apenas o módulo de hand_tracking

# Carregando uma imagem
image = cv2.imread('path/to/image.jpg')

# Instanciando a classe de tracking
hand_tck = Tracking()

# Busca todas as mãos na imagem
hands = hand_tck.predict(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
for hand in hands:
    hand.draw(image, (255, 0, 0)) # Desenha todas as mãos encontradas

cv2.imshow("Hand(s)", image) # Mostrar imagem
cv2.waitKey() # Esperar o usuario clicar alguma tecla
cv2.destroyAllWindows()
```

Desenhando cada dedo separadamente e detectando quais dedos estão levantados
```python
import cv2
import tracking as tck

# 1° parametro: Define o tamanho da tela
# 2° parametro: Define a webcam que será usada
# 3° parametro: Define quais tipos de tracking deve carregar os modulos
tck.init((1920, 1080), 0, flags=tck.type.HAND_TRACKING)

# Instancia a classe de tracking de mãos
hand_tck = tck.HandTracking(tck.running_mode.LIVE_STREAM,   # running_mode = LIVE_STREAM para rastrear de forma assincrona
                            max_num_hands=2)                # max_num_hands = 2 Para rastrear até duas mãos ao mesmo tempo
cap = tck.CONFIG.VIDEO_CAPTURE # Referencia para a webcam

# Enquanto webcam estiver aberta
while cap.isOpened:
    # Obtem todas as mãos na camera (side_mirror=True se a imagem estiver invertida)
    hands = hand_tck.predict(side_mirror=True)

    # Ultimo frame que foi capturado
    frame = cap.frame

    for hand in hands:
        for finger in tck.finger:
            # Cor azul caso o dedo estiver levantado, senão, cor vermelha
            color = (255, 0, 0) if hand.finger_is_raised(finger) else (0, 0, 255)
            # Desenha apenas o dedo atual do loop
            hand.draw(frame, color, palm=False, fingers=[finger])

    # Mostra a imagem
    cv2.imshow("WebCam", frame)
    if cv2.waitKey(10) & 0xFF == 27:    # Se apertar Esc
        cap.close()                     # Fecha a webcam

cv2.destroyAllWindows() # Fecha a janela aberta pelo programa
```


## Autores

| ilunnie | marcoshrb |
| :---: | :---: |
| [![ilunnie](https://github.com/ilunnie.png?size=115)](https://github.com/ilunnie) | [![marcoshrb](https://github.com/marcoshrb.png?size=115)](https://github.com/marcoshrb) |


## Licença

[Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)

