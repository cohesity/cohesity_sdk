# TenantAssignmentProperties

List of all the assigned properties to a Tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | **List[int]** | A list of Ids of properties assigned to the tenant. | [optional] 
**policies** | [**ProtectionPolicyResponseWithPagination**](ProtectionPolicyResponseWithPagination.md) |  | [optional] 
**storage_domains** | [**StorageDomains**](StorageDomains.md) |  | [optional] 
**views** | [**GetViewsResult**](GetViewsResult.md) |  | [optional] 
**vlans** | **List[str]** | A list of Ids of properties assigned to the tenant. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tenant_assignment_properties import TenantAssignmentProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAssignmentProperties from a JSON string
tenant_assignment_properties_instance = TenantAssignmentProperties.from_json(json)
# print the JSON string representation of the object
print(TenantAssignmentProperties.to_json())

# convert the object into a dict
tenant_assignment_properties_dict = tenant_assignment_properties_instance.to_dict()
# create an instance of TenantAssignmentProperties from a dict
tenant_assignment_properties_from_dict = TenantAssignmentProperties.from_dict(tenant_assignment_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


