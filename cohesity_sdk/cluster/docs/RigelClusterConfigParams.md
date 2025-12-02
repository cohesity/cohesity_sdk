# RigelClusterConfigParams

Params for Rigel Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_token** | **str** | Specifies the token which is used to claim this Cluster to Helios. | [optional] [readonly] 
**dataplane_endpoint** | **str** | Specifies the endpoint of the dataplane cluster which is associated with this rigel. | [optional] 
**nodes** | [**List[RigelClusterNode]**](RigelClusterNode.md) | Specifies the Nodes present in this Cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.rigel_cluster_config_params import RigelClusterConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of RigelClusterConfigParams from a JSON string
rigel_cluster_config_params_instance = RigelClusterConfigParams.from_json(json)
# print the JSON string representation of the object
print(RigelClusterConfigParams.to_json())

# convert the object into a dict
rigel_cluster_config_params_dict = rigel_cluster_config_params_instance.to_dict()
# create an instance of RigelClusterConfigParams from a dict
rigel_cluster_config_params_from_dict = RigelClusterConfigParams.from_dict(rigel_cluster_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


