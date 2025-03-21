# OpenVINO enable QWen2.5VL Multimodal model

Requirement : Init environment 
```
pip install -r requirements.txt
```
- Step 1. HF model downloading 

```
python hf_qwen2.5vl_download.py
# Need to use HF access token for the code below to run.
```
- Step 2. OpenVINO model convert 
```
./ov_qwen2.5vl_convert.sh
```
- Step 3. OpenVINO model inference
```
python ov_qwen2.5vl_infer.py
```