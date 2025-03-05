# CreationInfo

Specifies the information about the creation of the protection group or recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Specifies the name of the user who created the protection group or recovery. | [optional] 

## Example

```python
from cohesity_sdk.models.creation_info import CreationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreationInfo from a JSON string
creation_info_instance = CreationInfo.from_json(json)
# print the JSON string representation of the object
print(CreationInfo.to_json())

# convert the object into a dict
creation_info_dict = creation_info_instance.to_dict()
# create an instance of CreationInfo from a dict
creation_info_from_dict = CreationInfo.from_dict(creation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


