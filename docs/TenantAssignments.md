# TenantAssignments

All properties like entities, sources, policies etc assigned to the tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**TenantAssignmentsResult**](TenantAssignmentsResult.md) |  | [optional] 
**tenant_id** | **str** | The tenant id. | [optional] 

## Example

```python
from cohesity_sdk.models.tenant_assignments import TenantAssignments

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAssignments from a JSON string
tenant_assignments_instance = TenantAssignments.from_json(json)
# print the JSON string representation of the object
print(TenantAssignments.to_json())

# convert the object into a dict
tenant_assignments_dict = tenant_assignments_instance.to_dict()
# create an instance of TenantAssignments from a dict
tenant_assignments_from_dict = TenantAssignments.from_dict(tenant_assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


