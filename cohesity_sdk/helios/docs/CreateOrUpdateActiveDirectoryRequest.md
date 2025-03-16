# CreateOrUpdateActiveDirectoryRequest

Specifies the request to create an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name of the Active Directory. | 
**machine_accounts** | [**List[McmMachineAccount]**](McmMachineAccount.md) | Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified. | 
**organizational_unit_name** | **str** | Specifies an optional organizational unit name. | [optional] 
**preferred_domain_controllers** | [**List[DomainController]**](DomainController.md) | Specifies a list of preferred domain controllers of this Active Directory. | [optional] 
**trusted_domain_params** | [**TrustedDomainParams**](TrustedDomainParams.md) | Specifies the params of trusted domain info of an Active Directory. | [optional] 
**work_group_name** | **str** | Specifies a work group name. | [optional] 
**admin_params** | **object** | Specifies the params of a user with administrative privilege of this Active Directory. | 
**overwrite_machine_accounts** | **bool** | Specifies if specified machine accounts should overwrite existing machine accounts. | [optional] 
**trusted_domain_list** | [**List[TrustedDomainInfo]**](TrustedDomainInfo.md) | A list of domains which this domain trusts. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.create_or_update_active_directory_request import CreateOrUpdateActiveDirectoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateActiveDirectoryRequest from a JSON string
create_or_update_active_directory_request_instance = CreateOrUpdateActiveDirectoryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateActiveDirectoryRequest.to_json())

# convert the object into a dict
create_or_update_active_directory_request_dict = create_or_update_active_directory_request_instance.to_dict()
# create an instance of CreateOrUpdateActiveDirectoryRequest from a dict
create_or_update_active_directory_request_from_dict = CreateOrUpdateActiveDirectoryRequest.from_dict(create_or_update_active_directory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


