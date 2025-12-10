# IbmKmsConfigurationUpdateParams

IBM KMS configuration updatable parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Specify the API key. | [optional] 
**tenant_crn** | **str** | Specify the tenant CRN. | [optional] 
**trusted_profile_id** | **str** | Specify the trusted profile ID. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_kms_configuration_update_params import IbmKmsConfigurationUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of IbmKmsConfigurationUpdateParams from a JSON string
ibm_kms_configuration_update_params_instance = IbmKmsConfigurationUpdateParams.from_json(json)
# print the JSON string representation of the object
print(IbmKmsConfigurationUpdateParams.to_json())

# convert the object into a dict
ibm_kms_configuration_update_params_dict = ibm_kms_configuration_update_params_instance.to_dict()
# create an instance of IbmKmsConfigurationUpdateParams from a dict
ibm_kms_configuration_update_params_from_dict = IbmKmsConfigurationUpdateParams.from_dict(ibm_kms_configuration_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


