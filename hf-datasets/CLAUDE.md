# CLAUDE.md For Hugging Face Datasets

## Purpose

This directory contains Hugging Face datasets that Daniel manages, organized into public and private subdirectories. Datasets stored here are typically synchronized with Hugging Face Hub repositories.

## Directory Structure

- **`public/`**: Publicly accessible datasets shared on Hugging Face Hub
- **`private/`**: Private datasets for internal use or development

## Typical Contents

- Training datasets for machine learning models
- Evaluation and benchmark datasets
- Data preprocessing scripts
- Dataset cards and documentation
- Data loading scripts
- Curated datasets for specific tasks
- Synthetic or generated data
- Cleaned and processed versions of public datasets

## Common Tasks

When operating at this level of the filesystem, you may be asked to:

### Dataset Management
- Clone datasets from Hugging Face Hub
- Upload new datasets to Hugging Face Hub
- Update existing datasets with new data
- Organize datasets by task, domain, or project
- Manage dataset versions and splits
- Archive or remove outdated datasets

### Dataset Creation and Processing
- Create new datasets from raw data sources
- Clean and preprocess data
- Generate dataset cards with metadata
- Create data loading scripts
- Split data into train/validation/test sets
- Convert between data formats (CSV, JSON, Parquet, etc.)
- Validate data quality and integrity

### Documentation
- Write comprehensive dataset cards (README.md)
- Document data sources and collection methods
- Specify licensing and usage restrictions
- Include examples and sample data
- Document preprocessing steps and transformations
- Add citations and references

### Analysis
- Analyze dataset statistics and distributions
- Identify class imbalances or biases
- Generate data quality reports
- Compare dataset versions
- Visualize data distributions

## Hugging Face Integration

### Using Hugging Face CLI
```bash
# Login to Hugging Face
huggingface-cli login

# Clone a dataset
git clone https://huggingface.co/datasets/username/dataset-name

# Push changes
cd dataset-name
git add .
git commit -m "Update dataset"
git push
```

### Using Datasets Library
```python
from datasets import load_dataset, Dataset, DatasetDict

# Load a dataset
dataset = load_dataset("username/dataset-name")

# Push to Hub
dataset.push_to_hub("username/new-dataset")
```

## Dataset Card Requirements

Every dataset should include a README.md with:
- Dataset description and purpose
- Data sources and collection methodology
- Dataset structure and fields
- Splits (train/validation/test)
- Licensing information
- Citation information
- Usage examples
- Known limitations or biases
- Maintenance and update schedule

## Best Practices

1. **Organization**: Use clear, descriptive names for datasets
2. **Documentation**: Always include comprehensive dataset cards
3. **Versioning**: Use git tags or branches for dataset versions
4. **Privacy**: Keep sensitive data in private/ directory
5. **Licensing**: Clearly specify data licenses and usage rights
6. **Quality**: Validate data integrity before uploading
7. **Format**: Prefer efficient formats (Parquet) for large datasets
8. **Splits**: Include standard train/val/test splits when applicable
9. **Metadata**: Include rich metadata for discoverability
10. **Size**: Monitor dataset sizes and use Git LFS for large files

## Working in This Directory

- Check if Git LFS is enabled for large files
- Use Hugging Face datasets library for efficient data handling
- Keep raw and processed data separate when possible
- Document preprocessing pipelines
- Include data validation scripts
- Consider data privacy and compliance requirements
- Test dataset loading scripts before pushing to Hub

## Public vs Private Datasets

### Public Datasets (`public/`)
- Openly shared on Hugging Face Hub
- Include proper attribution and licensing
- Follow community standards and best practices
- Make discoverable with appropriate tags and metadata

### Private Datasets (`private/`)
- Not shared publicly on Hugging Face Hub
- May contain proprietary or sensitive data
- Still maintain documentation for internal use
- Consider data security and access controls
