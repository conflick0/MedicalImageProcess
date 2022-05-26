# MedicalImageProcess
## Install
```bash
conda create -n MedicalImageProcess python=3.9
```
```bash
conda activate MedicalImageProcess
```
```bash
pip install -r requirements.txt
```
## Usage
```python
from utils import convert as cvt
ptn_path = r'seg_512_512_267.ptn'
nrrd_path = r'seg_512_512_267.nrrd'
header = {
    'space': 'left-posterior-superior',
    'space directions': [
        [0.37695312, 0, 0], 
        [0, 0.37695312, 0], 
        [0, 0, 0.5]
    ],
    'space origin': [-67.31152344, -279.31152344, -293],
}
cvt.ptn2nrrd(ptn_path, nrrd_path, ptn_shape=(512, 512, 267), header=header)
```