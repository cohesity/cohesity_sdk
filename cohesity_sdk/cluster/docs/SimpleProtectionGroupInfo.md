# SimpleProtectionGroupInfo

Simplified protection group information with essential fields only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str** | ID of the protection group. | [optional] 
**protection_group_instance_id** | **int** | Instance ID of the protection group. | [optional] 
**protection_group_name** | **str** | Name of the protection group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.simple_protection_group_info import SimpleProtectionGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleProtectionGroupInfo from a JSON string
simple_protection_group_info_instance = SimpleProtectionGroupInfo.from_json(json)
# print the JSON string representation of the object
print(SimpleProtectionGroupInfo.to_json())

# convert the object into a dict
simple_protection_group_info_dict = simple_protection_group_info_instance.to_dict()
# create an instance of SimpleProtectionGroupInfo from a dict
simple_protection_group_info_from_dict = SimpleProtectionGroupInfo.from_dict(simple_protection_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


