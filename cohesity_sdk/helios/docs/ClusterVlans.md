# ClusterVlans

Cluster vlans.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlans** | [**List[ClusterVlanParams]**](ClusterVlanParams.md) | List of vlans. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_vlans import ClusterVlans

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVlans from a JSON string
cluster_vlans_instance = ClusterVlans.from_json(json)
# print the JSON string representation of the object
print(ClusterVlans.to_json())

# convert the object into a dict
cluster_vlans_dict = cluster_vlans_instance.to_dict()
# create an instance of ClusterVlans from a dict
cluster_vlans_from_dict = ClusterVlans.from_dict(cluster_vlans_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


