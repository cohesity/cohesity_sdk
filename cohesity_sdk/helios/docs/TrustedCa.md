# TrustedCa

Specifies the basic info about CA Root Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | description of the certificate. | [optional] [readonly] 
**expiration_time_usecs** | **int** | Specifies the timestamp epoch in microseconds when this certificate will no longer be valid. | [optional] [readonly] 
**id** | **str** | Unique id for the certificate. | [optional] [readonly] 
**issued_by** | **str** | Specifies the issuer. | [optional] [readonly] 
**issued_time_usecs** | **int** | Specifies the timestamp epoch in microseconds when this certificate will start being valid. | [optional] [readonly] 
**issued_to** | **str** | Specifies whom it was issued to. | [optional] [readonly] 
**last_validated_time_usecs** | **int** | Specifies the timestamp epoch in microseconds when this certificate was last validated. | [optional] [readonly] 
**name** | **str** | Unique name for the certificate. | [optional] [readonly] 
**registration_time_usecs** | **int** | Specifies the timestamp epoch in microseconds when this certificate was registered on the cluster. | [optional] [readonly] 
**status** | **str** | Validation Status of the certificate. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.trusted_ca import TrustedCa

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCa from a JSON string
trusted_ca_instance = TrustedCa.from_json(json)
# print the JSON string representation of the object
print(TrustedCa.to_json())

# convert the object into a dict
trusted_ca_dict = trusted_ca_instance.to_dict()
# create an instance of TrustedCa from a dict
trusted_ca_from_dict = TrustedCa.from_dict(trusted_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


