from huggingface_hub import login, snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer

import os
os.environ["HF_ENDPOINT"]="https://hf-mirror.com"

acc_tok = ""
login(token=acc_tok)

model_id = "Qwen/Qwen2.5-VL-3B-Instruct"
model_save_path = model_id.split("/")[-1]

model_local_dir = snapshot_download(
    repo_id=model_id,
    local_dir=model_save_path,
    use_auth_token=acc_tok,
)

print(f"== {model_id} huggingface downloading success ==")
