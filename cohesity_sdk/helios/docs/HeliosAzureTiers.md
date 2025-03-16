# HeliosAzureTiers

Specifies Azure tiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tiers** | [**List[HeliosAzureTier]**](HeliosAzureTier.md) | Specifies the tiers that are used to move the archived backup from current tier to next tier. The order of the tiers determines which tier will be used next for moving the archived backup. The first tier input should always be default tier where backup will be acrhived. Each tier specifies how much time after the backup will be moved to next tier from the current tier. | 

## Example

```python
from cohesity_sdk.helios.models.helios_azure_tiers import HeliosAzureTiers

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAzureTiers from a JSON string
helios_azure_tiers_instance = HeliosAzureTiers.from_json(json)
# print the JSON string representation of the object
print(HeliosAzureTiers.to_json())

# convert the object into a dict
helios_azure_tiers_dict = helios_azure_tiers_instance.to_dict()
# create an instance of HeliosAzureTiers from a dict
helios_azure_tiers_from_dict = HeliosAzureTiers.from_dict(helios_azure_tiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


