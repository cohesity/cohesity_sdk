# FortknoxAwsVaultReqParams

Fortknox AWS vault related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_class** | **str** | Specifies the AWS storage class. When the storageClass is not given, set it to the default value, &#39;kAmazonS3StandardIA&#39;. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_aws_vault_req_params import FortknoxAwsVaultReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxAwsVaultReqParams from a JSON string
fortknox_aws_vault_req_params_instance = FortknoxAwsVaultReqParams.from_json(json)
# print the JSON string representation of the object
print(FortknoxAwsVaultReqParams.to_json())

# convert the object into a dict
fortknox_aws_vault_req_params_dict = fortknox_aws_vault_req_params_instance.to_dict()
# create an instance of FortknoxAwsVaultReqParams from a dict
fortknox_aws_vault_req_params_from_dict = FortknoxAwsVaultReqParams.from_dict(fortknox_aws_vault_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


