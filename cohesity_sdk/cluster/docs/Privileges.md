# Privileges

Specifies a list of Privileges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileges** | [**List[Privilege]**](Privilege.md) | Specifies the list of Privileges. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.privileges import Privileges

# TODO update the JSON string below
json = "{}"
# create an instance of Privileges from a JSON string
privileges_instance = Privileges.from_json(json)
# print the JSON string representation of the object
print(Privileges.to_json())

# convert the object into a dict
privileges_dict = privileges_instance.to_dict()
# create an instance of Privileges from a dict
privileges_from_dict = Privileges.from_dict(privileges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


