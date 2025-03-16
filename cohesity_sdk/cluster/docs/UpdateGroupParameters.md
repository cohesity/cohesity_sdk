# UpdateGroupParameters

Specifies group properties to update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description of the group. | [optional] 
**local_group_params** | [**LocalGroupParams**](LocalGroupParams.md) |  | [optional] 
**restricted** | **bool** | Specifies whether the Group is restricted. A restricted group can only view &amp; manage the objects it has permissions to. | [optional] 
**roles** | **List[str]** | Specifies the Cohesity roles to associate with the group. The Cohesity roles determine privileges on the Cohesity Cluster for this group. | [optional] 
**tenant_ids** | **List[str]** | Specifies a list of tenant ids who can access this group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_group_parameters import UpdateGroupParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupParameters from a JSON string
update_group_parameters_instance = UpdateGroupParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupParameters.to_json())

# convert the object into a dict
update_group_parameters_dict = update_group_parameters_instance.to_dict()
# create an instance of UpdateGroupParameters from a dict
update_group_parameters_from_dict = UpdateGroupParameters.from_dict(update_group_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


