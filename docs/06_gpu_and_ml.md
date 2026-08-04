# 06：GPU 与机器学习

覆盖模型训练、推理、生成式 AI、语音和计算生物学工作负载。

返回 [案例总览](README.md)。

## `06_gpu_and_ml/audio-to-text/whisperx_transcribe.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：WhisperX transcription with word-level timestamps
- **源码**：[打开 `06_gpu_and_ml/audio-to-text/whisperx_transcribe.py`](../06_gpu_and_ml/audio-to-text/whisperx_transcribe.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/audio-to-text/whisperx_transcribe.py`

## `06_gpu_and_ml/binder-design/esmfold2_binder_design.py`

- **作用**：调用计算生物学模型进行蛋白质折叠、结构预测或结合物设计。
- **源码原题**：Design protein binders at scale with ESMFold2 and ESMC
- **源码**：[打开 `06_gpu_and_ml/binder-design/esmfold2_binder_design.py`](../06_gpu_and_ml/binder-design/esmfold2_binder_design.py)
- **关键对象**：`modal.App`、`modal.FunctionCall`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/binder-design/esmfold2_binder_design.py`

## `06_gpu_and_ml/blender/blender_video.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Render a video with Blender on many GPUs or CPUs in parallel
- **源码**：[打开 `06_gpu_and_ml/blender/blender_video.py`](../06_gpu_and_ml/blender/blender_video.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/blender/blender_video.py`

## `06_gpu_and_ml/controlnet/controlnet_gradio_demos.py`

- **作用**：在 GPU 上运行图像生成或编辑模型，并提供命令行、API 或交互界面。
- **源码原题**：Play with the ControlNet demos
- **源码**：[打开 `06_gpu_and_ml/controlnet/controlnet_gradio_demos.py`](../06_gpu_and_ml/controlnet/controlnet_gradio_demos.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`@app.function`、`@modal.asgi_app`
- **常用启动方式**：`modal serve 06_gpu_and_ml/controlnet/controlnet_gradio_demos.py`

## `06_gpu_and_ml/dreambooth/diffusers_lora_finetune.py`

- **作用**：展示可恢复的模型训练或微调流程，并配置 GPU、检查点与依赖镜像。
- **源码原题**：Fine-tune Flux on your pet using LoRA
- **源码**：[打开 `06_gpu_and_ml/dreambooth/diffusers_lora_finetune.py`](../06_gpu_and_ml/dreambooth/diffusers_lora_finetune.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/dreambooth/diffusers_lora_finetune.py`

## `06_gpu_and_ml/embeddings/amazon_embeddings.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：Embed 30 million Amazon reviews at 575k tokens per second with Qwen2-7B
- **源码**：[打开 `06_gpu_and_ml/embeddings/amazon_embeddings.py`](../06_gpu_and_ml/embeddings/amazon_embeddings.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/amazon_embeddings.py`

## `06_gpu_and_ml/embeddings/image_embeddings_infinity.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：Modal Cookbook: Recipe for Inference Throughput Maximization
- **源码**：[打开 `06_gpu_and_ml/embeddings/image_embeddings_infinity.py`](../06_gpu_and_ml/embeddings/image_embeddings_infinity.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/image_embeddings_infinity.py`

## `06_gpu_and_ml/embeddings/liquidai_embeddings_server.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：Serve Liquid AI ColBERT embeddings with llama.cpp and Modal Servers
- **源码**：[打开 `06_gpu_and_ml/embeddings/liquidai_embeddings_server.py`](../06_gpu_and_ml/embeddings/liquidai_embeddings_server.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/liquidai_embeddings_server.py`

## `06_gpu_and_ml/embeddings/qdrant.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：qdrant
- **源码**：[打开 `06_gpu_and_ml/embeddings/qdrant.py`](../06_gpu_and_ml/embeddings/qdrant.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/qdrant.py`

## `06_gpu_and_ml/embeddings/text_embeddings_inference.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：Run TextEmbeddingsInference (TEI) on Modal
- **源码**：[打开 `06_gpu_and_ml/embeddings/text_embeddings_inference.py`](../06_gpu_and_ml/embeddings/text_embeddings_inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/text_embeddings_inference.py`

## `06_gpu_and_ml/embeddings/wikipedia/download.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：download
- **源码**：[打开 `06_gpu_and_ml/embeddings/wikipedia/download.py`](../06_gpu_and_ml/embeddings/wikipedia/download.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/wikipedia/download.py`

## `06_gpu_and_ml/embeddings/wikipedia/main.py`

- **作用**：构建文本或图像向量嵌入服务，关注批处理吞吐、索引或检索集成。
- **源码原题**：Embedding Containers Configuration
- **源码**：[打开 `06_gpu_and_ml/embeddings/wikipedia/main.py`](../06_gpu_and_ml/embeddings/wikipedia/main.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/embeddings/wikipedia/main.py`

## `06_gpu_and_ml/gpu_fallbacks.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Set "fallback" GPUs
- **源码**：[打开 `06_gpu_and_ml/gpu_fallbacks.py`](../06_gpu_and_ml/gpu_fallbacks.py)
- **关键对象**：`modal.App`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/gpu_fallbacks.py`

## `06_gpu_and_ml/gpu_snapshot.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Snapshot GPU memory to speed up cold starts
- **源码**：[打开 `06_gpu_and_ml/gpu_snapshot.py`](../06_gpu_and_ml/gpu_snapshot.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`@app.cls`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/gpu_snapshot.py`

## `06_gpu_and_ml/hyperparameter-sweep/hp_sweep_gpt.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Train an SLM from scratch with early-stopping grid search over hyperparameters
- **源码**：[打开 `06_gpu_and_ml/hyperparameter-sweep/hp_sweep_gpt.py`](../06_gpu_and_ml/hyperparameter-sweep/hp_sweep_gpt.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/hyperparameter-sweep/hp_sweep_gpt.py`

## `06_gpu_and_ml/image-to-video/image_to_video.py`

- **作用**：以 GPU 加速的生成模型将文本或图像转换为视频或三维场景。
- **源码原题**：Animate images with Lightricks LTX-Video via CLI, API, and web UI
- **源码**：[打开 `06_gpu_and_ml/image-to-video/image_to_video.py`](../06_gpu_and_ml/image-to-video/image_to_video.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/image-to-video/image_to_video.py`

## `06_gpu_and_ml/import_torch.py`

- **作用**：展示深度学习框架在 Modal Image 与远程 GPU Function 中的运行方式。
- **源码原题**：import torch
- **源码**：[打开 `06_gpu_and_ml/import_torch.py`](../06_gpu_and_ml/import_torch.py)
- **关键对象**：`modal.App`、`modal.Image`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/import_torch.py`

## `06_gpu_and_ml/langchains/potus_speech_qanda.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Retrieval-augmented generation (RAG) for question-answering with LangChain
- **源码**：[打开 `06_gpu_and_ml/langchains/potus_speech_qanda.py`](../06_gpu_and_ml/langchains/potus_speech_qanda.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Retries`、`modal.Secret`、`@app.function`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/langchains/potus_speech_qanda.py`

## `06_gpu_and_ml/llm-serving/chat_with_pdf_vision.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Chat with PDF: RAG with ColQwen2
- **源码**：[打开 `06_gpu_and_ml/llm-serving/chat_with_pdf_vision.py`](../06_gpu_and_ml/llm-serving/chat_with_pdf_vision.py)
- **关键对象**：`modal.App`、`modal.Dict`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/chat_with_pdf_vision.py`

## `06_gpu_and_ml/llm-serving/deepseek_v4.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serve DeepSeek V4 Pro on Modal with SGLang
- **源码**：[打开 `06_gpu_and_ml/llm-serving/deepseek_v4.py`](../06_gpu_and_ml/llm-serving/deepseek_v4.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/deepseek_v4.py`

## `06_gpu_and_ml/llm-serving/deepseek_v4_flash.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Deploy DeepSeek-V4-Flash with SGLang and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/deepseek_v4_flash.py`](../06_gpu_and_ml/llm-serving/deepseek_v4_flash.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/deepseek_v4_flash.py`

## `06_gpu_and_ml/llm-serving/gpt_oss_inference.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Run OpenAI's gpt-oss model with vLLM
- **源码**：[打开 `06_gpu_and_ml/llm-serving/gpt_oss_inference.py`](../06_gpu_and_ml/llm-serving/gpt_oss_inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/gpt_oss_inference.py`

## `06_gpu_and_ml/llm-serving/inkling_small.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serve Inkling-Small on Modal with SGLang
- **源码**：[打开 `06_gpu_and_ml/llm-serving/inkling_small.py`](../06_gpu_and_ml/llm-serving/inkling_small.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/inkling_small.py`

## `06_gpu_and_ml/llm-serving/lfm_snapshot.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Low Latency, Serverless LFM2 with vLLM and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/lfm_snapshot.py`](../06_gpu_and_ml/llm-serving/lfm_snapshot.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Server`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/lfm_snapshot.py`

## `06_gpu_and_ml/llm-serving/ministral3_inference.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serverless Ministral 3 with vLLM and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/ministral3_inference.py`](../06_gpu_and_ml/llm-serving/ministral3_inference.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/ministral3_inference.py`

## `06_gpu_and_ml/llm-serving/nemotron_inference.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Low latency Nvidia Nemotron 3 with SGLang and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/nemotron_inference.py`](../06_gpu_and_ml/llm-serving/nemotron_inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Server`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/nemotron_inference.py`

## `06_gpu_and_ml/llm-serving/openai_compatible/load_test.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：load test
- **源码**：[打开 `06_gpu_and_ml/llm-serving/openai_compatible/load_test.py`](../06_gpu_and_ml/llm-serving/openai_compatible/load_test.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/openai_compatible/load_test.py`

## `06_gpu_and_ml/llm-serving/sglang_low_latency.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Low latency Qwen 3.6 with SGLang and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/sglang_low_latency.py`](../06_gpu_and_ml/llm-serving/sglang_low_latency.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Server`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/sglang_low_latency.py`

## `06_gpu_and_ml/llm-serving/sglang_snapshot.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serverless Qwen 3-8B with SGLang and Modal Snapshots
- **源码**：[打开 `06_gpu_and_ml/llm-serving/sglang_snapshot.py`](../06_gpu_and_ml/llm-serving/sglang_snapshot.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.exit`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/sglang_snapshot.py`

## `06_gpu_and_ml/llm-serving/sglang_vlm.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serve the Qwen 3.6 Vision-Language Model with SGLang
- **源码**：[打开 `06_gpu_and_ml/llm-serving/sglang_vlm.py`](../06_gpu_and_ml/llm-serving/sglang_vlm.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/sglang_vlm.py`

## `06_gpu_and_ml/llm-serving/stepfun_inference.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Run StepFun models with SGLang
- **源码**：[打开 `06_gpu_and_ml/llm-serving/stepfun_inference.py`](../06_gpu_and_ml/llm-serving/stepfun_inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/stepfun_inference.py`

## `06_gpu_and_ml/llm-serving/trtllm_latency.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serve an interactive language model app with low-latency TensorRT-LLM (LLaMA 3 8B)
- **源码**：[打开 `06_gpu_and_ml/llm-serving/trtllm_latency.py`](../06_gpu_and_ml/llm-serving/trtllm_latency.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/trtllm_latency.py`

## `06_gpu_and_ml/llm-serving/trtllm_throughput.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serverless TensorRT-LLM (LLaMA 3 8B)
- **源码**：[打开 `06_gpu_and_ml/llm-serving/trtllm_throughput.py`](../06_gpu_and_ml/llm-serving/trtllm_throughput.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.fastapi_endpoint`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/trtllm_throughput.py`

## `06_gpu_and_ml/llm-serving/very_large_models.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Serve very large language models (DeepSeek V3, Kimi-K2, GLM 4.7/5)
- **源码**：[打开 `06_gpu_and_ml/llm-serving/very_large_models.py`](../06_gpu_and_ml/llm-serving/very_large_models.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/very_large_models.py`

## `06_gpu_and_ml/llm-serving/vllm_inference.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Run OpenAI-compatible LLM inference with Gemma and vLLM
- **源码**：[打开 `06_gpu_and_ml/llm-serving/vllm_inference.py`](../06_gpu_and_ml/llm-serving/vllm_inference.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/vllm_inference.py`

## `06_gpu_and_ml/llm-serving/vllm_low_latency.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Low latency Qwen 3 8B with vLLM and Modal
- **源码**：[打开 `06_gpu_and_ml/llm-serving/vllm_low_latency.py`](../06_gpu_and_ml/llm-serving/vllm_low_latency.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Server`、`modal.Volume`、`@app.local_entrypoint`、`@app.server`、`@modal.enter`、`@modal.exit`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/vllm_low_latency.py`

## `06_gpu_and_ml/llm-serving/vllm_throughput.py`

- **作用**：在 GPU 容器中加载指定大语言模型，并展示服务化、低延迟、吞吐优化或快照冷启动策略。
- **源码原题**：Run LLM inference at maximum throughput
- **源码**：[打开 `06_gpu_and_ml/llm-serving/vllm_throughput.py`](../06_gpu_and_ml/llm-serving/vllm_throughput.py)
- **关键对象**：`modal.App`、`modal.FunctionCall`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.exit`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/llm-serving/vllm_throughput.py`

## `06_gpu_and_ml/long-training.py`

- **作用**：展示可恢复的模型训练或微调流程，并配置 GPU、检查点与依赖镜像。
- **源码原题**：Run long, resumable training jobs on Modal
- **源码**：[打开 `06_gpu_and_ml/long-training.py`](../06_gpu_and_ml/long-training.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Retries`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/long-training.py`

## `06_gpu_and_ml/openai_whisper/fine_tune_asr.py`

- **作用**：微调或运行 Whisper 自动语音识别模型，使用持久化数据和 GPU 训练资源。
- **源码原题**：Fine-tune Whisper to Improve Transcription on Domain-Specific Vocab
- **源码**：[打开 `06_gpu_and_ml/openai_whisper/fine_tune_asr.py`](../06_gpu_and_ml/openai_whisper/fine_tune_asr.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/openai_whisper/fine_tune_asr.py`

## `06_gpu_and_ml/openai_whisper/finetuning/train/train.py`

- **作用**：微调或运行 Whisper 自动语音识别模型，使用持久化数据和 GPU 训练资源。
- **源码原题**：train
- **源码**：[打开 `06_gpu_and_ml/openai_whisper/finetuning/train/train.py`](../06_gpu_and_ml/openai_whisper/finetuning/train/train.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.function`
- **常用启动方式**：`modal run 06_gpu_and_ml/openai_whisper/finetuning/train/train.py`

## `06_gpu_and_ml/protein-folding/boltz_predict.py`

- **作用**：调用计算生物学模型进行蛋白质折叠、结构预测或结合物设计。
- **源码原题**：Fold proteins with Boltz-2
- **源码**：[打开 `06_gpu_and_ml/protein-folding/boltz_predict.py`](../06_gpu_and_ml/protein-folding/boltz_predict.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/protein-folding/boltz_predict.py`

## `06_gpu_and_ml/protein-folding/chai1.py`

- **作用**：调用计算生物学模型进行蛋白质折叠、结构预测或结合物设计。
- **源码原题**：Fold proteins with Chai-1
- **源码**：[打开 `06_gpu_and_ml/protein-folding/chai1.py`](../06_gpu_and_ml/protein-folding/chai1.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/protein-folding/chai1.py`

## `06_gpu_and_ml/protein-folding/esm3.py`

- **作用**：调用计算生物学模型进行蛋白质折叠、结构预测或结合物设计。
- **源码原题**：Build a protein folding dashboard with ESM3, Molstar, and Gradio
- **源码**：[打开 `06_gpu_and_ml/protein-folding/esm3.py`](../06_gpu_and_ml/protein-folding/esm3.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/protein-folding/esm3.py`

## `06_gpu_and_ml/protein-folding/esmfold2.py`

- **作用**：调用计算生物学模型进行蛋白质折叠、结构预测或结合物设计。
- **源码原题**：Fold proteins and biomolecular complexes with ESMFold2
- **源码**：[打开 `06_gpu_and_ml/protein-folding/esmfold2.py`](../06_gpu_and_ml/protein-folding/esmfold2.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/protein-folding/esmfold2.py`

## `06_gpu_and_ml/reinforcement-learning/grpo_trl.py`

- **作用**：运行强化学习训练工作流，包含奖励计算、训练器和分布式 GPU 资源配置。
- **源码原题**：Train a model to solve coding problems using GRPO and TRL
- **源码**：[打开 `06_gpu_and_ml/reinforcement-learning/grpo_trl.py`](../06_gpu_and_ml/reinforcement-learning/grpo_trl.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Sandbox`、`modal.Secret`、`modal.Volume`、`@app.function`、`@modal.concurrent`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/reinforcement-learning/grpo_trl.py`

## `06_gpu_and_ml/reinforcement-learning/grpo_verl.py`

- **作用**：运行强化学习训练工作流，包含奖励计算、训练器和分布式 GPU 资源配置。
- **源码原题**：Train a model to solve math problems using GRPO and verl
- **源码**：[打开 `06_gpu_and_ml/reinforcement-learning/grpo_verl.py`](../06_gpu_and_ml/reinforcement-learning/grpo_verl.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.function`、`@modal.concurrent`、`@modal.web_server`
- **常用启动方式**：`modal run 06_gpu_and_ml/reinforcement-learning/grpo_verl.py`

## `06_gpu_and_ml/reinforcement-learning/learn_math.py`

- **作用**：运行强化学习训练工作流，包含奖励计算、训练器和分布式 GPU 资源配置。
- **源码原题**：Training a mathematical reasoning model using the verifiers library with sandboxed code execution
- **源码**：[打开 `06_gpu_and_ml/reinforcement-learning/learn_math.py`](../06_gpu_and_ml/reinforcement-learning/learn_math.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/reinforcement-learning/learn_math.py`

## `06_gpu_and_ml/reinforcement-learning/trainer_script_grpo.py`

- **作用**：运行强化学习训练工作流，包含奖励计算、训练器和分布式 GPU 资源配置。
- **源码原题**：Training script for training a reasoning model using the verifiers library with sandboxed code execution
- **源码**：[打开 `06_gpu_and_ml/reinforcement-learning/trainer_script_grpo.py`](../06_gpu_and_ml/reinforcement-learning/trainer_script_grpo.py)
- **关键对象**：`modal.App`、`modal.Sandbox`
- **常用启动方式**：`modal run 06_gpu_and_ml/reinforcement-learning/trainer_script_grpo.py`

## `06_gpu_and_ml/sam/segment_anything.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Run Facebook's Segment Anything Model 2 (SAM 2) on Modal
- **源码**：[打开 `06_gpu_and_ml/sam/segment_anything.py`](../06_gpu_and_ml/sam/segment_anything.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/sam/segment_anything.py`

## `06_gpu_and_ml/speech-to-text/batched_whisper.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：Fast Whisper inference using dynamic batching
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/batched_whisper.py`](../06_gpu_and_ml/speech-to-text/batched_whisper.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.batched`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/batched_whisper.py`

## `06_gpu_and_ml/speech-to-text/parakeet_multitalker.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：Parakeet Multi-talker Speech-to-Text
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/parakeet_multitalker.py`](../06_gpu_and_ml/speech-to-text/parakeet_multitalker.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/parakeet_multitalker.py`

## `06_gpu_and_ml/speech-to-text/sortformer2_1_speaker_diarization.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：Streaming Speaker Diarization with Sortformer2.1
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/sortformer2_1_speaker_diarization.py`](../06_gpu_and_ml/speech-to-text/sortformer2_1_speaker_diarization.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/sortformer2_1_speaker_diarization.py`

## `06_gpu_and_ml/speech-to-text/streaming_kyutai_stt.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：Stream transcriptions with Kyutai STT
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/streaming_kyutai_stt.py`](../06_gpu_and_ml/speech-to-text/streaming_kyutai_stt.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Queue`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/streaming_kyutai_stt.py`

## `06_gpu_and_ml/speech-to-text/streaming_parakeet.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：Streaming audio transcription using Parakeet
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/streaming_parakeet.py`](../06_gpu_and_ml/speech-to-text/streaming_parakeet.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Queue`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/streaming_parakeet.py`

## `06_gpu_and_ml/speech-to-text/streaming_whisper.py`

- **作用**：部署语音识别或说话人处理模型，重点展示流式或批量音频处理路径。
- **源码原题**：streaming whisper
- **源码**：[打开 `06_gpu_and_ml/speech-to-text/streaming_whisper.py`](../06_gpu_and_ml/speech-to-text/streaming_whisper.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`
- **常用启动方式**：`modal run 06_gpu_and_ml/speech-to-text/streaming_whisper.py`

## `06_gpu_and_ml/stable_diffusion/flux.py`

- **作用**：在 GPU 上运行图像生成或编辑模型，并提供命令行、API 或交互界面。
- **源码原题**：Run Flux fast on H100s with torch.compile
- **源码**：[打开 `06_gpu_and_ml/stable_diffusion/flux.py`](../06_gpu_and_ml/stable_diffusion/flux.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/stable_diffusion/flux.py`

## `06_gpu_and_ml/stable_diffusion/image_to_image.py`

- **作用**：在 GPU 上运行图像生成或编辑模型，并提供命令行、API 或交互界面。
- **源码原题**：Edit images with Flux Kontext
- **源码**：[打开 `06_gpu_and_ml/stable_diffusion/image_to_image.py`](../06_gpu_and_ml/stable_diffusion/image_to_image.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/stable_diffusion/image_to_image.py`

## `06_gpu_and_ml/stable_diffusion/text_to_image.py`

- **作用**：在 GPU 上运行图像生成或编辑模型，并提供命令行、API 或交互界面。
- **源码原题**：Run Stable Diffusion 3.5 Large Turbo as a CLI, API, and web UI
- **源码**：[打开 `06_gpu_and_ml/stable_diffusion/text_to_image.py`](../06_gpu_and_ml/stable_diffusion/text_to_image.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`、`@modal.fastapi_endpoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/stable_diffusion/text_to_image.py`

## `06_gpu_and_ml/tensorflow/tensorflow_tutorial.py`

- **作用**：展示深度学习框架在 Modal Image 与远程 GPU Function 中的运行方式。
- **源码原题**：TensorFlow tutorial
- **源码**：[打开 `06_gpu_and_ml/tensorflow/tensorflow_tutorial.py`](../06_gpu_and_ml/tensorflow/tensorflow_tutorial.py)
- **关键对象**：`modal.App`、`modal.Function`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.wsgi_app`
- **常用启动方式**：`modal run 06_gpu_and_ml/tensorflow/tensorflow_tutorial.py`

## `06_gpu_and_ml/text-to-audio/chatterbox_tts.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Create a Chatterbox TTS API on Modal
- **源码**：[打开 `06_gpu_and_ml/text-to-audio/chatterbox_tts.py`](../06_gpu_and_ml/text-to-audio/chatterbox_tts.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.enter`、`@modal.fastapi_endpoint`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/text-to-audio/chatterbox_tts.py`

## `06_gpu_and_ml/text-to-audio/generate_music.py`

- **作用**：展示该目录主题下的 Modal App、Image、Function 或相关资源如何组合成可运行工作流。
- **源码原题**：Make music with ACE-Step 1.5
- **源码**：[打开 `06_gpu_and_ml/text-to-audio/generate_music.py`](../06_gpu_and_ml/text-to-audio/generate_music.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`、`@modal.enter`
- **常用启动方式**：`modal run 06_gpu_and_ml/text-to-audio/generate_music.py`

## `06_gpu_and_ml/text-to-video/ltx.py`

- **作用**：以 GPU 加速的生成模型将文本或图像转换为视频或三维场景。
- **源码原题**：Generate videos from prompts with Lightricks LTX-Video
- **源码**：[打开 `06_gpu_and_ml/text-to-video/ltx.py`](../06_gpu_and_ml/text-to-video/ltx.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/text-to-video/ltx.py`

## `06_gpu_and_ml/text-to-video/ltx2_two_stage.py`

- **作用**：以 GPU 加速的生成模型将文本或图像转换为视频或三维场景。
- **源码原题**：High-quality text-to-video with LTX-2
- **源码**：[打开 `06_gpu_and_ml/text-to-video/ltx2_two_stage.py`](../06_gpu_and_ml/text-to-video/ltx2_two_stage.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/text-to-video/ltx2_two_stage.py`

## `06_gpu_and_ml/text-to-video/mochi.py`

- **作用**：以 GPU 加速的生成模型将文本或图像转换为视频或三维场景。
- **源码原题**：Text-to-video generation with Mochi
- **源码**：[打开 `06_gpu_and_ml/text-to-video/mochi.py`](../06_gpu_and_ml/text-to-video/mochi.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/text-to-video/mochi.py`

## `06_gpu_and_ml/torch_profiling.py`

- **作用**：展示深度学习框架在 Modal Image 与远程 GPU Function 中的运行方式。
- **源码原题**：Tracing and profiling GPU-accelerated PyTorch programs on Modal
- **源码**：[打开 `06_gpu_and_ml/torch_profiling.py`](../06_gpu_and_ml/torch_profiling.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`、`@modal.concurrent`、`@modal.wsgi_app`
- **常用启动方式**：`modal run 06_gpu_and_ml/torch_profiling.py`

## `06_gpu_and_ml/unsloth_finetune.py`

- **作用**：展示可恢复的模型训练或微调流程，并配置 GPU、检查点与依赖镜像。
- **源码原题**：Efficient LLM Finetuning with Unsloth
- **源码**：[打开 `06_gpu_and_ml/unsloth_finetune.py`](../06_gpu_and_ml/unsloth_finetune.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Retries`、`modal.Secret`、`modal.Volume`、`@app.function`、`@app.local_entrypoint`
- **常用启动方式**：`modal run 06_gpu_and_ml/unsloth_finetune.py`

## `06_gpu_and_ml/world-models/text_to_world.py`

- **作用**：以 GPU 加速的生成模型将文本或图像转换为视频或三维场景。
- **源码原题**：Generate 3D worlds from text with LTX-2.3 and InSpatio-World
- **源码**：[打开 `06_gpu_and_ml/world-models/text_to_world.py`](../06_gpu_and_ml/world-models/text_to_world.py)
- **关键对象**：`modal.App`、`modal.Image`、`modal.Retries`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.asgi_app`、`@modal.concurrent`
- **常用启动方式**：`modal run 06_gpu_and_ml/world-models/text_to_world.py`

## `06_gpu_and_ml/yolo/finetune_yolo.py`

- **作用**：展示可恢复的模型训练或微调流程，并配置 GPU、检查点与依赖镜像。
- **源码原题**：Fine-tune open source YOLO models for object detection
- **源码**：[打开 `06_gpu_and_ml/yolo/finetune_yolo.py`](../06_gpu_and_ml/yolo/finetune_yolo.py)
- **关键对象**：`modal.App`、`modal.Cls`、`modal.Image`、`modal.Secret`、`modal.Volume`、`@app.cls`、`@app.function`、`@app.local_entrypoint`、`@modal.enter`、`@modal.method`
- **常用启动方式**：`modal run 06_gpu_and_ml/yolo/finetune_yolo.py`
