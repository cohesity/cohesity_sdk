# PermissionInfo

Specifies the list of users, groups and users that have permissions for a given object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) | Specifies the list of user groups which has permissions to the object. | [optional] 
**object_id** | **int** | Specifies the id of the object. | [optional] 
**tenant** | [**TenantInfo**](TenantInfo.md) |  | [optional] 
**users** | [**List[User]**](User.md) | Specifies the list of users which has the permissions to the object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.permission_info import PermissionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionInfo from a JSON string
permission_info_instance = PermissionInfo.from_json(json)
# print the JSON string representation of the object
print(PermissionInfo.to_json())

# convert the object into a dict
permission_info_dict = permission_info_instance.to_dict()
# create an instance of PermissionInfo from a dict
permission_info_from_dict = PermissionInfo.from_dict(permission_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


