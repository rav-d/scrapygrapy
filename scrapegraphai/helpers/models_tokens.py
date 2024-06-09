"""
Models token
"""

models_tokens = {
    "openai": {
        "gpt-3.5-turbo-0125": 16385,
        "gpt-3.5": 4096,
        "gpt-3.5-turbo": 4096,
        "gpt-3.5-turbo-1106": 16385,
        "gpt-3.5-turbo-instruct": 4096,
        "gpt-4-0125-preview": 128000,
        "gpt-4-turbo-preview": 128000,
        "gpt-4-turbo": 128000,
        "gpt-4-turbo-2024-04-09": 128000,
        "gpt-4-1106-preview": 128000,
        "gpt-4-vision-preview": 128000,
        "gpt-4": 8192,
        "gpt-4-0613": 8192,
        "gpt-4-32k": 32768,
        "gpt-4-32k-0613": 32768,
        "gpt-4o": 128000,
    },
    "azure": {
        "gpt-3.5-turbo": 4096,
        "gpt-4": 8192,
        "gpt-4-0613": 8192,
        "gpt-4-32k": 32768,
        "gpt-4-32k-0613": 32768,
        "gpt-4o": 128000,
    },
    "gemini": {
        "gemini-pro": 128000,
        "gemini-1.5-flash-latest":128000,
        "gemini-1.5-pro-latest":128000,
        "models/embedding-001": 2048
    },

    "ollama": {
        "command-r": 12800,
        "command-r-plus": 12800,
        "codellama": 16000,
        "dbrx": 32768,
        "dbrx:instruct": 32768,
        "deepseek-coder:33b": 16000,
        "dolphin-mixtral": 32000,
        "llama2": 4096,
        "llama3": 8192,
        "llama3:70b-instruct": 8192,
        "llava": 4096,
        "llava:34b": 4096,
        "llava_next": 4096,
        "mistral": 8192,
        "falcon": 2048,
        "codellama": 16000,
        "dolphin-mixtral": 32000,
        "mistral-openorca": 32000,
        "stablelm-zephyr": 8192,
        "command-r-plus": 12800,
        "command-r": 12800,
        "mistral:7b-instruct": 32768,
        "mistral-openorca": 32000,
        "mixtral:8x22b-instruct": 65536,
        "nous-hermes2:34b": 4096,
        "orca-mini": 2048,
        "phi3:3.8b": 12800,
        "phi3:14b": 12800,
        "qwen:0.5b": 32000,
        "qwen:1.8b": 32000,
        "qwen:4b": 32000,
        "qwen:14b": 32000,
        "qwen:32b": 32000,
        "qwen:72b": 32000,
        "qwen:110b": 32000,
        "stablelm-zephyr": 8192,
        "wizardlm2:8x22b": 65536,
        # embedding models
        "nomic-embed-text": 8192,
        "snowflake-arctic-embed:335m": 8192,
        "snowflake-arctic-embed:l": 8192,
        "mxbai-embed-large": 512,
    },
    "oneapi": {
        "qwen-turbo": 6000 
    },
    "groq": {
        "llama3-8b-8192": 8192,
        "llama3-70b-8192": 8192,
        "mixtral-8x7b-32768": 32768,
        "gemma-7b-it": 8192,
    },
    "claude": {
        "claude_instant": 100000,
        "claude2": 9000,
        "claude2.1": 200000,
        "claude3": 200000
    },
    "bedrock": {
        "anthropic.claude-3-haiku-20240307-v1:0": 200000,
        "anthropic.claude-3-sonnet-20240229-v1:0": 200000,
        "anthropic.claude-3-opus-20240229-v1:0": 200000,
        "anthropic.claude-v2:1": 200000,
        "anthropic.claude-v2": 100000,
        "anthropic.claude-instant-v1": 100000,
        "meta.llama3-8b-instruct-v1:0": 8192,
        "meta.llama3-70b-instruct-v1:0": 8192,
        "meta.llama2-13b-chat-v1": 4096,
        "meta.llama2-70b-chat-v1": 4096,
        "mistral.mistral-7b-instruct-v0:2": 32768,
        "mistral.mixtral-8x7b-instruct-v0:1": 32768,
        "mistral.mistral-large-2402-v1:0": 32768,
		# Embedding models
		"amazon.titan-embed-text-v1": 8000,
		"amazon.titan-embed-text-v2:0": 8000,
        "cohere.embed-english-v3": 512,
        "cohere.embed-multilingual-v3": 512
    },
    "mistral": {
        "mistralai/Mistral-7B-Instruct-v0.2": 32000
    },
    "hugging_face": {
        "meta-llama/Meta-Llama-3-8B": 8192,
        "meta-llama/Meta-Llama-3-8B-Instruct": 8192,
        "meta-llama/Meta-Llama-3-70B": 8192,
        "meta-llama/Meta-Llama-3-70B-Instruct": 8192,
        "google/gemma-2b": 8192,
        "google/gemma-2b-it": 8192,
        "google/gemma-7b": 8192,
        "google/gemma-7b-it": 8192,
        "microsoft/phi-2": 2048,
        "openai-community/gpt2": 1024,
        "openai-community/gpt2-medium": 1024,
        "openai-community/gpt2-large": 1024,
        "facebook/opt-125m": 2048,
        "petals-team/StableBeluga2": 8192,
        "distilbert/distilgpt2": 1024,
        "mistralai/Mistral-7B-Instruct-v0.2": 32768,
        "gradientai/Llama-3-8B-Instruct-Gradient-1048k": 1040200,
        "NousResearch/Hermes-2-Pro-Llama-3-8B": 8192,
        "NousResearch/Hermes-2-Pro-Llama-3-8B-GGUF": 8192,
        "nvidia/Llama3-ChatQA-1.5-8B": 8192,
        "microsoft/Phi-3-mini-4k-instruct": 4192,
        "microsoft/Phi-3-mini-128k-instruct": 131072,
        "mlabonne/Meta-Llama-3-120B-Instruct": 8192,
        "cognitivecomputations/dolphin-2.9-llama3-8b": 8192,
        "cognitivecomputations/dolphin-2.9-llama3-8b-gguf": 8192,
        "cognitivecomputations/dolphin-2.8-mistral-7b-v02": 32768,
        "cognitivecomputations/dolphin-2.5-mixtral-8x7b": 32768,
        "TheBloke/dolphin-2.7-mixtral-8x7b-GGUF": 32768,
        "deepseek-ai/DeepSeek-V2": 131072,
        "deepseek-ai/DeepSeek-V2-Chat": 131072,
        "claude-3-haiku": 200000
    },
    "deepseek": {
        "deepseek-chat": 32768,
        "deepseek-coder": 16384
    },
    "ernie": {
        "ernie-bot-turbo": 4096,
        "ernie-bot": 4096,
        "ernie-bot-2": 4096,
        "ernie-bot-2-base": 4096,
        "ernie-bot-2-base-zh": 4096,
        "ernie-bot-2-base-en": 4096,
        "ernie-bot-2-base-en-zh": 4096,
        "ernie-bot-2-base-zh-en": 4096,
    }
}
