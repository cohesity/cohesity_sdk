# FortknoxVaultAwsResp

Information about each Fortknox vault that is being added.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **str** | ID that identifies a region. | [optional] 
**vault_params** | [**FortknoxAwsVaultRespParams**](FortknoxAwsVaultRespParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_vault_aws_resp import FortknoxVaultAwsResp

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxVaultAwsResp from a JSON string
fortknox_vault_aws_resp_instance = FortknoxVaultAwsResp.from_json(json)
# print the JSON string representation of the object
print(FortknoxVaultAwsResp.to_json())

# convert the object into a dict
fortknox_vault_aws_resp_dict = fortknox_vault_aws_resp_instance.to_dict()
# create an instance of FortknoxVaultAwsResp from a dict
fortknox_vault_aws_resp_from_dict = FortknoxVaultAwsResp.from_dict(fortknox_vault_aws_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


