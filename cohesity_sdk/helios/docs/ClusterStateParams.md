# ClusterStateParams

Specifies the current cluster state details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**name** | **str** | Specifies the name of the cluster. | [optional] 
**operations** | **List[str]** | Specifies the operations running on the cluster. &#39;None&#39; indicates that there are no operations currently running on the cluster. &#39;Destroy&#39; indicates that the cluster is currently being destroyed. &#39;Upgrade&#39; indicates that the cluster is currently being upgraded. &#39;Clean&#39; indicates that the cluster is being cleaned. &#39;NodeRemoval&#39; indicates that a node is being removed from the cluster. &#39;DiskRemoval&#39; indicates that a disk is being removed from the cluster. &#39;DiskAddition&#39; indicates that a disk is being added tos the cluster. &#39;UploadPackageByUrl&#39; indicates that a package is being uploaded using a URL. &#39;UploadPackageAndUpgrade&#39; indicates package upload by URL and upgrade operation. &#39;BaseOSUpgrade&#39; indicates that the BaseOSUpgrade operation on the cluster is set. &#39;ServiceRestart&#39; indicates that the services on the Cluster are currently being restarted. &#39;SystemServiceRestart&#39; indicates that system services on the Cluster are currently being restarted. | [optional] 
**software_version** | **str** | Specifies the software version of the cluster. | [optional] 
**system_apps** | [**List[SystemAppStatusParams]**](SystemAppStatusParams.md) | Specifies the details of each system app state on the cluster. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_state_params import ClusterStateParams

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


