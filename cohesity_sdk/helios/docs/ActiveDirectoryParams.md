# ActiveDirectoryParams

Specifies the params of Active Directory which are used across creating and updating.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name of the Active Directory. | 
**machine_accounts** | [**List[McmMachineAccount]**](McmMachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified. | 
**organizational_unit_name** | **str** | Specifies an optional organizational unit name. | [optional] 
**preferred_domain_controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**trusted_domain_params** | [**TrustedDomainParams**](TrustedDomainParams.md) | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**work_group_name** | **str** | Specifies a work group name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directory_params import ActiveDirectoryParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryParams from a JSON string
active_directory_params_instance = ActiveDirectoryParams.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryParams.to_json())

# convert the object into a dict
active_directory_params_dict = active_directory_params_instance.to_dict()
# create an instance of ActiveDirectoryParams from a dict
active_directory_params_from_dict = ActiveDirectoryParams.from_dict(active_directory_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


