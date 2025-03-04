# Ldaps

Specifies a list of LDAPs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldaps** | [**List[Ldap]**](Ldap.md) | Specifies the list of LDAPs. | [optional] 

## Example

```python
from cohesity_sdk.models.ldaps import Ldaps

# TODO update the JSON string below
json = "{}"
# create an instance of Ldaps from a JSON string
ldaps_instance = Ldaps.from_json(json)
# print the JSON string representation of the object
print(Ldaps.to_json())

# convert the object into a dict
ldaps_dict = ldaps_instance.to_dict()
# create an instance of Ldaps from a dict
ldaps_from_dict = Ldaps.from_dict(ldaps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


