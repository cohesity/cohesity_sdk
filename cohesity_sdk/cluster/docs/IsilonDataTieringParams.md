# IsilonDataTieringParams

Specifies the parameters which are specific to Isilon related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the root of data tiering source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.isilon_data_tiering_params import IsilonDataTieringParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsilonDataTieringParams from a JSON string
isilon_data_tiering_params_instance = IsilonDataTieringParams.from_json(json)
# print the JSON string representation of the object
print(IsilonDataTieringParams.to_json())

# convert the object into a dict
isilon_data_tiering_params_dict = isilon_data_tiering_params_instance.to_dict()
# create an instance of IsilonDataTieringParams from a dict
isilon_data_tiering_params_from_dict = IsilonDataTieringParams.from_dict(isilon_data_tiering_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


