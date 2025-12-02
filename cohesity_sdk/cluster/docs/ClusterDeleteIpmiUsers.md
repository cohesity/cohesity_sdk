# ClusterDeleteIpmiUsers

Specifies the cluster level IPMI user name and the list of node level IPMI user names for which ipmi credentials in cluster config needs to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_username** | **str** | Specifies the cluster level IPMI username to be deleted from cluster config. | [optional] 
**node_ipmi_usernames** | **List[str]** | Specifies the ipmi usernames for the nodes for which ipmi credentials in cluster config needs to be deleted. | [optional] 
**node_ips** | **List[str]** | Specifies the ip addresses for nodes in the cluster for which ipmi credentials in cluster config needs to be deleted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_delete_ipmi_users import ClusterDeleteIpmiUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDeleteIpmiUsers from a JSON string
cluster_delete_ipmi_users_instance = ClusterDeleteIpmiUsers.from_json(json)
# print the JSON string representation of the object
print(ClusterDeleteIpmiUsers.to_json())

# convert the object into a dict
cluster_delete_ipmi_users_dict = cluster_delete_ipmi_users_instance.to_dict()
# create an instance of ClusterDeleteIpmiUsers from a dict
cluster_delete_ipmi_users_from_dict = ClusterDeleteIpmiUsers.from_dict(cluster_delete_ipmi_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


