# ClusterIpmiUsers

Specifies the  cluster level IPMI user name and the list of node level IPMI user names..

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_username** | **str** | IPMI user name at the cluster level for the cluster. | [optional] 
**node_ipmi_users** | [**List[NodeIpmiUser]**](NodeIpmiUser.md) | Specifies the ipmi user info for all the nodes in the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_ipmi_users import ClusterIpmiUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIpmiUsers from a JSON string
cluster_ipmi_users_instance = ClusterIpmiUsers.from_json(json)
# print the JSON string representation of the object
print(ClusterIpmiUsers.to_json())

# convert the object into a dict
cluster_ipmi_users_dict = cluster_ipmi_users_instance.to_dict()
# create an instance of ClusterIpmiUsers from a dict
cluster_ipmi_users_from_dict = ClusterIpmiUsers.from_dict(cluster_ipmi_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


