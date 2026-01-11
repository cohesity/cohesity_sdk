# ArchivalIBMExternalTargetParams

Specifies the parameters for archival to IBM Cloud Object Storage(COS) external targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**IBMAuthenticationMethodsParams**](IBMAuthenticationMethodsParams.md) |  | 
**bucket_name** | **str, none_type** | Specifies bucket name of the external target. | 
**location** | **str, none_type** | Specifies location of the external target. A location can be a geo(Ex. us-geo), region(Ex. us-east) or a datacenter site (Ex. sjc04) and is used to identify the external target endpoint. | 
**storage_class** | **str, none_type** | Specifies the IBM COS external target storage class. | 
**endpoint** | **str, none_type** | Specifies the complete endpoint to be used by the Cohesity cluster to access the external target. If specified, location and endpointType parameters are ignored. For example, an endpoint would look like s3.direct.us-east.cloud-object-storage.appdomain.cloud (direct endpoint) OR s3.us-east.cloud-object-storage.appdomain.cloud (public endpoint). | [optional] 
**endpoint_for_connectors** | **str, none_type** | Specifies the complete endpoint to be used by the data-source connector(s) to access the external target. If not specified, &#39;endpoint&#39; parameter is used. If &#39;endpoint&#39; parameter is also not specified, endpoint constructed by &#39;location&#39; and &#39;endpointType&#39; would be used by the data-source connector(s) to access the external target. | [optional] 
**endpoint_type** | **str, none_type** | Specifies the endpoint type to be used to access the external target. The endpoint used by the Cohesity cluster or data-source connectors is constructed using &#39;endpointType&#39; and &#39;location&#39; as follows, s3[.endpointType].[location].cloud-object-storage.appdomaincloud. Eg. s3.private.us-east.cloud-object-storage.appdomain.cloud | [optional] 
**is_forever_incremental_archival_enabled** | **bool, none_type** | Specifies if Forever Incremental Archival setting is enabled or not. Check the documentation for details. | [optional] 
**is_incremental_archival_enabled** | **bool, none_type** | Specifies if Incremental Archival setting is enabled or not. Check the documentation for details. | [optional] 
**source_side_deduplication** | **bool, none_type** | Specifies the Source Side Deduplication setting for the IBM COS external target. If set to true deduplication is done before sending data to the external target. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


