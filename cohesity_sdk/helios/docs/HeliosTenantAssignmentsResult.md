# HeliosTenantAssignmentsResult

All properties like entities, sources, policies etc assigned to the tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**HeliosBaseTenantAssignmentsResult**](HeliosBaseTenantAssignmentsResult.md) |  | [optional] 
**tenant_id** | **str** | The tenant id. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tenant_assignments_result import HeliosTenantAssignmentsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTenantAssignmentsResult from a JSON string
helios_tenant_assignments_result_instance = HeliosTenantAssignmentsResult.from_json(json)
# print the JSON string representation of the object
print(HeliosTenantAssignmentsResult.to_json())

# convert the object into a dict
helios_tenant_assignments_result_dict = helios_tenant_assignments_result_instance.to_dict()
# create an instance of HeliosTenantAssignmentsResult from a dict
helios_tenant_assignments_result_from_dict = HeliosTenantAssignmentsResult.from_dict(helios_tenant_assignments_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


