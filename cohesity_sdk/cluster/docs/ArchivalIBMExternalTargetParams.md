# ArchivalIBMExternalTargetParams

Specifies the parameters for archival to IBM Cloud Object Storage(COS) external targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**IBMAuthenticationMethodsParams**](IBMAuthenticationMethodsParams.md) |  | 
**bucket_name** | **str** | Specifies bucket name of the external target. | 
**endpoint** | **str** | Specifies the complete endpoint to be used by the Cohesity cluster to access the external target. If specified, location and endpointType parameters are ignored. For example, an endpoint would look like s3.direct.us-east.cloud-object-storage.appdomain.cloud (direct endpoint) OR s3.us-east.cloud-object-storage.appdomain.cloud (public endpoint). | [optional] 
**endpoint_for_connectors** | **str** | Specifies the complete endpoint to be used by the data-source connector(s) to access the external target. If not specified, &#39;endpoint&#39; parameter is used. If &#39;endpoint&#39; parameter is also not specified, endpoint constructed by &#39;location&#39; and &#39;endpointType&#39; would be used by the data-source connector(s) to access the external target. | [optional] 
**endpoint_type** | **str** | Specifies the endpoint type to be used to access the external target. The endpoint used by the Cohesity cluster or data-source connectors is constructed using &#39;endpointType&#39; and &#39;location&#39; as follows, s3[.endpointType].[location].cloud-object-storage.appdomaincloud. Eg. s3.private.us-east.cloud-object-storage.appdomain.cloud | [optional] 
**location** | **str** | Specifies location of the external target. A location can be a geo(Ex. us-geo), region(Ex. us-east) or a datacenter site (Ex. sjc04) and is used to identify the external target endpoint. | 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. Check the documentation for details. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. Check the documentation for details. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the IBM COS external target. If set to true deduplication is done before sending data to the external target. | [optional] 
**storage_class** | **str** | Specifies the IBM COS external target storage class. | 

## Example

```python
from cohesity_sdk.cluster.models.archival_ibm_external_target_params import ArchivalIBMExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalIBMExternalTargetParams from a JSON string
archival_ibm_external_target_params_instance = ArchivalIBMExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalIBMExternalTargetParams.to_json())

# convert the object into a dict
archival_ibm_external_target_params_dict = archival_ibm_external_target_params_instance.to_dict()
# create an instance of ArchivalIBMExternalTargetParams from a dict
archival_ibm_external_target_params_from_dict = ArchivalIBMExternalTargetParams.from_dict(archival_ibm_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


