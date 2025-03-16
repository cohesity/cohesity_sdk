# HeliosClusterTenant

Description of a Tenant and cluster related properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**region_id** | **str** | Specifies the region id of the cluster. Only valid for DMaaS clusters. | [optional] 
**created_at_time_msecs** | **int** | Epoch time when tenant was created. | [optional] [readonly] 
**deleted_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**description** | **str** | Description about the tenant. | [optional] 
**id** | **str** | The tenant id. | [optional] 
**is_managed_on_helios** | **bool** | Flag to indicate if tenant is managed on helios | [optional] 
**last_updated_at_time_msecs** | **int** | Epoch time when tenant was last updated. | [optional] [readonly] 
**name** | **str** | Name of the Tenant. | [optional] 
**network** | [**TenantNetwork**](TenantNetwork.md) |  | [optional] 
**status** | **str** | Current Status of the Tenant. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_cluster_tenant import HeliosClusterTenant

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosClusterTenant from a JSON string
helios_cluster_tenant_instance = HeliosClusterTenant.from_json(json)
# print the JSON string representation of the object
print(HeliosClusterTenant.to_json())

# convert the object into a dict
helios_cluster_tenant_dict = helios_cluster_tenant_instance.to_dict()
# create an instance of HeliosClusterTenant from a dict
helios_cluster_tenant_from_dict = HeliosClusterTenant.from_dict(helios_cluster_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


