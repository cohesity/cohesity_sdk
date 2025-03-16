# GetFortknoxVaultsResp

Success response to get Fortknox vaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fortknox_vault_info_list** | [**List[FortknoxVaultInfo]**](FortknoxVaultInfo.md) | List of Fortknox vaults for a helios account | [optional] 

## Example

```python
from cohesity_sdk.helios.models.get_fortknox_vaults_resp import GetFortknoxVaultsResp

# TODO update the JSON string below
json = "{}"
# create an instance of GetFortknoxVaultsResp from a JSON string
get_fortknox_vaults_resp_instance = GetFortknoxVaultsResp.from_json(json)
# print the JSON string representation of the object
print(GetFortknoxVaultsResp.to_json())

# convert the object into a dict
get_fortknox_vaults_resp_dict = get_fortknox_vaults_resp_instance.to_dict()
# create an instance of GetFortknoxVaultsResp from a dict
get_fortknox_vaults_resp_from_dict = GetFortknoxVaultsResp.from_dict(get_fortknox_vaults_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


