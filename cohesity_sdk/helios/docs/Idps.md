# Idps

Identity Providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idps** | [**List[Idp]**](Idp.md) | Specifies the list of Idps. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.idps import Idps

# TODO update the JSON string below
json = "{}"
# create an instance of Idps from a JSON string
idps_instance = Idps.from_json(json)
# print the JSON string representation of the object
print(Idps.to_json())

# convert the object into a dict
idps_dict = idps_instance.to_dict()
# create an instance of Idps from a dict
idps_from_dict = Idps.from_dict(idps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


