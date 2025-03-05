# ProtectionGroupIdentifier

Specifies Protection Group Identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str** | Specifies Protection Group id. | [optional] 
**protection_group_name** | **str** | Specifies Protection Group name. | [optional] 

## Example

```python
from cohesity_sdk.models.protection_group_identifier import ProtectionGroupIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupIdentifier from a JSON string
protection_group_identifier_instance = ProtectionGroupIdentifier.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupIdentifier.to_json())

# convert the object into a dict
protection_group_identifier_dict = protection_group_identifier_instance.to_dict()
# create an instance of ProtectionGroupIdentifier from a dict
protection_group_identifier_from_dict = ProtectionGroupIdentifier.from_dict(protection_group_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


