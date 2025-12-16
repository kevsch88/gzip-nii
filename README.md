# gzip-nii

A simple command-line tool for compressing NIfTI (Neuroimaging Informatics Technology Initiative) files using gzip compression.

## Overview

This tool uses the `nibabel` package to load and save NIfTI files, automatically applying gzip compression to reduce file sizes.

## Installation

Requires Python 3.x and nibabel:

```bash
pip install nibabel
```

## Usage

Basic usage:

```bash
python compress_nii.py input_file.nii
```

This will create a compressed file `input_file.nii.gz` in the same directory.

### Options

- `input_file` (required): Path to the input NIfTI file
- `-o, --output_file` (optional): Path to the output compressed file. Defaults to the input filename with `.nii.gz` extension

### Examples

Compress a file with default output name:
```bash
python compress_nii.py brain_img.nii
# Creates: brain_img.nii.gz
```

Specify a custom output path:
```bash
python compress_nii.py brain_img.nii -o compressed/brain_img.nii.gz
```

## Features / Checks

- Automatically creates output directories if they don't exist
- Validates that input file exists
- Prevents overwriting the input file
- Ensures output file has `.gz` extension
