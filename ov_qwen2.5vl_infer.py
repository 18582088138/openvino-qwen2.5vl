from optimum.intel.openvino import OVModelForVisualCausalLM

from PIL import Image
from transformers import AutoProcessor, AutoTokenizer
from qwen_vl_utils import process_vision_info
from transformers import TextStreamer
# from huggingface_hub import login, snapshot_download

import os
os.environ["HF_ENDPOINT"]="https://hf-mirror.com"

ov_model_path = "ov-Qwen2.5-VL-3B-Instruct-INT4"
device="CPU"
min_pixels = 256 * 28 * 28
max_pixels = 1280 * 28 * 28
image_path = "demo.jpeg"

model = OVModelForVisualCausalLM.from_pretrained(ov_model_path, device=device)
processor = AutoProcessor.from_pretrained(ov_model_path, min_pixels=min_pixels, max_pixels=max_pixels)

image = Image.open(image_path)
question = "Describe this image."


messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": f"file://{image_path}",
            },
            {"type": "text", "text": question},
        ],
    }
]

text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)


# display(image)
print("Question:")
print(question)
print("Answer:")

generated_ids = model.generate(**inputs, max_new_tokens=100, streamer=TextStreamer(processor.tokenizer, skip_prompt=True, skip_special_tokens=True))
