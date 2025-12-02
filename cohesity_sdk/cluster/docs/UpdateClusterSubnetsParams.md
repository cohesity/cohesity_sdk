# UpdateClusterSubnetsParams

Specifies the params for update cluster subnets request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_subnets** | [**List[Subnet]**](Subnet.md) | Contains the subnets to be updated | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_cluster_subnets_params import UpdateClusterSubnetsParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterSubnetsParams from a JSON string
update_cluster_subnets_params_instance = UpdateClusterSubnetsParams.from_json(json)
# print the JSON string representation of the object
print(UpdateClusterSubnetsParams.to_json())

# convert the object into a dict
update_cluster_subnets_params_dict = update_cluster_subnets_params_instance.to_dict()
# create an instance of UpdateClusterSubnetsParams from a dict
update_cluster_subnets_params_from_dict = UpdateClusterSubnetsParams.from_dict(update_cluster_subnets_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


