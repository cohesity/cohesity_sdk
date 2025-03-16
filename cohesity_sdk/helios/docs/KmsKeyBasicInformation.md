# KmsKeyBasicInformation

Information about one KMS key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the helios account. | 
**cloud_provider** | [**FortknoxCloudProvider**](FortknoxCloudProvider.md) |  | [optional] 
**kms_key_type** | **str** | Whether the KMS key is customer provided or by Cohesity. | 

## Example

```python
from cohesity_sdk.helios.models.kms_key_basic_information import KmsKeyBasicInformation

# TODO update the JSON string below
json = "{}"
# create an instance of KmsKeyBasicInformation from a JSON string
kms_key_basic_information_instance = KmsKeyBasicInformation.from_json(json)
# print the JSON string representation of the object
print(KmsKeyBasicInformation.to_json())

# convert the object into a dict
kms_key_basic_information_dict = kms_key_basic_information_instance.to_dict()
# create an instance of KmsKeyBasicInformation from a dict
kms_key_basic_information_from_dict = KmsKeyBasicInformation.from_dict(kms_key_basic_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


