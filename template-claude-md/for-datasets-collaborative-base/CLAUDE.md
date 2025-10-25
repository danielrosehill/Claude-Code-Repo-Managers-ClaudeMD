# CLAUDE.md For Collaborative Dataset Projects Base

## Purpose

This directory manages collaborative dataset repositories where Daniel works with other contributors on shared data projects. These repositories focus on creating, curating, maintaining, and improving datasets for research, machine learning, or data analysis.

## Typical Contents

- Multi-contributor dataset repositories
- Community-curated datasets
- Open data projects
- Machine learning dataset collections
- Research data collaborations
- Benchmark datasets
- Crowdsourced data initiatives
- Data annotation projects

## Platforms and Formats

### Common Platforms
- **Hugging Face Datasets**: ML/AI datasets with standardized format
- **Kaggle**: Competition and community datasets
- **GitHub**: Version-controlled data repositories
- **Zenodo/Figshare**: Research data repositories
- **Open Data portals**: Government and institutional data
- **DVC (Data Version Control)**: Git for data

### Common Formats
- CSV/TSV (tabular data)
- JSON/JSONL (structured data)
- Parquet (columnar storage)
- HDF5 (hierarchical data)
- Arrow (in-memory columnar)
- SQLite (database)
- Images (PNG, JPEG, TIFF)
- Audio (WAV, MP3, FLAC)
- Text files (TXT, MD)

## Key Characteristics

Dataset projects differ from code projects:
- **Large files**: May require Git LFS or specialized storage
- **Data quality**: Accuracy and consistency are critical
- **Licensing**: Data licensing is complex and important
- **Privacy**: May contain sensitive or regulated data
- **Versioning**: Changes affect reproducibility
- **Documentation**: Metadata and data cards are essential
- **Testing**: Data validation and quality checks
- **Ethics**: Bias, representation, and ethical considerations

## Common Tasks

### Dataset Management
- Clone dataset repositories (may be large)
- Sync with upstream changes
- Track data quality issues
- Monitor dataset updates and versions
- Manage data lineage and provenance
- Handle large file storage (LFS, DVC)

### Data Curation
- Add new data samples
- Clean and validate existing data
- Standardize data formats
- Remove duplicates or errors
- Annotate or label data
- Split data (train/val/test)
- Augment datasets
- Merge data from multiple sources

### Collaboration Workflows
- Follow dataset contribution guidelines
- Submit pull requests for data additions
- Participate in data quality reviews
- Coordinate with data annotators
- Maintain consistency in annotations
- Document data collection methodology
- Track changes and versions

### Quality Assurance
- Validate data integrity
- Check for missing values
- Verify data types and ranges
- Test data loading scripts
- Check for bias or imbalance
- Verify licenses and attribution
- Ensure privacy compliance
- Run data quality metrics

## Dataset Documentation

### Essential Documentation
- **README**: Overview, purpose, and quick start
- **Data Card**: Standardized dataset description
- **Schema**: Data structure and field definitions
- **License**: Clear usage rights and restrictions
- **Collection methodology**: How data was gathered
- **Known limitations**: Biases, gaps, or issues
- **Citation**: How to cite the dataset
- **Changelog**: Version history and updates

### Data Cards / Model Cards
Follow standards like:
- Hugging Face Dataset Cards
- Google Dataset Cards
- Datasheets for Datasets
- Include: motivation, composition, collection, preprocessing, uses, distribution, maintenance

## Data Quality Standards

### Validation
- Schema validation (expected fields, types)
- Range checks (values within expected bounds)
- Completeness checks (missing data)
- Consistency checks (cross-field validation)
- Format validation (proper encoding, syntax)
- Duplicate detection
- Outlier detection

### Cleaning
- Handle missing values appropriately
- Standardize formats and encodings
- Remove or flag outliers
- Correct obvious errors
- Normalize data when appropriate
- Document all cleaning operations
- Preserve raw data when possible

## Ethical Considerations

### Privacy
- Remove or anonymize PII (Personally Identifiable Information)
- Follow GDPR, CCPA, and other regulations
- Obtain necessary consents
- Document data collection ethics
- Consider right to be forgotten

### Bias and Fairness
- Document data demographics
- Check for representation imbalances
- Acknowledge potential biases
- Consider downstream impacts
- Include fairness metrics
- Document mitigation strategies

### Use Cases
- Specify intended uses
- Document inappropriate uses
- Consider dual-use concerns
- Address potential harms
- Provide usage guidelines

## Version Management

### Versioning Strategies
- Semantic versioning for datasets
- Tag major changes and updates
- Maintain changelog
- Track data lineage
- Document breaking changes
- Preserve historical versions

### Large File Handling
- Use Git LFS for files >100MB
- Consider DVC for very large datasets
- Use cloud storage when appropriate
- Implement efficient chunking
- Provide download scripts
- Document storage locations

## Workflow Best Practices

### Before Contributing
1. Review dataset documentation
2. Understand data schema and format
3. Check licensing and ethical guidelines
4. Set up local data validation
5. Test data loading and processing

### While Contributing
1. Follow data format specifications
2. Validate data before submission
3. Document data sources
4. Maintain consistent quality
5. Preserve data lineage
6. Consider downstream users
7. Test with dataset loaders

### Before Submitting
1. Run data validation scripts
2. Check for PII or sensitive data
3. Verify licensing compliance
4. Update documentation
5. Add examples if needed
6. Test dataset loading
7. Provide clear commit messages

## Collaboration Etiquette

- Respect data ownership and attribution
- Follow ethical guidelines strictly
- Document all data transformations
- Be transparent about limitations
- Acknowledge data contributors
- Respond to data quality issues
- Coordinate on schema changes
- Provide reproducible pipelines

## Useful Tools

### Data Validation
- `pandas` with schema validation
- `great_expectations` - Data testing
- `pandera` - Statistical data validation
- `jsonschema` - JSON validation
- `cerberus` - Python data validation

### Data Processing
- `pandas` - Data manipulation
- `polars` - Fast dataframe library
- `dask` - Parallel computing
- `pyarrow` - Columnar data
- `h5py` - HDF5 files

### Version Control
- `git-lfs` - Large file storage
- `dvc` - Data version control
- `dagshub` - Data science platform

### Dataset Platforms
- `huggingface-hub` - HF dataset utilities
- `kaggle` API - Kaggle datasets
- `datasets` library - HF datasets

## Common Commands

- `git lfs install` - Set up Git LFS
- `git lfs track "*.csv"` - Track large files
- `dvc add data/` - Track data with DVC
- `huggingface-cli upload` - Upload to HF
- `datasets-cli test` - Test dataset loading
- `kaggle datasets list` - List Kaggle datasets

## File Organization

Typical dataset repository structure:
```
dataset-repo/
├── README.md
├── DATACARD.md
├── LICENSE
├── data/
│   ├── train/
│   ├── validation/
│   └── test/
├── scripts/
│   ├── download.py
│   ├── validate.py
│   └── preprocess.py
├── metadata/
│   ├── schema.json
│   └── stats.json
├── examples/
│   └── load_dataset.py
└── tests/
    └── test_data_quality.py
```

## Dataset Licenses

Common data licenses:
- **CC0**: Public domain
- **CC-BY**: Attribution required
- **CC-BY-SA**: Share-alike
- **ODbL**: Open Database License
- **Custom**: Project-specific terms

Always verify license compatibility before combining datasets.
