# SapHanaProtectionGroupParams

Specifies parameters related to the SAP HANA Protection job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **str** | Specifies the incremental backup delta (incremental/differential) | 
**objects** | [**[UdaProtectionGroupObjectParams]**](UdaProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | 
**source_id** | **int, none_type** | Specifies the source Id of the objects to be protected. | 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 8
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


