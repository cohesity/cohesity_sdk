# Privilege

Specifies a Privileges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Specifies the Privilege category. | [optional] 
**description** | **str** | Specifies the description message for the Privilege. | [optional] 
**id** | **int** | Specifies the Privilege id. | [optional] 
**is_available_on_helios** | **bool** | Specifies whether the Privilege is available for Helios operations. | [optional] 
**is_custom_role_default** | **bool** | Specifies whether the Privilege is auto assigned to custom Roles. | [optional] 
**is_special** | **bool** | Specifies whether the Privilege is a special privilege. Special Privileges are not assigned to builtin &#39;Admin&#39; Role. | [optional] 
**is_view_only** | **bool** | Specifies whether the Privilege is a read-only privilege. Read-only Previlege only grants read access to a Role. | [optional] 
**label** | **str** | Specifies the Privilege label. | [optional] 
**name** | **str** | Specifies the Privilege name. | [optional] 

## Example

```python
from cohesity_sdk.models.privilege import Privilege

# TODO update the JSON string below
json = "{}"
# create an instance of Privilege from a JSON string
privilege_instance = Privilege.from_json(json)
# print the JSON string representation of the object
print(Privilege.to_json())

# convert the object into a dict
privilege_dict = privilege_instance.to_dict()
# create an instance of Privilege from a dict
privilege_from_dict = Privilege.from_dict(privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


