# Groups

Specifies a list of groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GroupParams]**](GroupParams.md) | Specifies the list of groups. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.groups import Groups

# TODO update the JSON string below
json = "{}"
# create an instance of Groups from a JSON string
groups_instance = Groups.from_json(json)
# print the JSON string representation of the object
print(Groups.to_json())

# convert the object into a dict
groups_dict = groups_instance.to_dict()
# create an instance of Groups from a dict
groups_from_dict = Groups.from_dict(groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


