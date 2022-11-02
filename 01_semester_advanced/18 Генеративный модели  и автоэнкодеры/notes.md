# Generative models, autoencoders

## old ones - discriminative models

hard to create new data

## generative models

* need different models
* data is not distributed well in a unimodal way

## autoencoders

* encode into a latent space
* decode into original space
* calculate and estimate MSE with original picture

## denoising auto encoders

* add artificual corruption -  compare with original

## anomaly detection with AE

* train AE
* after training $\rightarrow$ good MSE
* detect large MSE (>threshold) - anomaly

## Variational autoencoder

* estimate distribution of latent variables
* sample from distributions one point in latent space
* decode
* calculate loss

* minimize $L_{KL} = \frac{1}{2}(\sigma_i - \log{\sigma_i} - 1 + \mu_i^2)$

при $\mu_i^2 = 0$, min at ${\sigma_i} = 0$

Зачем нужно - похожесть распределений.

### дивергенция

* 0 для распределения и его самого
* не отрицательная
* дивергенция не симметрична (из p to q, not equal to q to p)
* правило треугольника не выполняется

#### KL дивергенция - популярный выбор

#### VAE Loss

* борется с тем что автоэнкодер все точки в латентном пространстве собирает в точку, а отличные - максимально далего
* этот лосс пробует заставить быть кодирование более компактным и круглым 

$L = L_{rec} + \beta \cdot L_{KL}$

Правая часть лосса - собирает точки ближе, а левое - раскидывать