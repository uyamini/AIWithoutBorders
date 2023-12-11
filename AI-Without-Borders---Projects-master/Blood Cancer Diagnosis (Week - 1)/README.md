# Report for Week - 1

## Aim

Finding a suitable model for classification of leukemic B-lymphoblast cells from normal B-lymphoid precursors from blood smear microscopic images.

## Approach

After preprocessing the dataset, We have used various models for this problem and trained them on this data(two types of images) to classify the images into two types. The best approach for this problem turned out to be the VGG19 model, the reason behind this model getting much better accuracy than others is its architecture, the main key points of this architecture are as follows: 

*    Use of very small convolutional filters, e.g. 3×3 and 1×1 with a stride of one.
*    Use of max pooling with a size of 2×2 and a stride of the same dimensions.
*    The importance of stacking convolutional layers together before using a pooling layer to define a block.
*    Dramatic repetition of the convolutional-pooling block pattern.
*    Development of very deep (16 and 19 layer) models.

Since our dataset contains images of human cell(s), this model worked really well in classifying the images by learning even the very minor details due to its architecture.

The information about model used is defined in the table below:

| Model/Architecture | Type | Accuracy(in %) |
| --- | --- | --- |
| CNN | Raw | ~65 |
| ResNet50 | Pre-Trained | ~64 |
| VGG16 | Pre-Trained | ~77 |
| VGG19 | Pre-Trained | ~79 |
| Inception | Pre-Trained | ~64 |
