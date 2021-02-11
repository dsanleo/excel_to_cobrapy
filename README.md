# Model Excel Importer
Repository with functions to import an excel model, with the last COBRA structure version, to cobrapy.
## Excel structure
https://github.com/opencobra/cobratoolbox/blob/master/docs/source/notes/ExcelModelFileDefinition.md

## Requirements
- Pandas >= 1.0
- Cobra >= 0.15

## Usage
```
import importExcelModel

my_model=importExcelModel.import_excel_model(file_path,model_id='my_model')
```
