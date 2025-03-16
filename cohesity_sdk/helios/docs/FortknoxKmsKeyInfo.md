# FortknoxKmsKeyInfo

Information about KMS key for Fortknox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the helios account. | 
**cloud_provider** | [**FortknoxCloudProvider**](FortknoxCloudProvider.md) |  | [optional] 
**kms_key_type** | **str** | Whether the KMS key is customer provided or by Cohesity. | 
**aws_params** | [**AwsKmsKeyResp**](AwsKmsKeyResp.md) |  | [optional] 
**global_kms_id** | **str** | ID that uniquely identifies a KMS key. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_kms_key_info import FortknoxKmsKeyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxKmsKeyInfo from a JSON string
fortknox_kms_key_info_instance = FortknoxKmsKeyInfo.from_json(json)
# print the JSON string representation of the object
print(FortknoxKmsKeyInfo.to_json())

# convert the object into a dict
fortknox_kms_key_info_dict = fortknox_kms_key_info_instance.to_dict()
# create an instance of FortknoxKmsKeyInfo from a dict
fortknox_kms_key_info_from_dict = FortknoxKmsKeyInfo.from_dict(fortknox_kms_key_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


