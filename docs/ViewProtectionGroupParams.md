# ViewProtectionGroupParams

Specifies the parameters which are specific to view related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externally_triggered_job_params** | [**ExternallyTriggeredJobParams**](ExternallyTriggeredJobParams.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[ViewProtectionGroupObjectParams]**](ViewProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**replication_params** | [**ViewProtectionGroupReplicationParams**](ViewProtectionGroupReplicationParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.view_protection_group_params import ViewProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtectionGroupParams from a JSON string
view_protection_group_params_instance = ViewProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(ViewProtectionGroupParams.to_json())

# convert the object into a dict
view_protection_group_params_dict = view_protection_group_params_instance.to_dict()
# create an instance of ViewProtectionGroupParams from a dict
view_protection_group_params_from_dict = ViewProtectionGroupParams.from_dict(view_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


