# CommonActiveDirectoryParams

Specifies the params of Active Directory which are used across creating and updating.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_accounts** | [**[MachineAccount], none_type**](MachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified. | 
**id** | **int, none_type** | Specifies the id of the Active Directory. | [optional] [readonly] 
**organizational_unit_name** | **str, none_type** | Specifies an optional organizational unit name. | [optional] 
**work_group_name** | **str, none_type** | Specifies a work group name. | [optional] 
**preferred_domain_controllers** | [**[DomainController], none_type**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**ldap_provider_id** | **int, none_type** | Specifies the LDAP provider id which is mapped to this Active Directory | [optional] 
**trusted_domain_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**nis_provider_domain_name** | **str, none_type** | Specifies the name of the NIS Provider which is mapped to this Active Directory. | [optional] 
**connection_id** | **int, none_type** | Specifies the id of the connection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

