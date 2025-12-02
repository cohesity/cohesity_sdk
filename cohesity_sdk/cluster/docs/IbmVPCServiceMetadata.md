# IbmVPCServiceMetadata

Specifies the service configuration for VPC service in IBM cloud.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_configs** | [**List[IbmVPCAPIMetadata]**](IbmVPCAPIMetadata.md) | Specifies the configuration for all API URLs that needs to have custom parameter values such as &#39;version&#39;. | [optional] 
**fqdn** | **str** | Specifies the fully qulified domain name along with the protocol information. If this value is not provided in the request, then we will set this to default value as &#39;http://api.metadata.cloud.ibm.com&#39; | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_vpc_service_metadata import IbmVPCServiceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IbmVPCServiceMetadata from a JSON string
ibm_vpc_service_metadata_instance = IbmVPCServiceMetadata.from_json(json)
# print the JSON string representation of the object
print(IbmVPCServiceMetadata.to_json())

# convert the object into a dict
ibm_vpc_service_metadata_dict = ibm_vpc_service_metadata_instance.to_dict()
# create an instance of IbmVPCServiceMetadata from a dict
ibm_vpc_service_metadata_from_dict = IbmVPCServiceMetadata.from_dict(ibm_vpc_service_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


