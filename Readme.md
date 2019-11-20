# PDF populator

How to Populate Fillable PDF's with Python using pdfrw

- [pdfrw](https://github.com/pmaupin/pdfrw)

```bash
pip3 install --user --upgrade ../pdf-populate/dist/pdf_populator-0.1.0.tar.gz
```

## Setup for dev

```bash
python3 -m venv venv
. ./venv/bin/active

pip install -r requirements.txt
```

## Populate pdf template
```bash
# Usage
python populate.py -h
usage: populate.py [-h] [--input INPUT] [--template TEMPLATE]
                   [--output-dir OUTPUT_DIR]

optional arguments:
  -h, --help               show this help message and exit
  --input INPUT            input file path
  --template TEMPLATE      template file path
  --output-dir OUTPUT_DIR  output directory path

# Example
python populate.py --input=./outputs/morgate-correct-answer.csv --template=./templates/Template2_MtgApp.pdf --output-dir=./outputs
```
