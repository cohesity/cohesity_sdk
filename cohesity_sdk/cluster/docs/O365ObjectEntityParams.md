# O365ObjectEntityParams

Specifies the common parameters for O365 object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_smtp_address** | **str** | Specifies the Primary SMTP Address of O365 Mailbox, User or Group Object. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.o365_object_entity_params import O365ObjectEntityParams

# TODO update the JSON string below
json = "{}"
# create an instance of O365ObjectEntityParams from a JSON string
o365_object_entity_params_instance = O365ObjectEntityParams.from_json(json)
# print the JSON string representation of the object
print(O365ObjectEntityParams.to_json())

# convert the object into a dict
o365_object_entity_params_dict = o365_object_entity_params_instance.to_dict()
# create an instance of O365ObjectEntityParams from a dict
o365_object_entity_params_from_dict = O365ObjectEntityParams.from_dict(o365_object_entity_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


