# RequestInfo

Specifies common fields required to create an application.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Cluster ID for this request. | [optional] 
**key_info** | **str, none_type** | Additional key info about the quorum request in addition to http params and operation ID. | [optional] 
**description** | **str, none_type** | Human readable description about the quorum request which is displayed to approver to help differentiate between different quorum requests. | [optional] 
**http_params** | [**HttpParams**](HttpParams.md) |  | [optional] 
**operation_id** | **str, none_type** | If specified, this field will be used as unique identifier of operation instead of http endpoint + action. | [optional] 
**allow_multiple_pending_requests** | **bool, none_type** | If true, Quorum service should allow multiple pending quorum requests per operation. It is false by default. | [optional] 
**pre_value** | **str, none_type** | Previous value for this application info. | [optional] 
**new_value** | **str, none_type** | New value for this application info. | [optional] 
**auth_token** | **str, none_type** | Authentication token to be passed back when replaying the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


