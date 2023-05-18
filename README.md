# Model Excel Importer
Repository with functions to import an excel model, with the last COBRA structure version, to cobrapy.
## Excel structure
https://github.com/opencobra/cobratoolbox/blob/master/docs/source/notes/ExcelModelFileDefinition.md

## Requirements
- Pandas >= 1.0
- Cobra >= 0.15
- openxyl >= 3.0.0

## Usage
### Loading a model
```
import importExcelModel

my_model=importExcelModel.import_excel_model(file_path,model_id='my_model')
```
### Export excel model to SBML format
```
import importExcelModel

importExcelModel.excel_to_sbml(file_path,sbml_file_path,model_id='my_model')

```
### Export cobrapy model to excel format
```
import importExcelModel

importExcelModel.cobrapy_to_excel(model,'myModel.xlsx')

```
### Export pandas dataframe to cobrapy model
```
import importExcelModel

model=importExcelModel.dataframe_to_model(reactions_dataframe,metabolites_dataframe)

```
### Export cobrapy model to pandas dataframes
```
import importExcelModel

[reactions,metabolites]=importExcelModel.model_to_dataframe(model)

```

