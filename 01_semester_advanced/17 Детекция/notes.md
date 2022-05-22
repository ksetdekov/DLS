# Детекция

## Лекция

### повторение классификаций

1. извлечение фичей - потом классификация
2. AlexNet - конф-пул
3. VGG - много сверточных блоков и 3 fc слоя
4. Inception - 1*1 свертка на снижение размерности, потом conv, добавили выходы к лоссу на середине сети 2 раза - вместо остатков
5. ResNet - residual connections
6. DenseNet
7. SENet (squeeze and excitation net)
8. MnasNet (NAS - neural architecture search) - подобранное нейронкой конфигурация сетей.
9. EfficientNet - b7 - почти лучшее
10. GhostNet - еще новое, но не очень большой скачек

### object detection

1. что надо предсказать
    1. есть координаты (top-left, right-bottom)
    2. есть класс
    3. есть уверенность

2. есть датасеты (MS coco, open images v6, остальные)
3. IOU
4. Что есть корректно?

    * TP - когда большой iou
    * FN - когда не нашли объект
    * FP - когда не тот класс, мало (IOU < 0.5) пересексли или не пересекли
5. P/R

    * $Precision = \frac{True Posisitive}{True Positive + False Positive}$
    * $Recall = \frac{True Posisitive}{True Positive + False Negatives}$

6. Когда много классов - confusion matrix
7. Mean average precision (mAP)
8. Сделаем простой детектор:
    1. У нас есть детектор хороший
    2. Пройдем скользящим окном по всей картинке с разной формой окна
    3. Выберем только боксы большой уверенности
    4. Получили результат

### 2 Stage detectors

#### core ideas

1. не генерировать боксы заранее, мы имеем заранее предположение о боксах (априорные) - нужно выбрать нужное нам подмножество боксов. Anchor boxes

2. регрессируем нужные боксы к нашему датасету (из всех боксов)

3. в каждом боксе - классификация

4. фильтруем плохие предсказания

Multitask

#### examples

1. two stage (proposal-based)
    * rcnn
    * fast rcnn
    * faster rcnn
    * mask rcnn
2. one stage
    * ssd
    * yolov3
    * dsod
    * rfbnet
3. point-based
    * centernet
    * cornernet
    * extremenet

#### what is 2 stage?

1. RCNN
    * генерация предположений (selective search)
    * warp to one shape
    * regress and classify them
    * post-process
2. Fast RCNN
    * extract feature map with cnn - get feature tensor - this is backbone
    * for each roi
        * multi class classification
        * bounding box regressor
3. Faster RCNN
    * RPN - region proposal network для предсказания выбора регионов
4. Mask RCNN
    * Добавили третью голову - mask head -  выдает instance segmentation (маску красит внутри)

#### one-stage detectors

SSD, YOLO

##### YOLO

you only look once

1. get features from a backbone network
2. predict feature map (grid)
3. predict boxes from grid
4. post-process predictions

##### conv recap

images -> feature maps

##### SSD

получилось несколько гридов (положений сети) и по ним предсказыванием положение классов. 

1. SSD pipeline
    1. input -> backbone
    2. backbone -> feature map
    3. feature map -> boxes locations and classes inside of them
2. detection task
    1. how many boxes?
    2. what should be the size of an input image
    3. how to train? (~how to make differentiable)

