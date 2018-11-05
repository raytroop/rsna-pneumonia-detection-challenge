import math
import pydicom
import matplotlib.pyplot as plt

def display_dicom(imgID):
    if not isinstance(imgID, (list, tuple)):
        imgID = [imgID]
    n = len(imgID)
    c = math.ceil(math.sqrt(n))
    r = math.ceil(n / c)
    fig, axs = plt.subplots(nrows=r, ncols=c, squeeze=False, gridspec_kw = {'wspace':0, 'hspace':0})
    for img_id, ax in zip(imgID, axs.flatten()):
        ds = pydicom.read_file(img_id)
        image = ds.pixel_array
        ax.imshow(image, cmap='gray')
        ax.set_aspect('equal')
    fig.tight_layout()
    fig.subplots_adjust(wspace=0, hspace=0)
