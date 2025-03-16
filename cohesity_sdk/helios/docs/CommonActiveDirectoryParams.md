# CommonActiveDirectoryParams

Specifies the params of Active Directory which are used across creating and updating.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** | Specifies the id of the connection. | [optional] 
**domain_controllers_deny_list** | **List[Optional[str]]** | Specifies a list of denied domain controllers of this Active Directory Domain. | [optional] 
**id** | **int** | Specifies the id of the Active Directory. | [optional] [readonly] 
**ldap_provider_id** | **int** | Specifies the LDAP provider id which is mapped to this Active Directory | [optional] 
**machine_accounts** | [**List[MachineAccount]**](MachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified. | 
**nis_provider_domain_name** | **str** | Specifies the name of the NIS Provider which is mapped to this Active Directory. | [optional] 
**organizational_unit_name** | **str** | Specifies an optional organizational unit name. | [optional] 
**preferred_domain_controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**trusted_domain_params** | [**TrustedDomainParams**](TrustedDomainParams.md) | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**work_group_name** | **str** | Specifies a work group name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_active_directory_params import CommonActiveDirectoryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonActiveDirectoryParams from a JSON string
common_active_directory_params_instance = CommonActiveDirectoryParams.from_json(json)
# print the JSON string representation of the object
print(CommonActiveDirectoryParams.to_json())

# convert the object into a dict
common_active_directory_params_dict = common_active_directory_params_instance.to_dict()
# create an instance of CommonActiveDirectoryParams from a dict
common_active_directory_params_from_dict = CommonActiveDirectoryParams.from_dict(common_active_directory_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


