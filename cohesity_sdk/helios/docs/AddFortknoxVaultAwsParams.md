# AddFortknoxVaultAwsParams

Fortknox AWS vault related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_params** | [**FortknoxAwsKmsReqParams**](FortknoxAwsKmsReqParams.md) |  | [optional] 
**region_id** | **str** | ID that identifies a region of the vault. | 
**vault_params** | [**FortknoxAwsVaultReqParams**](FortknoxAwsVaultReqParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_vault_aws_params import AddFortknoxVaultAwsParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxVaultAwsParams from a JSON string
add_fortknox_vault_aws_params_instance = AddFortknoxVaultAwsParams.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxVaultAwsParams.to_json())

# convert the object into a dict
add_fortknox_vault_aws_params_dict = add_fortknox_vault_aws_params_instance.to_dict()
# create an instance of AddFortknoxVaultAwsParams from a dict
add_fortknox_vault_aws_params_from_dict = AddFortknoxVaultAwsParams.from_dict(add_fortknox_vault_aws_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


