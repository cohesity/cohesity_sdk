# CreateGroupsParams

Specifies the parameters to add one or more Cohesity groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[CreateGroupParams]**](CreateGroupParams.md) | Specifies the list of groups to be created. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_groups_params import CreateGroupsParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupsParams from a JSON string
create_groups_params_instance = CreateGroupsParams.from_json(json)
# print the JSON string representation of the object
print(CreateGroupsParams.to_json())

# convert the object into a dict
create_groups_params_dict = create_groups_params_instance.to_dict()
# create an instance of CreateGroupsParams from a dict
create_groups_params_from_dict = CreateGroupsParams.from_dict(create_groups_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


