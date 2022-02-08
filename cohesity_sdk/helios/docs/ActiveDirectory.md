# ActiveDirectory

Specifies an Active Directory.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_accounts** | [**[MachineAccount], none_type**](MachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. | 
**id** | **int, none_type** | Specifies the id of the Active Directory. | [optional] [readonly] 
**organizational_unit_name** | **str, none_type** | Specifies an optional organizational unit name. | [optional] 
**work_group_name** | **str, none_type** | Specifies a work group name. | [optional] 
**preferred_domain_controllers** | [**[DomainController], none_type**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**ldap_provider_id** | **int, none_type** | Specifies the LDAP provider id which is mapped to this Active Directory | [optional] 
**trusted_domain_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**nis_provider_domain_name** | **str, none_type** | Specifies the name of the NIS Provider which is mapped to this Active Directory. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection. | [optional] 
**id_mapping_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of the user id mapping info of an Active Directory. | [optional] 
**domain_name** | **str, none_type** | Specifies the domain name of the Active Directory. | [optional] 
**centrify_zones** | [**[CentrifyZones], none_type**](CentrifyZones.md) | Specifies a list of centrify zones. | [optional] 
**domain_controllers** | [**[DomainControllers], none_type**](DomainControllers.md) | A list of domain names with a list of it&#39;s domain controllers. | [optional] 
**security_principals** | [**[SecurityPrincipal], none_type**](SecurityPrincipal.md) | Specifies a list of security principals. | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this Active Directory. | [optional] 
**transitive_ad_trust_level_limit** | **int, none_type** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


