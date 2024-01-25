from run_on_recommended_gpu.datasets import data_management
from run_on_recommended_gpu import __version__
from run_on_recommended_gpu.datasets import data_management

def test_version():
    assert __version__ == '0.4.16'

def test_get_image_id_dict():
    image_list = ["image_0005.nii.gz", "./abc/img_6.nii.gz", "image_0040.nii.gz"]
    id_dict = {
        5: "image_0005.nii.gz",
        6: "./abc/img_6.nii.gz",
        40: "image_0040.nii.gz"}
    result = data_management.get_image_id_dict(image_list)
    assert id_dict == result



def test_get_label_id_dict():
    image_list = ["lbl_0005.nii.gz", "./lbl/seg_6.nii.gz",
        "./lbl/seg_f0001_m0002.nii.gz"]
    id_dict = {
        5: "lbl_0005.nii.gz",
        6: "./lbl/seg_6.nii.gz",
        "f0001_m0002": "./lbl/seg_f0001_m0002.nii.gz"}
    result = data_management.get_label_id_dict(image_list)
    assert id_dict == result