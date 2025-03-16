# AddFortknoxVaultParams

Information about each Fortknox vault that is being added.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AddFortknoxVaultAwsParams**](AddFortknoxVaultAwsParams.md) |  | [optional] 
**azure_params** | [**AddFortknoxVaultAzureParams**](AddFortknoxVaultAzureParams.md) |  | [optional] 
**cloud_provider** | [**FortknoxCloudProvider**](FortknoxCloudProvider.md) |  | 
**kms_key_type** | **str** | Whether the KMS key is customer provided or by Cohesity. | 
**vault_name** | **str** | Fortknox vault name. | 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_vault_params import AddFortknoxVaultParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxVaultParams from a JSON string
add_fortknox_vault_params_instance = AddFortknoxVaultParams.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxVaultParams.to_json())

# convert the object into a dict
add_fortknox_vault_params_dict = add_fortknox_vault_params_instance.to_dict()
# create an instance of AddFortknoxVaultParams from a dict
add_fortknox_vault_params_from_dict = AddFortknoxVaultParams.from_dict(add_fortknox_vault_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


