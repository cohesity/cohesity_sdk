# CloudClusterExpandParams

Parameters to expand cloud edition cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_ips** | **List[str]** | List of IPs of the new nodes. | 

## Example

```python
from cohesity_sdk.models.cloud_cluster_expand_params import CloudClusterExpandParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloudClusterExpandParams from a JSON string
cloud_cluster_expand_params_instance = CloudClusterExpandParams.from_json(json)
# print the JSON string representation of the object
print(CloudClusterExpandParams.to_json())

# convert the object into a dict
cloud_cluster_expand_params_dict = cloud_cluster_expand_params_instance.to_dict()
# create an instance of CloudClusterExpandParams from a dict
cloud_cluster_expand_params_from_dict = CloudClusterExpandParams.from_dict(cloud_cluster_expand_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


