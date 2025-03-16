# McmActiveDirectory

Specifies an Active Directory config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name of the Active Directory. | 
**machine_accounts** | [**List[McmMachineAccount]**](McmMachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified. | 
**organizational_unit_name** | **str** | Specifies an optional organizational unit name. | [optional] 
**preferred_domain_controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**trusted_domain_params** | [**TrustedDomainParams**](TrustedDomainParams.md) | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**work_group_name** | **str** | Specifies a work group name. | [optional] 
**domain_controllers** | [**List[DomainControllers]**](DomainControllers.md) | A list of domain names with a list of it&#39;s domain controllers. | [optional] 
**error** | [**ActiveDirectoryError**](ActiveDirectoryError.md) |  | [optional] 
**transitive_active_directory_trust_level_limit** | **int** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 
**trusted_domain_list** | [**List[TrustedDomainInfo]**](TrustedDomainInfo.md) | A list of domains which this domain trusts. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_active_directory import McmActiveDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of McmActiveDirectory from a JSON string
mcm_active_directory_instance = McmActiveDirectory.from_json(json)
# print the JSON string representation of the object
print(McmActiveDirectory.to_json())

# convert the object into a dict
mcm_active_directory_dict = mcm_active_directory_instance.to_dict()
# create an instance of McmActiveDirectory from a dict
mcm_active_directory_from_dict = McmActiveDirectory.from_dict(mcm_active_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


