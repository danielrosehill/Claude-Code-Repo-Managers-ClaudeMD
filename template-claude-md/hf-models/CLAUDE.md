# CLAUDE.md For Hugging Face Models

## Purpose

This directory contains machine learning models that Daniel manages and hosts on Hugging Face Hub. Models stored here include trained models, fine-tuned versions, and custom architectures.

## Typical Contents

- Trained machine learning models
- Fine-tuned versions of base models
- Custom model architectures
- Model weights and checkpoints
- Model cards and documentation
- Training scripts and configurations
- Inference examples and demos
- Evaluation results and metrics
- LoRA adapters and other parameter-efficient fine-tuning artifacts

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

### Model Management
- Clone models from Hugging Face Hub
- Upload new models to Hugging Face Hub
- Update existing models with new checkpoints
- Organize models by type, task, or project
- Manage model versions and variants
- Archive or remove outdated models
- Convert models between formats (PyTorch, ONNX, SafeTensors)

### Model Development
- Fine-tune pre-trained models
- Train custom models from scratch
- Perform parameter-efficient fine-tuning (LoRA, QLoRA)
- Quantize models for efficiency
- Merge LoRA adapters with base models
- Optimize models for inference
- Create model ensembles

### Documentation
- Write comprehensive model cards (README.md)
- Document model architecture and parameters
- Specify training data and methodology
- Include performance metrics and benchmarks
- Document intended use and limitations
- Add ethical considerations and biases
- Provide usage examples and code snippets
- Include citation information

### Testing and Evaluation
- Run inference tests on models
- Evaluate model performance on benchmarks
- Compare different model versions
- Generate sample outputs
- Profile model performance (speed, memory)
- Test model deployment

## Hugging Face Integration

### Using Hugging Face CLI
```bash
# Login to Hugging Face
huggingface-cli login

# Clone a model
git clone https://huggingface.co/username/model-name

# Upload large files with Git LFS
git lfs install
git lfs track "*.bin" "*.safetensors"
git add .gitattributes
git add model_files
git commit -m "Add model files"
git push
```

### Using Transformers Library
```python
from transformers import AutoModel, AutoTokenizer

# Load a model
model = AutoModel.from_pretrained("username/model-name")
tokenizer = AutoTokenizer.from_pretrained("username/model-name")

# Push to Hub
model.push_to_hub("username/new-model")
tokenizer.push_to_hub("username/new-model")
```

### Using Diffusers Library (for image models)
```python
from diffusers import DiffusionPipeline

# Load a diffusion model
pipeline = DiffusionPipeline.from_pretrained("username/model-name")

# Push to Hub
pipeline.push_to_hub("username/new-model")
```

## Model Card Requirements

Every model should include a README.md with:
- Model description and purpose
- Model architecture and parameters
- Training data and methodology
- Training hyperparameters and configurations
- Performance metrics and benchmarks
- Intended use cases
- Limitations and biases
- Ethical considerations
- Licensing information
- Citation information
- Usage examples with code
- Environmental impact (optional but recommended)

## Model Types and Organization

Consider organizing by:
- **Task**: text-generation, image-generation, classification, etc.
- **Base Model**: llama, stable-diffusion, bert, etc.
- **Domain**: medical, finance, general, etc.
- **Size**: small, medium, large
- **Stage**: experimental, production, archived

## Best Practices

1. **Format**: Use SafeTensors format when possible for security and speed
2. **Size**: Use Git LFS for large model files (>10MB)
3. **Documentation**: Always include comprehensive model cards
4. **Versioning**: Tag important model versions with git tags
5. **Licensing**: Clearly specify model license and base model licenses
6. **Privacy**: Ensure training data doesn't contain sensitive information
7. **Testing**: Test models before pushing to Hub
8. **Metadata**: Include rich metadata for discoverability (tags, languages, tasks)
9. **Quantization**: Consider providing quantized versions for efficiency
10. **Safety**: Document safety considerations and potential misuse

## Working in This Directory

- Ensure Git LFS is configured for large files
- Use appropriate model libraries (transformers, diffusers, etc.)
- Test model loading before pushing to Hub
- Monitor model sizes and storage usage
- Keep training scripts and configs with models
- Document hardware requirements for inference
- Include example inference code
- Consider providing GGUF/ONNX versions for broader compatibility

## File Organization

Typical model repository structure:
```
model-name/
├── README.md (model card)
├── config.json (model configuration)
├── model.safetensors (or pytorch_model.bin)
├── tokenizer.json
├── tokenizer_config.json
├── special_tokens_map.json
├── generation_config.json (optional)
├── training_args.json (optional)
├── trainer_state.json (optional)
├── .gitattributes (for LFS tracking)
└── examples/ (optional usage examples)
```

## LoRA and Fine-tuning Artifacts

For LoRA adapters and similar:
- Store adapter weights separately from base models
- Document base model compatibility
- Include merge scripts if applicable
- Specify training parameters and data used
- Note performance compared to base model

## Model Deployment Considerations

- Test models with expected input formats
- Document hardware requirements (GPU, RAM)
- Provide inference time estimates
- Include optimization options (quantization, ONNX)
- Consider creating demo spaces for models
- Document API usage if providing inference endpoints
