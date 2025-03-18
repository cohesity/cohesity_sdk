# MachineAccount

Specifies a machine account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_host_name** | **str** | Specifies the DNS host name of the machine account. | [optional] 
**encryption** | **List[str]** | Specifies a list of encryption types apply to the machine account. | [optional] 
**name** | **str** | Specifies the machine account name. | 
**service_principal_names** | **List[str]** | Specifies the customized Service Principal Names of the Machine Account. Service Principal Name should be unique across the Active Directory forest. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.machine_account import MachineAccount

# TODO update the JSON string below
json = "{}"
# create an instance of MachineAccount from a JSON string
machine_account_instance = MachineAccount.from_json(json)
# print the JSON string representation of the object
print(MachineAccount.to_json())

# convert the object into a dict
machine_account_dict = machine_account_instance.to_dict()
# create an instance of MachineAccount from a dict
machine_account_from_dict = MachineAccount.from_dict(machine_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


