# HeliosTenantAssignmentsParams

Parameters to be specified for assigning properties like policies to a tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies the the cluster on which properties are to be assigned. The format is clusterId:clusterIncarnationId. | [optional] 
**policy_ids** | **List[str]** | List of policies on the cluster, to be assigned to the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tenant_assignments_params import HeliosTenantAssignmentsParams

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTenantAssignmentsParams from a JSON string
helios_tenant_assignments_params_instance = HeliosTenantAssignmentsParams.from_json(json)
# print the JSON string representation of the object
print(HeliosTenantAssignmentsParams.to_json())

# convert the object into a dict
helios_tenant_assignments_params_dict = helios_tenant_assignments_params_instance.to_dict()
# create an instance of HeliosTenantAssignmentsParams from a dict
helios_tenant_assignments_params_from_dict = HeliosTenantAssignmentsParams.from_dict(helios_tenant_assignments_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


