# IbmKmsConfigurationResponse

IBM KMS configuration response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**AuthenticationMethod**](AuthenticationMethod.md) |  | [optional] 
**kms_key_crn** | **str** | CRN of the root key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_kms_configuration_response import IbmKmsConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IbmKmsConfigurationResponse from a JSON string
ibm_kms_configuration_response_instance = IbmKmsConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(IbmKmsConfigurationResponse.to_json())

# convert the object into a dict
ibm_kms_configuration_response_dict = ibm_kms_configuration_response_instance.to_dict()
# create an instance of IbmKmsConfigurationResponse from a dict
ibm_kms_configuration_response_from_dict = IbmKmsConfigurationResponse.from_dict(ibm_kms_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


