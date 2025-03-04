# DataTieringSource

Specifies the source data tiering details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment type of the data tiering source. | [optional] 
**generic_nas_params** | [**GenericNasDataTieringParams**](GenericNasDataTieringParams.md) |  | [optional] 
**isilon_params** | [**IsilonDataTieringParams**](IsilonDataTieringParams.md) |  | [optional] 
**netapp_params** | [**NetappDataTieringParams**](NetappDataTieringParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.data_tiering_source import DataTieringSource

# TODO update the JSON string below
json = "{}"
# create an instance of DataTieringSource from a JSON string
data_tiering_source_instance = DataTieringSource.from_json(json)
# print the JSON string representation of the object
print(DataTieringSource.to_json())

# convert the object into a dict
data_tiering_source_dict = data_tiering_source_instance.to_dict()
# create an instance of DataTieringSource from a dict
data_tiering_source_from_dict = DataTieringSource.from_dict(data_tiering_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


