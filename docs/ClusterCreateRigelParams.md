# ClusterCreateRigelParams

Params for Rigel Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_token** | **str** | Specifies the token which will be used to claim this Cluster to Helios. | 
**nodes** | [**List[RigelClusterNode]**](RigelClusterNode.md) |  | 

## Example

```python
from cohesity_sdk.models.cluster_create_rigel_params import ClusterCreateRigelParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateRigelParams from a JSON string
cluster_create_rigel_params_instance = ClusterCreateRigelParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateRigelParams.to_json())

# convert the object into a dict
cluster_create_rigel_params_dict = cluster_create_rigel_params_instance.to_dict()
# create an instance of ClusterCreateRigelParams from a dict
cluster_create_rigel_params_from_dict = ClusterCreateRigelParams.from_dict(cluster_create_rigel_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


