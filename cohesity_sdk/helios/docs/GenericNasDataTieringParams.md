# GenericNasDataTieringParams

Specifies the parameters which are specific to NAS related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the root of data tiering source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.generic_nas_data_tiering_params import GenericNasDataTieringParams

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNasDataTieringParams from a JSON string
generic_nas_data_tiering_params_instance = GenericNasDataTieringParams.from_json(json)
# print the JSON string representation of the object
print(GenericNasDataTieringParams.to_json())

# convert the object into a dict
generic_nas_data_tiering_params_dict = generic_nas_data_tiering_params_instance.to_dict()
# create an instance of GenericNasDataTieringParams from a dict
generic_nas_data_tiering_params_from_dict = GenericNasDataTieringParams.from_dict(generic_nas_data_tiering_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


