# ClusterCreateCloudParams

Params for Cloud Edition Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ips** | **List[str]** |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_create_cloud_params import ClusterCreateCloudParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateCloudParams from a JSON string
cluster_create_cloud_params_instance = ClusterCreateCloudParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateCloudParams.to_json())

# convert the object into a dict
cluster_create_cloud_params_dict = cluster_create_cloud_params_instance.to_dict()
# create an instance of ClusterCreateCloudParams from a dict
cluster_create_cloud_params_from_dict = ClusterCreateCloudParams.from_dict(cluster_create_cloud_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


