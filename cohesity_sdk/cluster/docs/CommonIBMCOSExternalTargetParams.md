# CommonIBMCOSExternalTargetParams

Specifies the common parameters for IBM COS external targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**IBMAuthenticationMethodsParams**](IBMAuthenticationMethodsParams.md) |  | 
**bucket_name** | **str, none_type** | Specifies bucket name of the external target. | 
**location** | **str, none_type** | Specifies location of the external target. A location can be a geo(Ex. us-geo), region(Ex. us-east) or a datacenter site (Ex. sjc04) and is used to identify the external target endpoint. | 
**endpoint** | **str, none_type** | Specifies the complete endpoint to be used by the Cohesity cluster to access the external target. If specified, location and endpointType parameters are ignored. For example, an endpoint would look like s3.direct.us-east.cloud-object-storage.appdomain.cloud (direct endpoint) OR s3.us-east.cloud-object-storage.appdomain.cloud (public endpoint). | [optional] 
**endpoint_for_connectors** | **str, none_type** | Specifies the complete endpoint to be used by the data-source connector(s) to access the external target. If not specified, &#39;endpoint&#39; parameter is used. If &#39;endpoint&#39; parameter is also not specified, endpoint constructed by &#39;location&#39; and &#39;endpointType&#39; would be used by the data-source connector(s) to access the external target. | [optional] 
**endpoint_type** | **str, none_type** | Specifies the endpoint type to be used to access the external target. The endpoint used by the Cohesity cluster or data-source connectors is constructed using &#39;endpointType&#39; and &#39;location&#39; as follows, s3[.endpointType].[location].cloud-object-storage.appdomaincloud. Eg. s3.private.us-east.cloud-object-storage.appdomain.cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


