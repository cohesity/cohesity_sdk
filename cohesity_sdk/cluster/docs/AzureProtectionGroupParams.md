# AzureProtectionGroupParams

Specifies the parameters which are specific to Azure related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_protection_type_params** | [**AzureAgentProtectionGroupParams**](AzureAgentProtectionGroupParams.md) |  | [optional] 
**native_protection_type_params** | [**AzureNativeProtectionGroupParams**](AzureNativeProtectionGroupParams.md) |  | [optional] 
**protection_type** | **str** | Specifies the Azure Protection Group type. | 
**snapshot_manager_protection_type_params** | [**AzureSnapshotManagerProtectionGroupParams**](AzureSnapshotManagerProtectionGroupParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_protection_group_params import AzureProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProtectionGroupParams from a JSON string
azure_protection_group_params_instance = AzureProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AzureProtectionGroupParams.to_json())

# convert the object into a dict
azure_protection_group_params_dict = azure_protection_group_params_instance.to_dict()
# create an instance of AzureProtectionGroupParams from a dict
azure_protection_group_params_from_dict = AzureProtectionGroupParams.from_dict(azure_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


