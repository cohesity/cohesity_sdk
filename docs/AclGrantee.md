# AclGrantee

Specifies an ACL grantee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Specifies the group to which permissions are granted if the &#x60;type&#x60; is Group. | [optional] 
**type** | **str** | Specifies the grantee type. | 
**user_id** | **str** | Specifies the user id of the grantee if the &#x60;type&#x60; is Registered User. | [optional] 

## Example

```python
from cohesity_sdk.models.acl_grantee import AclGrantee

# TODO update the JSON string below
json = "{}"
# create an instance of AclGrantee from a JSON string
acl_grantee_instance = AclGrantee.from_json(json)
# print the JSON string representation of the object
print(AclGrantee.to_json())

# convert the object into a dict
acl_grantee_dict = acl_grantee_instance.to_dict()
# create an instance of AclGrantee from a dict
acl_grantee_from_dict = AclGrantee.from_dict(acl_grantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


