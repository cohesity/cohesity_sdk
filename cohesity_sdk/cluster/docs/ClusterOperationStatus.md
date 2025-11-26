# ClusterOperationStatus

Specifies cluster operation status parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**events** | [**[OperationEvents]**](OperationEvents.md) | Specifies the list of events that took place during the operation. | [optional] 
**nodes_operation_status** | [**[ClusterNodeOperationStatus]**](ClusterNodeOperationStatus.md) | Specifies the operation status of the nodes. | [optional] 
**percentage** | **int** | Specifies an approximate completion percentage for the operation. | [optional] 
**status** | **str** | Specifies the status of the operation. &#39;Success&#39; indicates the operation is successful. &#39;Failed&#39; indicates the operation failed due to an error. &#39;InProgress&#39; indicates the operation is in progress. | [optional] 
**time_remaining_seconds** | **int** | Specifies an estimated number of seconds until the operation is complete. | [optional] 
**type** | **str** | Specifies the type of cluster operation. &#39;Destroy&#39; indicates cluster destroy operation. &#39;Create&#39; indicates cluster create operation. &#39;NodeAddition&#39; indicates the operation to add nodes to the cluster. &#39;Upgrade&#39; indicates cluster upgrade operation. &#39;UploadPackageByUrl&#39; indicates the operation to upload a package by URL. &#39;UploadPackageAndUpgrade&#39; indicates the operation to upload package by URL and upgrade the cluster. &#39;NodeRemoval&#39; indicates a node removal operation. &#39;PackageRemoval&#39; indicates the operation to remove a software package from the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


