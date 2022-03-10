# Linear model

## grad descend

шаг градиентного спуска $$x = x -\alpha \triangledown f$$

* Шагать пока не будет близко к 0
* Пока не будет достаточно много шагов

### grad descend for linear regression

loss

$$L(w) = \sum_{i=1}^l{(X^T_i W - y_i)^2}$$

$$\frac{\partial L}{\partial w_1} = \sum^l_{i=1}{2(X^T_i W - y_i)x_{i1}}$$

## нормализация

$$ x^{new}_{ij} = \frac{x_{ij} - \mu_j}{\sigma_j} - плохо работает градиентный спуск и другие методы
