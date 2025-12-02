# ClusterSLAMetadata

Specifies the SLA related metadata associated with the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_sla** | **int** | Specifies the default SLA in minutes at cluster level which will be applied as default across all protection groups. This value is only used by UI to populate the default value. | [optional] 
**minimum_sla** | **int** | Specifies the minimum SLA in minutes at cluster level which will be validated against all protection groups SLA configuration. If the provided SLA at protection group creation or update is less than this value then protection group request will be invalidated. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_sla_metadata import ClusterSLAMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSLAMetadata from a JSON string
cluster_sla_metadata_instance = ClusterSLAMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterSLAMetadata.to_json())

# convert the object into a dict
cluster_sla_metadata_dict = cluster_sla_metadata_instance.to_dict()
# create an instance of ClusterSLAMetadata from a dict
cluster_sla_metadata_from_dict = ClusterSLAMetadata.from_dict(cluster_sla_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


