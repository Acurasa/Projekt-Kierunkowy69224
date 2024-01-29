### Projekt-Kierunkowy 69224 Leonid Stasyuk

Temat: Bot do handlu kryptowalut operujący na giełdach **Binance** oraz **Bitmex**.

***Technologie***:

Lang:

**Python**

System VC:

**Git** \ **Github**

CICD Pipeline(optional):

**Github Actions - Azure \ AWS**


## Na ten moment jest zrealizowana GUI wersja projektu.

Program posiada moduł /interface który odpowiada za input & output z programu. Render za pomocą standartowej biblioteki Tkinter 

![alt text](https://sun9-45.userapi.com/impf/GsOm-kvjNjqR3IXjxcNm9GLkm2y5a8iVdd-EnQ/e3-RxoVhVI4.jpg?size=1430x369&quality=96&sign=0f56de5a326a4b96c93b813f1457e39e&type=album)

## Zimplementowane Strategie :

**Breakout**

**Techniczna(Manualna,RSI-oriented)**

![alt text](https://sun9-78.userapi.com/impf/4TGe6IM3NJNqAkcNzuxxeUYC7IPA-wweBV-cqw/G4apk3bxFxE.jpg?size=1042x335&quality=96&sign=eb9a2949a33e2c5466b7040972729778&type=album)

## Binance \ Bitmex API

2 konektory **(binance_futures.py & bitmex.py)** odpowiadają za modele **REST & WEBSOCKET** zrealizowane w programie 

**https://binance-docs.github.io/apidocs/futures/en/#account-trades-endpoints**

**https://www.bitmex.com/app/apiOverview**

