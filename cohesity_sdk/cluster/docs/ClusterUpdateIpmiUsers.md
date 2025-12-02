# ClusterUpdateIpmiUsers

Specifies the cluster level IPMI user name and the list of node level IPMI user names for which ipmi credentials in cluster config needs to be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ipmi_password** | **str** | Specifies the ipmi password for the cluster level ipmi username to update ipmi user credentials. | [optional] 
**cluster_ipmi_username** | **str** | Specifies the cluster level IPMI username to update ipmi user credentials. | [optional] 
**node_ipmi_passwords** | **List[str]** | Specifies the ipmi passwords corresponding to the ipmi usernames provided. | [optional] 
**node_ipmi_usernames** | **List[str]** | Specifies the ipmi usernames for the nodes for which ipmi credentials in cluster config needs to be updated. | [optional] 
**node_ips** | **List[str]** | Specifies the ip addresses for nodes in the cluster for which ipmi credentials in cluster config needs to be updated. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_update_ipmi_users import ClusterUpdateIpmiUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterUpdateIpmiUsers from a JSON string
cluster_update_ipmi_users_instance = ClusterUpdateIpmiUsers.from_json(json)
# print the JSON string representation of the object
print(ClusterUpdateIpmiUsers.to_json())

# convert the object into a dict
cluster_update_ipmi_users_dict = cluster_update_ipmi_users_instance.to_dict()
# create an instance of ClusterUpdateIpmiUsers from a dict
cluster_update_ipmi_users_from_dict = ClusterUpdateIpmiUsers.from_dict(cluster_update_ipmi_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


