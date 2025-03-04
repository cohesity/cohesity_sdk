# PstParam

Specifies the PST conversion specific parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_pst** | **bool** | Specifies if create a PST or MSG for input items. | [optional] 
**password** | **str** | Specifies Password to be set for generated PSTs. | 
**size_threshold_bytes** | **int** | Specifies PST size threshold in bytes. | [optional] 

## Example

```python
from cohesity_sdk.models.pst_param import PstParam

# TODO update the JSON string below
json = "{}"
# create an instance of PstParam from a JSON string
pst_param_instance = PstParam.from_json(json)
# print the JSON string representation of the object
print(PstParam.to_json())

# convert the object into a dict
pst_param_dict = pst_param_instance.to_dict()
# create an instance of PstParam from a dict
pst_param_from_dict = PstParam.from_dict(pst_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


