# AzureAgentProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups using cohesity protection-service installed on the instance. Objects must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. | [optional] 
**cloud_migration** | **bool** | Specifies whether or not to move the workload to the cloud. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[AzureAgentProtectionGroupObjectParams]**](AzureAgentProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.azure_agent_protection_group_params import AzureAgentProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAgentProtectionGroupParams from a JSON string
azure_agent_protection_group_params_instance = AzureAgentProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureAgentProtectionGroupParams.to_json())

# convert the object into a dict
azure_agent_protection_group_params_dict = azure_agent_protection_group_params_instance.to_dict()
# create an instance of AzureAgentProtectionGroupParams from a dict
azure_agent_protection_group_params_from_dict = AzureAgentProtectionGroupParams.from_dict(azure_agent_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


