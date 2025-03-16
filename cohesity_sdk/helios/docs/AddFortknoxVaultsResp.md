# AddFortknoxVaultsResp

Success response to add Fortknox vaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fortknox_vault_info_list** | [**List[FortknoxVaultInfo]**](FortknoxVaultInfo.md) | List of Fortknox vaults for a helios account | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_vaults_resp import AddFortknoxVaultsResp

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxVaultsResp from a JSON string
add_fortknox_vaults_resp_instance = AddFortknoxVaultsResp.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxVaultsResp.to_json())

# convert the object into a dict
add_fortknox_vaults_resp_dict = add_fortknox_vaults_resp_instance.to_dict()
# create an instance of AddFortknoxVaultsResp from a dict
add_fortknox_vaults_resp_from_dict = AddFortknoxVaultsResp.from_dict(add_fortknox_vaults_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


