# Metrics and kaggle

## Metrics

Precision - процент объектов первого класа среди найденных классификатором как первый класс

$$\text{Precision} = \frac{\text{true positives}}{\text{false positives} + \text{true positives}}$$

Recall (полнота) - процент найденных объектов 1 класса среди всех объектов первого класса

$$\text{Recall} = \frac{\text{true positives}}{\text{false negative} + \text{true positives}}$$

![pr_recall](pre_rec.PNG)

## Решающие деревья

Хотим получить критерий разбиение, чтобы более чистые вершины после разбиения получались:

$\frac{L}{Q}H(p_L)+\frac{R}{Q}H(p_R) \rightarrow \min$

* Энтропия $H(q) = -q \log q - (1-q) \log (1-q)$
* Индекс Джини $H(q) = 4q(1-q)$
* Misclassification error

### params, параметры дерева

* Критерий
* Глубина
* минимальный разрмер листа
* стратерия разделения
