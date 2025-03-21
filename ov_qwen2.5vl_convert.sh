export HF_ENDPOINT=https://hf-mirror.com

optimum-cli export openvino --model Qwen/Qwen2.5-VL-3B-Instruct --task image-text-to-text  ov-Qwen2.5-VL-3B-Instruct
# optimum-cli export openvino --model Qwen/Qwen2.5-VL-3B-Instruct --task image-text-to-text --weight-format int4  ov-Qwen2.5-VL-3B-Instruct-INT4