# UpdateActiveDirectoryRequest

Specifies the request to create an Active Directory.

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
**trusted_domain_params** | [**TrustedDomainParams**](TrustedDomainParams.md) |  | [optional] 
**work_group_name** | **str** | Specifies a work group name. | [optional] 
**active_directory_admin_params** | [**ActiveDirectoryAdminParams**](ActiveDirectoryAdminParams.md) |  | [optional] 
**id_mapping_params** | [**IdMappingParams**](IdMappingParams.md) |  | [optional] 
**overwrite_machine_accounts** | **bool** | Specifies if specified machine accounts should overwrite existing machine accounts. | [optional] 
**transitive_ad_trust_level_limit** | **int** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_active_directory_request import UpdateActiveDirectoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateActiveDirectoryRequest from a JSON string
update_active_directory_request_instance = UpdateActiveDirectoryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateActiveDirectoryRequest.to_json())

# convert the object into a dict
update_active_directory_request_dict = update_active_directory_request_instance.to_dict()
# create an instance of UpdateActiveDirectoryRequest from a dict
update_active_directory_request_from_dict = UpdateActiveDirectoryRequest.from_dict(update_active_directory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


