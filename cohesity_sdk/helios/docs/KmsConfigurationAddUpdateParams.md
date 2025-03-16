# KmsConfigurationAddUpdateParams

Parameters to update or add key management system(KMS) on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_target_ids** | **List[int]** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfiguration**](KmipKmsConfiguration.md) |  | [optional] 
**name** | **str** | Name of the KMS. | 
**storage_domain_ids** | **List[int]** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.kms_configuration_add_update_params import KmsConfigurationAddUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of KmsConfigurationAddUpdateParams from a JSON string
kms_configuration_add_update_params_instance = KmsConfigurationAddUpdateParams.from_json(json)
# print the JSON string representation of the object
print(KmsConfigurationAddUpdateParams.to_json())

# convert the object into a dict
kms_configuration_add_update_params_dict = kms_configuration_add_update_params_instance.to_dict()
# create an instance of KmsConfigurationAddUpdateParams from a dict
kms_configuration_add_update_params_from_dict = KmsConfigurationAddUpdateParams.from_dict(kms_configuration_add_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


