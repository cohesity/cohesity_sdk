# FortknoxVaultInfo

Account specific information about a Fortknox vault.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the helios account | [optional] 
**aws_params** | [**FortknoxVaultAwsResp**](FortknoxVaultAwsResp.md) |  | [optional] 
**azure_params** | [**FortknoxVaultAzureResp**](FortknoxVaultAzureResp.md) |  | [optional] 
**cloud_provider** | [**FortknoxCloudProvider**](FortknoxCloudProvider.md) |  | [optional] 
**cluster_pairing_info** | [**List[FortknoxClusterPairingInfo]**](FortknoxClusterPairingInfo.md) | Provides the list of configured cluster pairing info with this Fortknox vault. | [optional] 
**deletion_status** | [**FortknoxProvisionDeletionStatus**](FortknoxProvisionDeletionStatus.md) |  | [optional] 
**global_vault_id** | **str** | Global Fortknox vault identifier. | [optional] 
**kms_key_type** | **str** | Indicates whether the KMS key type is Cohesity KMS or Customer managed KMS. | [optional] 
**provision_status** | [**FortknoxProvisionStatus**](FortknoxProvisionStatus.md) |  | [optional] 
**transfer_time_config_params** | [**TransferTimeConfigParamsList**](TransferTimeConfigParamsList.md) |  | [optional] 
**vault_name** | **str** | Fortknox vault name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_vault_info import FortknoxVaultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxVaultInfo from a JSON string
fortknox_vault_info_instance = FortknoxVaultInfo.from_json(json)
# print the JSON string representation of the object
print(FortknoxVaultInfo.to_json())

# convert the object into a dict
fortknox_vault_info_dict = fortknox_vault_info_instance.to_dict()
# create an instance of FortknoxVaultInfo from a dict
fortknox_vault_info_from_dict = FortknoxVaultInfo.from_dict(fortknox_vault_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


