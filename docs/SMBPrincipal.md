# SMBPrincipal

Specifies principal parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Specifies the domain of the principal. For active directories, this is the fully qualified domain name (FQDN). | [optional] 
**name** | **str** | Specifies the principal name. | [optional] 
**object_class** | **str** | Specifies the principal class. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.smb_principal import SMBPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of SMBPrincipal from a JSON string
smb_principal_instance = SMBPrincipal.from_json(json)
# print the JSON string representation of the object
print(SMBPrincipal.to_json())

# convert the object into a dict
smb_principal_dict = smb_principal_instance.to_dict()
# create an instance of SMBPrincipal from a dict
smb_principal_from_dict = SMBPrincipal.from_dict(smb_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


