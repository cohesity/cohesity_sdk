# KmsConfigurationCreateParams

Parameters to add key management system(KMS) on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_target_ids** | **List[int]** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfiguration**](KmipKmsConfiguration.md) |  | [optional] 
**name** | **str** | Name of the KMS. | 
**storage_domain_ids** | **List[int]** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**aws_kms_params** | [**AwsKmsConfiguration**](AwsKmsConfiguration.md) |  | [optional] 
**ownership_context** | **str** | Specifies the ownership context of the kms config. &#39;Local&#39; indicates this is used for regular archival. &#39;FortKnox&#39; indicates this is used for FortKnox only. | [optional] 
**type** | **str** | Type of KMS. &#39;InternalKms&#39; indicates the internal cluster KMS. &#39;AwsKms&#39; indicates AWS KMS. &#39;KmipKms&#39; indicates any KMIP compliant KMS. | 
**usage_type** | **str** | Specifies the usage type of the kms config. &#39;kArchival&#39; indicates this is used for regular archival. &#39;kRpaasArchival&#39; indicates this is used for RPaaS only. | [optional] 

## Example

```python
from cohesity_sdk.models.kms_configuration_create_params import KmsConfigurationCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of KmsConfigurationCreateParams from a JSON string
kms_configuration_create_params_instance = KmsConfigurationCreateParams.from_json(json)
# print the JSON string representation of the object
print(KmsConfigurationCreateParams.to_json())

# convert the object into a dict
kms_configuration_create_params_dict = kms_configuration_create_params_instance.to_dict()
# create an instance of KmsConfigurationCreateParams from a dict
kms_configuration_create_params_from_dict = KmsConfigurationCreateParams.from_dict(kms_configuration_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


