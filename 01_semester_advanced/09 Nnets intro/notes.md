# Neural networks

## backpropagation

* x -> linear model -> $\sigma (h)$ -> logistic reg -> pred

## terminology

* layers
  * dense/linear/FC layer
  * nonlinear layer
  * input layer, output layer
  * additional

* activation function - applied to layer output

  * sigmoid
    $\frac{1}{1+e^a}$
  * $\tanh$
  * ReLU
  $max(0, a)$
  * leaky ReLU
  $max(0.01a, a)$
  * leaky ReLU
  $max(\alpha a, a)$
  * exponential Linear unit
  * any other

использовать ReLU, если не знаем, если знаем - брать что нужно, не использовать сигмойду

* Backprop == chain rule

## полносвязная нейронка

задача минимизации

$$\frac{1}{l}\sum_{(x,y) \in X_{\text{train}}}{logloss(y,p(x,\Theta))} \rightarrow \min_{\Theta}$$
