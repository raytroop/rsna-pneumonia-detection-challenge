import glob
import matplotlib.pyplot as plt
from utils import display_dicom


imgs = glob.glob('dataset/stage_1_train_images/*.dcm')
imgs = imgs[:9]
display_dicom(imgs)
plt.show()