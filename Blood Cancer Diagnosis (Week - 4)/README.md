# Report for Week - 4

## Aim

Finding a suitable model for classification of leukemic B-lymphoblast cells from normal B-lymphoid precursors from blood smear microscopic images.

## Approach

This week, I have used some other approaches to classify our images, following are the details of different models used:


### ResNext Architecture 

To classify our images, we have used this ResNext network architecture and it gave a accuracy of about ~68%. 
Though it is not a significant development from our previous networks used, I will not go more deep in this architecture here. 


### SeResnext Architecture

SeResnext model, this model is giving a super good accuracy of about 90% or more just after 10-15 epochs. This is a significant development regarding our other models used with highest accuracy being 79% for VGG19 model. 
This SeResnext model seems to be the best model tried on this dataset till now by me. 

#### Training Accuracy vs Validation Accuracy for SeResnext model

![](/images/TAccuracyvsVAccuracy.jpeg)