# CreateProtectionGroupRunResponseBody

Specifies the response for create a protection run. On success, the system will accept the request and return the Protection Group id for which the run is supposed to start. The actual run may start at a later time if the system is busy. Consumers must query the Protection Group to see the run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str, none_type** | Specifies id of the Protection Group which must be polled for seeing the new run. | [optional] 
**uda_params** | [**UdaCreateRunResponseParams**](UdaCreateRunResponseParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


