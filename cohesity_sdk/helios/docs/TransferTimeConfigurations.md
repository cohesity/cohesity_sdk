# TransferTimeConfigurations

List of FortKnox vaults transfer time configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transfer_time_configs** | [**List[TransferTimeConfiguration]**](TransferTimeConfiguration.md) | List of FortKnox vaults transfer time configurations. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_configurations import TransferTimeConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeConfigurations from a JSON string
transfer_time_configurations_instance = TransferTimeConfigurations.from_json(json)
# print the JSON string representation of the object
print(TransferTimeConfigurations.to_json())

# convert the object into a dict
transfer_time_configurations_dict = transfer_time_configurations_instance.to_dict()
# create an instance of TransferTimeConfigurations from a dict
transfer_time_configurations_from_dict = TransferTimeConfigurations.from_dict(transfer_time_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


