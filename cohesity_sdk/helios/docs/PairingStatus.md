# PairingStatus

Defines the pairing status of the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Pairing message for the cluster in that region. | [optional] 
**status** | **str** | Pairing status for the cluster in that region | [optional] 

## Example

```python
from cohesity_sdk.helios.models.pairing_status import PairingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PairingStatus from a JSON string
pairing_status_instance = PairingStatus.from_json(json)
# print the JSON string representation of the object
print(PairingStatus.to_json())

# convert the object into a dict
pairing_status_dict = pairing_status_instance.to_dict()
# create an instance of PairingStatus from a dict
pairing_status_from_dict = PairingStatus.from_dict(pairing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


