# HeliosTenantClusterResources

A list of Sources and Storage Domains assigned to the Tenant, grouped by Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 
**source_names** | **List[str]** | List of completely assigned Sources. | [optional] 
**source_stats** | [**List[HeliosSourceObjectsStats]**](HeliosSourceObjectsStats.md) | Number of assigned objects grouped by source names. | [optional] 
**storage_domain_names** | **List[str]** | List of assigned Storage Domains. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_tenant_cluster_resources import HeliosTenantClusterResources

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTenantClusterResources from a JSON string
helios_tenant_cluster_resources_instance = HeliosTenantClusterResources.from_json(json)
# print the JSON string representation of the object
print(HeliosTenantClusterResources.to_json())

# convert the object into a dict
helios_tenant_cluster_resources_dict = helios_tenant_cluster_resources_instance.to_dict()
# create an instance of HeliosTenantClusterResources from a dict
helios_tenant_cluster_resources_from_dict = HeliosTenantClusterResources.from_dict(helios_tenant_cluster_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


