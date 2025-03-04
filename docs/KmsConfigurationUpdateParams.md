# KmsConfigurationUpdateParams

Parameters to update key management system(KMS) on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_target_ids** | **List[int]** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfiguration**](KmipKmsConfiguration.md) |  | [optional] 
**name** | **str** | Name of the KMS. | 
**storage_domain_ids** | **List[int]** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**aws_kms_params** | [**AwsKmsConfigurationUpdateParams**](AwsKmsConfigurationUpdateParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.kms_configuration_update_params import KmsConfigurationUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of KmsConfigurationUpdateParams from a JSON string
kms_configuration_update_params_instance = KmsConfigurationUpdateParams.from_json(json)
# print the JSON string representation of the object
print(KmsConfigurationUpdateParams.to_json())

# convert the object into a dict
kms_configuration_update_params_dict = kms_configuration_update_params_instance.to_dict()
# create an instance of KmsConfigurationUpdateParams from a dict
kms_configuration_update_params_from_dict = KmsConfigurationUpdateParams.from_dict(kms_configuration_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


