# FortKnoxVaultInfoList

List of FortKnox vaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vaults** | [**List[RpaasRegionInfo]**](RpaasRegionInfo.md) | Specifies an FortKnox vault. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fort_knox_vault_info_list import FortKnoxVaultInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of FortKnoxVaultInfoList from a JSON string
fort_knox_vault_info_list_instance = FortKnoxVaultInfoList.from_json(json)
# print the JSON string representation of the object
print(FortKnoxVaultInfoList.to_json())

# convert the object into a dict
fort_knox_vault_info_list_dict = fort_knox_vault_info_list_instance.to_dict()
# create an instance of FortKnoxVaultInfoList from a dict
fort_knox_vault_info_list_from_dict = FortKnoxVaultInfoList.from_dict(fort_knox_vault_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


