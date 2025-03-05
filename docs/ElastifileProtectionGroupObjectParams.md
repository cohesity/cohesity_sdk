# ElastifileProtectionGroupObjectParams

Specifies an object protected by an Elastifile Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the ID of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.elastifile_protection_group_object_params import ElastifileProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ElastifileProtectionGroupObjectParams from a JSON string
elastifile_protection_group_object_params_instance = ElastifileProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(ElastifileProtectionGroupObjectParams.to_json())

# convert the object into a dict
elastifile_protection_group_object_params_dict = elastifile_protection_group_object_params_instance.to_dict()
# create an instance of ElastifileProtectionGroupObjectParams from a dict
elastifile_protection_group_object_params_from_dict = ElastifileProtectionGroupObjectParams.from_dict(elastifile_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


