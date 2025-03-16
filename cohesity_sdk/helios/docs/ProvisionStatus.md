# ProvisionStatus

Defines the provision status of the object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the status message. | [optional] 
**status** | **str** | Specifies the status code. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.provision_status import ProvisionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionStatus from a JSON string
provision_status_instance = ProvisionStatus.from_json(json)
# print the JSON string representation of the object
print(ProvisionStatus.to_json())

# convert the object into a dict
provision_status_dict = provision_status_instance.to_dict()
# create an instance of ProvisionStatus from a dict
provision_status_from_dict = ProvisionStatus.from_dict(provision_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


