# ActiveDirectoryAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**centrify_zones** | [**[CentrifyZones], none_type**](CentrifyZones.md) | Specifies a list of Centrify zones. | [optional] 
**domain_controllers** | [**[DomainControllers], none_type**](DomainControllers.md) | A list of domain names with a list of it&#39;s domain controllers. | [optional] 
**domain_name** | **str, none_type** | Specifies the domain name of the Active Directory. | [optional] 
**error** | [**ActiveDirectoryError**](ActiveDirectoryError.md) |  | [optional] 
**id_mapping_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of the user id mapping info of an Active Directory. | [optional] 
**permissions** | [**[Tenant], none_type**](Tenant.md) | Specifies the list of tenants that have permissions for this Active Directory. | [optional] 
**security_principals** | [**[SecurityPrincipal], none_type**](SecurityPrincipal.md) | Specifies a list of security principals. | [optional] 
**task_logs** | [**TaskLogs**](TaskLogs.md) |  | [optional] 
**transitive_ad_trust_level_limit** | **int, none_type** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


