# ClusterOperationStatus

Specifies the cluster operation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[ClusterOperationAttribute]**](ClusterOperationAttribute.md) | Specifies the attributes of the operation to provide more context for the operation. For example: Use name &#39;kPackageNameAttribute&#39; and value &#39;7.0.1-p1-2023Jul04-cc6d7c5f&#39; to indicate package being installed when operation type involves installation of package such as &#39;Upgrade&#39; or &#39;Patch&#39;. Attribute list will differ based on the type of operation.  | [optional] 
**cluster_id** | **int** | Specifies the ID of the cluster. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the incarnation id of the cluster. | [optional] 
**error_message** | **str** | Specifies the error message for the operation. | 
**events** | [**List[OperationEvents]**](OperationEvents.md) | Specifies the list of events that took place during the operation.  | [optional] 
**finish_time_seconds** | **int** | Specifies unix epoch finish time of operation. | [optional] 
**nodes_assessment_results** | [**List[NodeAssessmentResults]**](NodeAssessmentResults.md) | Specifies the result of running assessment on the cluster nodes. | [optional] 
**nodes_operation_status** | [**List[ClusterNodeOperationStatus]**](ClusterNodeOperationStatus.md) | Specifies the status of operation on the cluster nodes. | [optional] 
**operation_id** | **str** | Specifies the operation Id of cluster operation.  | [optional] 
**operation_type** | **str** | Specifies the type of cluster operation. * &#x60;Destroy&#x60; indicates cluster destroy operation. * &#x60;Create&#x60; indicates cluster create operation. * &#x60;NodeAddition&#x60; indicates the operation to add nodes to the cluster. * &#x60;NodeRemoval&#x60; indicates a node removal operation. *  Operation types related to software update are detailed in   [UpdateClusterSoftware](#tag/Platform/operation/UpdateClusterSoftware).  | [optional] 
**percentage** | **int** | Specifies an approximate completion percentage for the operation.  | [optional] 
**start_time_seconds** | **int** | Specifies unix epoch start time of operation. | [optional] 
**status** | **str** | Specifies the status of the operation. * &#39;Success&#39; indicates the operation is successful. * &#39;Failed&#39; indicates the operation failed due to an error. * &#39;InProgress&#39; indicates the operation is in progress.  | [optional] 
**time_remaining_seconds** | **int** | Specifies an estimated number of seconds until the operation is complete.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_operation_status import ClusterOperationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperationStatus from a JSON string
cluster_operation_status_instance = ClusterOperationStatus.from_json(json)
# print the JSON string representation of the object
print(ClusterOperationStatus.to_json())

# convert the object into a dict
cluster_operation_status_dict = cluster_operation_status_instance.to_dict()
# create an instance of ClusterOperationStatus from a dict
cluster_operation_status_from_dict = ClusterOperationStatus.from_dict(cluster_operation_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


