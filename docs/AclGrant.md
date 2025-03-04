# AclGrant

Specifies an ACL grant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantee** | [**AclGrantee**](AclGrantee.md) |  | 
**permissions** | **List[str]** | Specifies a list of permissions granted to the grantees. | 

## Example

```python
from cohesity_sdk.models.acl_grant import AclGrant

# TODO update the JSON string below
json = "{}"
# create an instance of AclGrant from a JSON string
acl_grant_instance = AclGrant.from_json(json)
# print the JSON string representation of the object
print(AclGrant.to_json())

# convert the object into a dict
acl_grant_dict = acl_grant_instance.to_dict()
# create an instance of AclGrant from a dict
acl_grant_from_dict = AclGrant.from_dict(acl_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


