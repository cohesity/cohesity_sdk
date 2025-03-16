# Role

Specifies a Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the Role name. | 
**description** | **str** | Specifies the description message for the Role. | [optional] 
**privileges** | **List[str]** | Specifies the list of Privileges of the Role. | 
**created_timestamp_msecs** | **int** | Specifies the timestamp when the Role is created in milliseconds. | [optional] 
**is_user_created_role** | **bool** | Specifies if the Role is created by user. | [optional] 
**label** | **str** | Specifies the Role label. | [optional] 
**last_updated_timestamp_msecs** | **int** | Specifies the timestamp when the Role is last updated in milliseconds. | [optional] 
**tenant_ids** | **List[str]** | Specifies the list of tenant ids who have access to this Role. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print(Role.to_json())

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


