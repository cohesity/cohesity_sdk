# InterfaceGroups

Interface groups configured on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_groups** | [**List[InterfaceGroup]**](InterfaceGroup.md) | Interface groups configured on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.interface_groups import InterfaceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of InterfaceGroups from a JSON string
interface_groups_instance = InterfaceGroups.from_json(json)
# print the JSON string representation of the object
print(InterfaceGroups.to_json())

# convert the object into a dict
interface_groups_dict = interface_groups_instance.to_dict()
# create an instance of InterfaceGroups from a dict
interface_groups_from_dict = InterfaceGroups.from_dict(interface_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


