# AssignClusterToTenantParamsBody

Params to assign a cluster or region to a tenant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.assign_cluster_to_tenant_params_body import AssignClusterToTenantParamsBody

# TODO update the JSON string below
json = "{}"
# create an instance of AssignClusterToTenantParamsBody from a JSON string
assign_cluster_to_tenant_params_body_instance = AssignClusterToTenantParamsBody.from_json(json)
# print the JSON string representation of the object
print(AssignClusterToTenantParamsBody.to_json())

# convert the object into a dict
assign_cluster_to_tenant_params_body_dict = assign_cluster_to_tenant_params_body_instance.to_dict()
# create an instance of AssignClusterToTenantParamsBody from a dict
assign_cluster_to_tenant_params_body_from_dict = AssignClusterToTenantParamsBody.from_dict(assign_cluster_to_tenant_params_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


