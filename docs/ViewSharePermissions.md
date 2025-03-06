# ViewSharePermissions

Specifies share permissions of the view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[SmbPermission]**](SmbPermission.md) | Specifies a list of share permissions. | [optional] 
**super_user_sids** | **List[str]** | Specifies a list of super user sids. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_share_permissions import ViewSharePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ViewSharePermissions from a JSON string
view_share_permissions_instance = ViewSharePermissions.from_json(json)
# print the JSON string representation of the object
print(ViewSharePermissions.to_json())

# convert the object into a dict
view_share_permissions_dict = view_share_permissions_instance.to_dict()
# create an instance of ViewSharePermissions from a dict
view_share_permissions_from_dict = ViewSharePermissions.from_dict(view_share_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


