# VdcCatalog

Specifies a VDC Catalog.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the catalog. | [optional] [readonly] 
**uuid** | **str** | Specifies the UUID of the catalog. | 

## Example

```python
from cohesity_sdk.models.vdc_catalog import VdcCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of VdcCatalog from a JSON string
vdc_catalog_instance = VdcCatalog.from_json(json)
# print the JSON string representation of the object
print(VdcCatalog.to_json())

# convert the object into a dict
vdc_catalog_dict = vdc_catalog_instance.to_dict()
# create an instance of VdcCatalog from a dict
vdc_catalog_from_dict = VdcCatalog.from_dict(vdc_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


