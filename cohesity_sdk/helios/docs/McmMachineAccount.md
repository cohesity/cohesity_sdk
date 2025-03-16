# McmMachineAccount

Specifies a machine account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_host_name** | **str** | Specifies the DNS host name of the machine account. | [optional] 
**encryption** | **List[str]** | Specifies a list of encryption types apply to the machine account. | [optional] 
**is_primary_machine** | **bool** | Specifies whether this machine account is primary or not. | [optional] 
**name** | **str** | Specifies the machine account name. | 

## Example

```python
from cohesity_sdk.helios.models.mcm_machine_account import McmMachineAccount

# TODO update the JSON string below
json = "{}"
# create an instance of McmMachineAccount from a JSON string
mcm_machine_account_instance = McmMachineAccount.from_json(json)
# print the JSON string representation of the object
print(McmMachineAccount.to_json())

# convert the object into a dict
mcm_machine_account_dict = mcm_machine_account_instance.to_dict()
# create an instance of McmMachineAccount from a dict
mcm_machine_account_from_dict = McmMachineAccount.from_dict(mcm_machine_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


