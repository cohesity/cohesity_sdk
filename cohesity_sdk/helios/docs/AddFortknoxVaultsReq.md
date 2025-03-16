# AddFortknoxVaultsReq

Request params for adding Fortknox vaults for a helios account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vaults** | [**List[AddFortknoxVaultParams]**](AddFortknoxVaultParams.md) | List of vaults being added. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_vaults_req import AddFortknoxVaultsReq

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxVaultsReq from a JSON string
add_fortknox_vaults_req_instance = AddFortknoxVaultsReq.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxVaultsReq.to_json())

# convert the object into a dict
add_fortknox_vaults_req_dict = add_fortknox_vaults_req_instance.to_dict()
# create an instance of AddFortknoxVaultsReq from a dict
add_fortknox_vaults_req_from_dict = AddFortknoxVaultsReq.from_dict(add_fortknox_vaults_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


