# GcpSourceRegistrationParams

Specifies the paramaters to register a GCP source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | GCP project ID where the resources are located. | 
**service_account_email** | **str** | Service account email. | [optional] 
**service_account_key** | **str** | Service account key content. | [optional] 
**subnet** | **str** | Name of the subnet within the VPC. | 
**use_cases** | **List[str]** | The use cases for which the source is to be registered. | [optional] 
**vpc** | **str** | Name of the VPC to be used. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_source_registration_params import GcpSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSourceRegistrationParams from a JSON string
gcp_source_registration_params_instance = GcpSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(GcpSourceRegistrationParams.to_json())

# convert the object into a dict
gcp_source_registration_params_dict = gcp_source_registration_params_instance.to_dict()
# create an instance of GcpSourceRegistrationParams from a dict
gcp_source_registration_params_from_dict = GcpSourceRegistrationParams.from_dict(gcp_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


