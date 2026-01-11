# ServiceEndpointsMetadata

Specifies the service endpoints that can be configured based on the environnment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_service_name** | **str, none_type** | Specifies the name of the IBM cloud service for which the endpoints need to be configured. Based on the provided name here, API callers must set the appropriate service metadata. | 
**iam_params** | [**IbmIAMCServiceMetadata**](IbmIAMCServiceMetadata.md) |  | [optional] 
**vpc_params** | [**IbmVPCServiceMetadata**](IbmVPCServiceMetadata.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


