# ActiveDirectory

Specifies an Active Directory.

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
**centrify_zones** | [**List[CentrifyZones]**](CentrifyZones.md) | Specifies a list of Centrify zones. | [optional] 
**domain_controllers** | [**List[DomainControllers]**](DomainControllers.md) | A list of domain names with a list of it&#39;s domain controllers. | [optional] 
**domain_name** | **str** | Specifies the domain name of the Active Directory. | [optional] 
**error** | [**ActiveDirectoryError**](ActiveDirectoryError.md) |  | [optional] 
**id_mapping_params** | **object** | Specifies the params of the user id mapping info of an Active Directory. | [optional] 
**permissions** | [**List[Tenant]**](Tenant.md) | Specifies the list of tenants that have permissions for this Active Directory. | [optional] 
**security_principals** | [**List[SecurityPrincipal]**](SecurityPrincipal.md) | Specifies a list of security principals. | [optional] 
**task_logs** | [**TaskLogs**](TaskLogs.md) |  | [optional] 
**transitive_ad_trust_level_limit** | **int** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directory import ActiveDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectory from a JSON string
active_directory_instance = ActiveDirectory.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectory.to_json())

# convert the object into a dict
active_directory_dict = active_directory_instance.to_dict()
# create an instance of ActiveDirectory from a dict
active_directory_from_dict = ActiveDirectory.from_dict(active_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


