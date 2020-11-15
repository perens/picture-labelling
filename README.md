# picture-labelling
Rotating and labelling pictures

```prediction.ipynb``` contains python script (in notebook format atm) that takes images from one folder, predicts the images, renames them with predicted label and certainty (e.g. img.jpg --> img_class1_98.jpg) and writes to another folder.

&nbsp;

Don't train on your laptop.

Example model under src/resources/

### Docker Setup
In docker-compose.yml change your volumes

### Docker Run
```docker-compose up```

### Prediction Setup
In ```conf.ini``` set:
- input_folder - location of images to predict
- output_folder - root folder for predicted (will be created if doesn't exist)
- model_folder - folder where model is/are
- model_name - name of the trained model

### Predicting
If ```conf.ini``` is set, open ```prediction.ipynb``` and ```Run All```
