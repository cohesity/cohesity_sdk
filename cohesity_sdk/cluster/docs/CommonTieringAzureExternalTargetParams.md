# CommonTieringAzureExternalTargetParams

Specifies the common parameters which are specific to Azure related External Targets of tiering purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Specifies the client id of the managed identity assigned to the cluster This is used only for clusters running as Azure VMs where authentication is done using AD. | [optional] 
**container_name** | **str** | Specifies the container name of the external target. | 
**region** | **str** | Specifies region of the External Target. This is only populated for FortKnox vaults. | [optional] 
**storage_access_key** | **str** | Specifies the storage access key of the external target. | [optional] 
**storage_account_name** | **str** | Specifies the storage account name of the external target. | 
**storage_class** | **str** | Specifies the Azure External Target class. | 

## Example

```python
from cohesity_sdk.cluster.models.common_tiering_azure_external_target_params import CommonTieringAzureExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTieringAzureExternalTargetParams from a JSON string
common_tiering_azure_external_target_params_instance = CommonTieringAzureExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonTieringAzureExternalTargetParams.to_json())

# convert the object into a dict
common_tiering_azure_external_target_params_dict = common_tiering_azure_external_target_params_instance.to_dict()
# create an instance of CommonTieringAzureExternalTargetParams from a dict
common_tiering_azure_external_target_params_from_dict = CommonTieringAzureExternalTargetParams.from_dict(common_tiering_azure_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


