# Report for Week - 3

## Aim

Finding a suitable model for classification of leukemic B-lymphoblast cells from normal B-lymphoid precursors from blood smear microscopic images.

## Approach

This week, I have used some other approaches to classify our images, following are the details of different models used:


### Capsule network 

To classify our images, we have used this capsule network architecture and it gave a accuracy of about ~66%. 
Though it is not a significant development, but since this architecture is different from our previously used VGG19, so I expect that it has learned the details differently and can increase our classifying accuracy if it is used with VGG19 model in ensembling.


### Densenet Architecture

We have used this architecture as it is also a very different approach from the other too, but there seems a problem with this model while training, I would be blunt enough to say that there might be some problem with my model training. The val_acc seems stuck at one particular value. I will update when any developments will be provided. It is giving a accuracy of ~65%.


### VGG19 Architecture

Since we have used this architecture before and there is not much to say about this model, this is giving us a nice accuracy of about 76%.


### Model Ensembling

We have used model "stacking" ensembling technique in our code so as to get the best out of all three models discussed above. After stacking the models in an ensemble, we got a accuracy of 79.9%.