# KmsKeyBasicInfo

Information about KMS key per region.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | Holds the value of the customer provided KMS. This is only applicable if the KMS Type is customer managed. This is restricted to only AWS managed KMS. | [optional] 
**kms_key_type** | **str** | Whether the KMS key is customer provided or by Cohesity. | 

## Example

```python
from cohesity_sdk.helios.models.kms_key_basic_info import KmsKeyBasicInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KmsKeyBasicInfo from a JSON string
kms_key_basic_info_instance = KmsKeyBasicInfo.from_json(json)
# print the JSON string representation of the object
print(KmsKeyBasicInfo.to_json())

# convert the object into a dict
kms_key_basic_info_dict = kms_key_basic_info_instance.to_dict()
# create an instance of KmsKeyBasicInfo from a dict
kms_key_basic_info_from_dict = KmsKeyBasicInfo.from_dict(kms_key_basic_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


