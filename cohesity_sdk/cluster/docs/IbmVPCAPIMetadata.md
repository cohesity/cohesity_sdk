# IbmVPCAPIMetadata

Specifies the API configuration for individual endpoint in IBM VPC cloud service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_suffix** | **str** | Specifies the suffix of the API endpoint. The suffx part must be the unique endpoint which does not conttain the FQDN part and only containes the reamining part of URL. This value along with FQDN will be used to form a URL by internal services to communicate with IBM VPC service. Example: /instance_identity/v1/iam_token | [optional] 
**version** | **str** | Specifies the version for the above API that need to be sent from cluster to IBM VPC service. The version must be specified in YYYY-MM-DD format. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_vpcapi_metadata import IbmVPCAPIMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IbmVPCAPIMetadata from a JSON string
ibm_vpcapi_metadata_instance = IbmVPCAPIMetadata.from_json(json)
# print the JSON string representation of the object
print(IbmVPCAPIMetadata.to_json())

# convert the object into a dict
ibm_vpcapi_metadata_dict = ibm_vpcapi_metadata_instance.to_dict()
# create an instance of IbmVPCAPIMetadata from a dict
ibm_vpcapi_metadata_from_dict = IbmVPCAPIMetadata.from_dict(ibm_vpcapi_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


