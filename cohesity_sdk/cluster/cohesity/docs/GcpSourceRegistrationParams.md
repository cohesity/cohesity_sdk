# GcpSourceRegistrationParams

Specifies the paramaters to register a GCP source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | GCP project ID where the resources are located. | 
**subnet** | **str** | Name of the subnet within the VPC. | 
**vpc** | **str** | Name of the VPC to be used. | 
**service_account_email** | **str** | Service account email. | [optional] 
**service_account_key** | **str** | Service account key content. | [optional] 
**use_cases** | **[str], none_type** | The use cases for which the source is to be registered. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


