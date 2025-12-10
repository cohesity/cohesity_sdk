# IdentitySet

Represents a keyed collection of identity resources. It is used to represent a set of identities associated with various events for an item, such as created by or last modified by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**Identity**](Identity.md) |  | [optional] 
**user** | [**Identity**](Identity.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.identity_set import IdentitySet

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySet from a JSON string
identity_set_instance = IdentitySet.from_json(json)
# print the JSON string representation of the object
print(IdentitySet.to_json())

# convert the object into a dict
identity_set_dict = identity_set_instance.to_dict()
# create an instance of IdentitySet from a dict
identity_set_from_dict = IdentitySet.from_dict(identity_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


