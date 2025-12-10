# IbmKmsConfiguration

IBM KMS configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**AuthenticationMethod**](AuthenticationMethod.md) |  | [optional] 
**endpoint_url** | **str** | Specifies the Key protect or HPCS endpoint URL. | [optional] 
**instance_id** | **str** | Specifies the unique IBM cloud instance ID. | [optional] 
**kms_key_crn** | **str** | CRN of the root key. | [optional] 
**kms_key_ring** | **str** | Specifies ID fo the key ring the specified key is a part of. | [optional] 
**kms_type** | **str** | Specifies the IBM KMS type used - Key Protect or HPCS. | [optional] 
**region** | **str** | Specifies the region abbreviation where the Key Protect instance resides. | [optional] 
**root_key_id** | **str** | Specifies the unique identifier for the root key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ibm_kms_configuration import IbmKmsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IbmKmsConfiguration from a JSON string
ibm_kms_configuration_instance = IbmKmsConfiguration.from_json(json)
# print the JSON string representation of the object
print(IbmKmsConfiguration.to_json())

# convert the object into a dict
ibm_kms_configuration_dict = ibm_kms_configuration_instance.to_dict()
# create an instance of IbmKmsConfiguration from a dict
ibm_kms_configuration_from_dict = IbmKmsConfiguration.from_dict(ibm_kms_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


