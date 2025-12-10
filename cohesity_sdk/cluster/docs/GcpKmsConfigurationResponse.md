# GcpKmsConfigurationResponse

IBM KMS configuration response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impersonation_account_id** | **str** | Specifies account ID to impersonate for kms access. | [optional] 
**kms_key_url** | **str** | URL of the GCP KMS key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_kms_configuration_response import GcpKmsConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GcpKmsConfigurationResponse from a JSON string
gcp_kms_configuration_response_instance = GcpKmsConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(GcpKmsConfigurationResponse.to_json())

# convert the object into a dict
gcp_kms_configuration_response_dict = gcp_kms_configuration_response_instance.to_dict()
# create an instance of GcpKmsConfigurationResponse from a dict
gcp_kms_configuration_response_from_dict = GcpKmsConfigurationResponse.from_dict(gcp_kms_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


