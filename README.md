# MedicalImageProcess
## Install
```bash
conda create -n MedicalImageProcess python=3.9
```
```bash
conda activate MedicalImageProcess
```
```bash
pip install requirements.txt
```
## Usage
```python
from utils import convert as cvt
ptn_path = r'segment_512_512_267.ptn'
nrrd_path = r'segment_512_512_267.nrrd'
cvt.ptn2nrrd(nrrd_path, ptn_path)
```