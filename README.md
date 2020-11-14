# picture-labelling
Rotating and labelling pictures

src/prediction.ipynb contains python script (in notebook format atm) that takes images from one folder, predicts them, renames them with label and certainty (e.g. img.jpg --> img_class1_98.jpg) and writes to another folder.

&nbsp;

Don't train on your laptop.

Example model under src/pickle/ 

### Setup
In docker-compose.yml change your volumes

### Run
```docker-compose up```
