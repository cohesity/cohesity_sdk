# Application

Specifies common fields required to define applications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Unique application id. | 
**operation_name** | **str, none_type** | Operation name. | [optional] 
**operation_category** | **str, none_type** | Operation category. | [optional] 
**requester** | [**UserInfo**](UserInfo.md) |  | [optional] 
**initiated_time** | **int, none_type** | Initiated time of the application request. | [optional] 
**status** | **str, none_type** | Current status of the application. | [optional] 
**expiration_period_days** | **int, none_type** | Application expiration period in days. | [optional] 
**final_decision_made_time** | **int, none_type** | Specifies the timestamp in milliseconds since the epoch when the final decision on quorum request is made. | [optional] 
**approval_count** | **int, none_type** | Number of current quorum approvals received. | [optional] 
**required_approval_count** | **int, none_type** | Total number of required quorum approval count for the application to be approved. | [optional] 
**cluster_id** | **int, none_type** | Specifies the id of the cluster. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the incarnation id of the cluster. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of the cluster. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


