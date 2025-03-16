# RegisterTrustedCas

Specifies the parameters to register a Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[TrustedCaRequest]**](TrustedCaRequest.md) | Specifies the certificates to be imported. | 
**only_validate** | **bool** | Specifies if the certificates are only to be validated. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.register_trusted_cas import RegisterTrustedCas

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterTrustedCas from a JSON string
register_trusted_cas_instance = RegisterTrustedCas.from_json(json)
# print the JSON string representation of the object
print(RegisterTrustedCas.to_json())

# convert the object into a dict
register_trusted_cas_dict = register_trusted_cas_instance.to_dict()
# create an instance of RegisterTrustedCas from a dict
register_trusted_cas_from_dict = RegisterTrustedCas.from_dict(register_trusted_cas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


