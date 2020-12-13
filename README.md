# picture-labelling
Rotating and labelling pictures

```prediction.py``` contains python script that takes images from one folder, predicts the images, renames them with predicted label and certainty (e.g. img.jpg --> img_class1_98.jpg) and writes to output folder.

&nbsp;

Example model under ```/src/resources/```

## Docker (If you don't want to run it on docker, proceed to 'Prediction setup')
### Docker Setup
In docker-compose.yml change your volumes

### Docker Run
```docker-compose up```

## Prediction Setup

### Setup (run if not using this repos docker)
```pip install -r requirements.txt```

### Configuration
Configuration file is in '/config/conf.ini’.

In ```conf.ini``` set:
- input_folder - folder with images to be predicted
- output_folder - folder where output images are placed (will be created if doesn't exist)
- model_folder - folder where the model resides
- model_name - name of the trained model (e.g. model.pkl)

### Predicting
#### Jupyter notebook
Open ```prediction.ipynb``` and ```Run All```
#### Python script
```python prediction.py```
