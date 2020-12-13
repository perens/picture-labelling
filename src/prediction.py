import configparser
import torchvision.transforms as tfms
from fastai.vision import *
from tqdm import tqdm

config = configparser.ConfigParser()
config.read('config/conf.ini')

model = load_learner(config['CONF']['model_folder'], config['CONF']['model_name'])

def get_rotation_degree(input_string):
    return int(''.join(filter(str.isdigit, input_string)))
    
def get_main_classification(input_string):
    return ''.join(filter(str.isalpha, str(input_string)))

def pil2fast(img):
    return vision.image.Image(pil2tensor(img, dtype=np.float32).div_(255))

def fast2pil(img):
    return tfms.ToPILImage()(img.data).convert("RGB")


input_folder = config['CONF']['input_folder']
output_folder = config['CONF']['output_folder']

for i in tqdm(os.listdir(input_folder)):
    img_fastai = open_image(os.path.join(input_folder, i))
    img_title, img_extension = os.path.splitext(i)
    pred_class, pred_idx, outputs = model.predict(img_fastai)
    prediction = (str(pred_class), round(max(outputs.numpy()) * 100))
    
    # 90 or 270 degrees, rotate and predict again
    rotate_degree = get_rotation_degree(str(pred_class))
    if rotate_degree in [90, 270]:
        img_pil = fast2pil(img_fastai)
        img_pil = img_pil.rotate(rotate_degree, expand=True)
        img_fastai = pil2fast(img_pil)

        pred_class, pred_idx, outputs = model.predict(img_fastai)
        prediction = (str(pred_class), round(max(outputs.numpy()) * 100))
        rotate_degree = get_rotation_degree(str(pred_class))
        
    # continue with rotation
    img_pil = fast2pil(img_fastai)
    img_pil = img_pil.rotate(360 - rotate_degree, expand=True)
    img_fastai = pil2fast(img_pil)
    
    # final prediction to get class and rotation for output
    pred_class, pred_idx, outputs = model.predict(img_fastai)
    prediction = (str(pred_class), round(max(outputs.numpy()) * 100))
    
    path_to_class = output_folder + "/" + get_main_classification(str(pred_class))
    
    if not os.path.exists(path_to_class):
        os.makedirs(path_to_class)
    
    new_img_title = img_title + "_" + prediction[0] + "_" + str(prediction[1]) + img_extension
    new_img_path = os.path.join(path_to_class, new_img_title)
    img_fastai.save(new_img_path)