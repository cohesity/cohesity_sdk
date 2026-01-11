# IbmVPCAPIMetadata

Specifies the API configuration for individual endpoint in IBM VPC cloud service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_suffix** | **str, none_type** | Specifies the suffix of the API endpoint. The suffx part must be the unique endpoint which does not conttain the FQDN part and only containes the reamining part of URL. This value along with FQDN will be used to form a URL by internal services to communicate with IBM VPC service. Example: /instance_identity/v1/iam_token | [optional] 
**version** | **str, none_type** | Specifies the version for the above API that need to be sent from cluster to IBM VPC service. The version must be specified in YYYY-MM-DD format. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


