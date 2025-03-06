# AAGInfo

Object details for Mssql.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the AAG name. | [optional] 
**object_id** | **int** | Specifies the AAG object Id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aag_info import AAGInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AAGInfo from a JSON string
aag_info_instance = AAGInfo.from_json(json)
# print the JSON string representation of the object
print(AAGInfo.to_json())

# convert the object into a dict
aag_info_dict = aag_info_instance.to_dict()
# create an instance of AAGInfo from a dict
aag_info_from_dict = AAGInfo.from_dict(aag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


