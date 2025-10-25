# CLAUDE.md For Hugging Face Spaces

## Purpose

This directory contains Hugging Face Spaces that Daniel manages, organized into public and private subdirectories. Spaces are web applications that provide interactive demos and interfaces for machine learning models and tools.

## Directory Structure

- **`public/`**: Publicly accessible Spaces shared on Hugging Face Hub
- **`private/`**: Private Spaces for internal testing or development

## Typical Contents

- Gradio applications
- Streamlit applications
- Static HTML/JS applications
- Docker-based custom applications
- Model demos and interactive interfaces
- Data visualization tools
- ML application prototypes
- API demonstrations
- Educational tools and tutorials

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

### Space Management
- Clone Spaces from Hugging Face Hub
- Create new Spaces for model demos
- Update existing Spaces with improvements
- Deploy Spaces to Hugging Face Hub
- Manage Space configurations and settings
- Archive or remove outdated Spaces
- Monitor Space usage and performance

### Space Development
- Build Gradio interfaces for models
- Create Streamlit applications
- Develop custom Docker-based Spaces
- Integrate models and datasets
- Implement user authentication
- Add analytics and monitoring
- Optimize Space performance
- Handle user inputs and edge cases

### Documentation
- Write comprehensive Space descriptions (README.md)
- Document Space usage and features
- Provide example inputs and outputs
- Include troubleshooting information
- Add citations for models/datasets used
- Document API usage if applicable

### Testing and Deployment
- Test Spaces locally before deployment
- Debug Space runtime issues
- Monitor Space logs and errors
- Update dependencies and packages
- Test across different browsers/devices
- Optimize loading times

## Hugging Face Spaces Types

### Gradio Spaces
Most common type for ML demos:
```python
import gradio as gr

def predict(input):
    # Your model inference code
    return output

demo = gr.Interface(fn=predict, inputs="text", outputs="text")
demo.launch()
```

### Streamlit Spaces
For more complex web apps:
```python
import streamlit as st

st.title("My ML Application")
input_text = st.text_input("Enter text:")
if st.button("Process"):
    result = process(input_text)
    st.write(result)
```

### Docker Spaces
For custom applications with specific dependencies:
```dockerfile
FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### Static Spaces
For HTML/CSS/JS applications without backend

## Space Configuration

Every Space requires an `README.md` with YAML frontmatter:
```yaml
---
title: My Space Name
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: gradio  # or streamlit, docker, static
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
---
```

## Common Space Features

- **Model Integration**: Load models from Hugging Face Hub
- **Dataset Integration**: Access datasets directly
- **File Upload**: Allow users to upload files
- **Real-time Processing**: Provide instant feedback
- **Examples**: Include pre-populated example inputs
- **Sharing**: Generate shareable links
- **Embedding**: Embed Spaces in other websites
- **API**: Some Spaces expose API endpoints

## Best Practices

1. **Performance**: Optimize model loading and inference
2. **UX**: Design intuitive, user-friendly interfaces
3. **Error Handling**: Gracefully handle invalid inputs
4. **Examples**: Provide good example inputs
5. **Documentation**: Include clear usage instructions
6. **Loading States**: Show loading indicators for processing
7. **Limits**: Set reasonable input size and rate limits
8. **Privacy**: Don't log sensitive user inputs
9. **Mobile**: Ensure mobile-responsive design
10. **Accessibility**: Follow accessibility best practices

## Hardware Configuration

Spaces can run on different hardware:
- **CPU Basic**: Free tier (2 vCPU, 16GB RAM)
- **CPU Upgrade**: Better performance
- **T4 Small**: GPU for inference (15GB VRAM)
- **T4 Medium**: More GPU memory (15GB VRAM)
- **A10G Small**: Faster GPU (24GB VRAM)
- **A10G Large**: Large GPU workloads (24GB VRAM)

Configure in Space settings or README frontmatter

## Working in This Directory

- Test Spaces locally before pushing to Hub
- Use appropriate SDK version specifications
- Monitor Space build logs for errors
- Keep dependencies minimal for faster builds
- Use caching for model/data loading
- Implement proper error handling
- Add rate limiting for expensive operations
- Consider using Hugging Face Inference API for large models

## Development Workflow

1. **Local Development**:
   ```bash
   # Install dependencies
   pip install gradio  # or streamlit

   # Run locally
   python app.py
   ```

2. **Push to Hub**:
   ```bash
   # Clone Space
   git clone https://huggingface.co/spaces/username/space-name
   cd space-name

   # Make changes
   # ...

   # Push changes
   git add .
   git commit -m "Update Space"
   git push
   ```

3. **Monitor**: Check Space logs and status on Hugging Face

## Common Space Patterns

### Model Demo Space
- Load model from Hugging Face Hub
- Provide text/image input interface
- Display model outputs
- Include example inputs
- Show processing time

### Data Visualization Space
- Load dataset from Hugging Face Hub
- Create interactive visualizations
- Allow filtering and exploration
- Export capabilities

### Tool/Utility Space
- Provide specific ML functionality
- Process user inputs
- Generate outputs (text, images, etc.)
- Downloadable results

## Public vs Private Spaces

### Public Spaces (`public/`)
- Openly accessible on Hugging Face Hub
- Listed in your profile
- Searchable and discoverable
- Can be embedded elsewhere
- Usage may count toward community metrics

### Private Spaces (`private/`)
- Only accessible to you (and collaborators)
- Not listed publicly
- Good for testing and development
- Can be made public later
- Same hardware options available

## Troubleshooting

Common issues:
- **Build failures**: Check requirements.txt and dependencies
- **Runtime errors**: Review Space logs in Hugging Face
- **Slow performance**: Optimize model loading, consider GPU upgrade
- **Out of memory**: Reduce batch size, optimize memory usage
- **Timeout errors**: Add progress indicators, optimize processing

## Security Considerations

- Don't expose API keys or secrets in code
- Use Hugging Face Secrets for sensitive values
- Validate and sanitize user inputs
- Set appropriate rate limits
- Be cautious with file uploads
- Don't log sensitive user data
