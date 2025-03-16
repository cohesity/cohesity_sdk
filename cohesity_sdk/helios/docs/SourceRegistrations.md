# SourceRegistrations

Protection Source Registrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registrations** | [**List[SourceRegistration]**](SourceRegistration.md) | Specifies the list of Protection Source Registrations. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.source_registrations import SourceRegistrations

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRegistrations from a JSON string
source_registrations_instance = SourceRegistrations.from_json(json)
# print the JSON string representation of the object
print(SourceRegistrations.to_json())

# convert the object into a dict
source_registrations_dict = source_registrations_instance.to_dict()
# create an instance of SourceRegistrations from a dict
source_registrations_from_dict = SourceRegistrations.from_dict(source_registrations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


