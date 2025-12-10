# ClusterStateParams

Specifies the current cluster state details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**name** | **str** | Specifies the name of the cluster. | [optional] 
**operations** | **List[str]** | Specifies the operations running on the cluster. * &#x60;None&#x60; indicates that there are no operations currently running on the cluster. * &#x60;Destroy&#x60; indicates that the cluster is currently being destroyed. * &#x60;Clean&#x60; indicates that the cluster is being cleaned. * &#x60;NodeRemoval&#x60; indicates that a node is being removed from the cluster. * &#x60;DiskRemoval&#x60; indicates that a disk is being removed from the cluster. * &#x60;DiskAddition&#x60; indicates that a disk is being added tos the cluster. * &#x60;Upgrade&#x60; indicates to upgrade the software on the cluster. * &#x60;ApplyPatch&#x60; indicates to apply the patch. * &#x60;RevertPatch&#x60; indicates to revert the patch. * &#x60;BaseOSUpgrade&#x60; indicates that the BaseOSUpgrade operation on the cluster is set. * &#x60;ServiceRestart&#x60; indicates that the services on the Cluster are currently being restarted. * &#x60;SystemServiceRestart&#39; indicates that system services on the Cluster are currently being restarted.  | [optional] 
**software_version** | **str** | Specifies the software version of the cluster. | [optional] 
**system_apps** | [**List[SystemAppStatusParams]**](SystemAppStatusParams.md) | Specifies the details of each system app state on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_state_params import ClusterStateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStateParams from a JSON string
cluster_state_params_instance = ClusterStateParams.from_json(json)
# print the JSON string representation of the object
print(ClusterStateParams.to_json())

# convert the object into a dict
cluster_state_params_dict = cluster_state_params_instance.to_dict()
# create an instance of ClusterStateParams from a dict
cluster_state_params_from_dict = ClusterStateParams.from_dict(cluster_state_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


