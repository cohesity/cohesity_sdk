# ClusterStateParams

Specifies the current cluster state details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**name** | **str** | Specifies the name of the cluster. | [optional] 
**software_version** | **str** | Specifies the software version of the cluster. | [optional] 
**operations** | **[str]** | Specifies the operations running on the cluster. &#39;Destroy&#39; indicates that the cluster is currently being destroyed. &#39;Upgrade&#39; indicates that the cluster is currently being upgraded. &#39;Clean&#39; indicates that the cluster is being cleaned. &#39;NodeRemoval&#39; indicates that a node is being removed from the cluster. &#39;DiskRemoval&#39; indicates that a disk is being removed from the cluster. &#39;DiskAddition&#39; indicates that a disk is being added tos the cluster. &#39;UploadPackageByUrl&#39; indicates that a package is being uploaded using a URL. &#39;UploadPackageAndUpgrade&#39; indicates package upload by URL and upgrade operation. | [optional] 
**system_apps** | [**[SystemAppStatusParams]**](SystemAppStatusParams.md) | Specifies the details of each system app state on the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


