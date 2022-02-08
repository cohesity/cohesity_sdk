# CommonDataTieringTaskParamsc9d6faa4Feda477aAffa033c21f67ca0

Specifies the data tiering task details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the data tiering task. | 
**type** | **str, none_type** | Type of data tiering task. &#39;Downtier&#39; indicates downtiering task. &#39;Uptier&#39; indicates uptiering task. | 
**description** | **str, none_type** | Specifies a description of the data tiering task. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**source** | [**DataTieringSource**](DataTieringSource.md) |  | [optional] 
**target** | [**DataTieringTarget**](DataTieringTarget.md) |  | [optional] 
**schedule** | [**DataTieringSchedule**](DataTieringSchedule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


