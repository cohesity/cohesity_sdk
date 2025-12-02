# IbmIAMCServiceMetadata

Specifies the service configuration for IAM service in IBM cloud.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Specifies the fully qulified domain name along with the protocol information. If this value is not provided in the request, then we will set this to default value as &#39;https://iam.cloud.ibm.com&#39; | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_iamc_service_metadata import IbmIAMCServiceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IbmIAMCServiceMetadata from a JSON string
ibm_iamc_service_metadata_instance = IbmIAMCServiceMetadata.from_json(json)
# print the JSON string representation of the object
print(IbmIAMCServiceMetadata.to_json())

# convert the object into a dict
ibm_iamc_service_metadata_dict = ibm_iamc_service_metadata_instance.to_dict()
# create an instance of IbmIAMCServiceMetadata from a dict
ibm_iamc_service_metadata_from_dict = IbmIAMCServiceMetadata.from_dict(ibm_iamc_service_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


