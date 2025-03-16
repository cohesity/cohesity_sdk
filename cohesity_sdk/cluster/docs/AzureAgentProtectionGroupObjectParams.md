# AzureAgentProtectionGroupObjectParams

Specifies the object parameters to create agent based Azure Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.azure_agent_protection_group_object_params import AzureAgentProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureAgentProtectionGroupObjectParams from a JSON string
azure_agent_protection_group_object_params_instance = AzureAgentProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AzureAgentProtectionGroupObjectParams.to_json())

# convert the object into a dict
azure_agent_protection_group_object_params_dict = azure_agent_protection_group_object_params_instance.to_dict()
# create an instance of AzureAgentProtectionGroupObjectParams from a dict
azure_agent_protection_group_object_params_from_dict = AzureAgentProtectionGroupObjectParams.from_dict(azure_agent_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


