# KmsConfiguration

 Key management system(KMS) configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_kms_params** | [**AwsKmsConfigurationResponse**](AwsKmsConfigurationResponse.md) |  | [optional] 
**external_target_ids** | **List[int]** | Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed. | [optional] 
**kmip_kms_params** | [**KmipKmsConfigurationResponse**](KmipKmsConfigurationResponse.md) |  | [optional] 
**name** | **str** | Name of the KMS. | [optional] 
**ownership_context** | **str** | Describes the consumption of the KMS key whether it is used for local or FortKnox. | [optional] 
**storage_domain_ids** | **List[int]** | Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed. | [optional] 
**type** | **str** | Type of KMS. &#39;InternalKms&#39; indicates the internal cluster KMS. &#39;AwsKms&#39; indicates AWS KMS. &#39;KmipKms&#39; indicates any KMIP compliant KMS. | [optional] 
**usage_type** | **str** | Specifies the usage type of the kms config. &#39;kArchival&#39; indicates this is used for regular archival. &#39;kRpaasArchival&#39; indicates this is used for RPaaS only. | [optional] 
**id** | **int** | Id of KMS. | [optional] [readonly] 
**state** | **str** | Specifies the state of KMS. &#39;Active&#39; indicates that KMS is reachable from cluster. &#39;InActive&#39; indicates that KMS is not reachable from cluster. &#39;MarkedForRemoval&#39; indicates that KMS is marked for removal and the removal process is in progress. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.kms_configuration import KmsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of KmsConfiguration from a JSON string
kms_configuration_instance = KmsConfiguration.from_json(json)
# print the JSON string representation of the object
print(KmsConfiguration.to_json())

# convert the object into a dict
kms_configuration_dict = kms_configuration_instance.to_dict()
# create an instance of KmsConfiguration from a dict
kms_configuration_from_dict = KmsConfiguration.from_dict(kms_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


