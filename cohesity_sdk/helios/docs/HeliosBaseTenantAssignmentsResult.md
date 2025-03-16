# HeliosBaseTenantAssignmentsResult

Result of attempted tenant assignments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies the the cluster on which properties are to be assigned. The format is clusterId:clusterIncarnationId. | [optional] 
**policies** | **List[str]** | A list of Ids of properties assigned to the tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_base_tenant_assignments_result import HeliosBaseTenantAssignmentsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosBaseTenantAssignmentsResult from a JSON string
helios_base_tenant_assignments_result_instance = HeliosBaseTenantAssignmentsResult.from_json(json)
# print the JSON string representation of the object
print(HeliosBaseTenantAssignmentsResult.to_json())

# convert the object into a dict
helios_base_tenant_assignments_result_dict = helios_base_tenant_assignments_result_instance.to_dict()
# create an instance of HeliosBaseTenantAssignmentsResult from a dict
helios_base_tenant_assignments_result_from_dict = HeliosBaseTenantAssignmentsResult.from_dict(helios_base_tenant_assignments_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


