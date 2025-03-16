# FortknoxAwsVaultRespParams

Fortknox AWS vault related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Name of the S3 bucket that is configured for a vault. | [optional] 
**storage_class** | **str** | Specifies the AWS storage class. When the storageClass is not given, set it to the default value, &#39;kAmazonS3StandardIA&#39;. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_aws_vault_resp_params import FortknoxAwsVaultRespParams

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxAwsVaultRespParams from a JSON string
fortknox_aws_vault_resp_params_instance = FortknoxAwsVaultRespParams.from_json(json)
# print the JSON string representation of the object
print(FortknoxAwsVaultRespParams.to_json())

# convert the object into a dict
fortknox_aws_vault_resp_params_dict = fortknox_aws_vault_resp_params_instance.to_dict()
# create an instance of FortknoxAwsVaultRespParams from a dict
fortknox_aws_vault_resp_params_from_dict = FortknoxAwsVaultRespParams.from_dict(fortknox_aws_vault_resp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


