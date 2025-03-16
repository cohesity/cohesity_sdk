# TenantAssignmentsParams

Parameters to be specified for assigning properties like storage domain, entities, policies to the tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[int]** | List of objects on the cluster, to be associated to the Tenant. | [optional] 
**policy_ids** | **List[str]** | List of policies on the cluster, to be associated to the Tenant. | [optional] 
**storage_domain_ids** | **List[int]** | List of storage domains on the cluster, to be associated to the Tenant. | [optional] 
**view_ids** | **List[int]** | List of views on the cluster, to be associated to the Tenant. | [optional] 
**vlan_iface_names** | **List[str]** | List of vlans on the cluster, to be associated to the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tenant_assignments_params import TenantAssignmentsParams

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAssignmentsParams from a JSON string
tenant_assignments_params_instance = TenantAssignmentsParams.from_json(json)
# print the JSON string representation of the object
print(TenantAssignmentsParams.to_json())

# convert the object into a dict
tenant_assignments_params_dict = tenant_assignments_params_instance.to_dict()
# create an instance of TenantAssignmentsParams from a dict
tenant_assignments_params_from_dict = TenantAssignmentsParams.from_dict(tenant_assignments_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


