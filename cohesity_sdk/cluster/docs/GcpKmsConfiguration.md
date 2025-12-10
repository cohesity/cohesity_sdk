# GcpKmsConfiguration

GCP KMS configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impersonation_account_id** | **str** | Specifies account ID to impersonate for kms access. | [optional] 
**kms_key_url** | **str** | URL of the GCP KMS key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_kms_configuration import GcpKmsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GcpKmsConfiguration from a JSON string
gcp_kms_configuration_instance = GcpKmsConfiguration.from_json(json)
# print the JSON string representation of the object
print(GcpKmsConfiguration.to_json())

# convert the object into a dict
gcp_kms_configuration_dict = gcp_kms_configuration_instance.to_dict()
# create an instance of GcpKmsConfiguration from a dict
gcp_kms_configuration_from_dict = GcpKmsConfiguration.from_dict(gcp_kms_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


