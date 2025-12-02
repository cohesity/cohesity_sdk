# GcpKmsConfigurationUpdateParams

GCP KMS configuration updatable parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impersonation_account_id** | **str** | Specifies account ID to impersonate for kms access. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_kms_configuration_update_params import GcpKmsConfigurationUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpKmsConfigurationUpdateParams from a JSON string
gcp_kms_configuration_update_params_instance = GcpKmsConfigurationUpdateParams.from_json(json)
# print the JSON string representation of the object
print(GcpKmsConfigurationUpdateParams.to_json())

# convert the object into a dict
gcp_kms_configuration_update_params_dict = gcp_kms_configuration_update_params_instance.to_dict()
# create an instance of GcpKmsConfigurationUpdateParams from a dict
gcp_kms_configuration_update_params_from_dict = GcpKmsConfigurationUpdateParams.from_dict(gcp_kms_configuration_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


