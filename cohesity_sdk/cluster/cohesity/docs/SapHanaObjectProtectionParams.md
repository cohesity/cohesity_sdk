# SapHanaObjectProtectionParams

Specifies the parameters that are specific to SAP HANA Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[UdaObjectProtectionObjectParams]**](UdaObjectProtectionObjectParams.md) | Specifies the objects to be included in the Object Protection. | 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams thatwill be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 8
**delta** | **str, none_type** | Specifies the incremental backup delta (incremental/differential) | [optional]  if omitted the server will use the default value of "incremental"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


