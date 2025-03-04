# ArchivalTargetTierInfo

Specifies the tier info for archival.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_tiering** | [**AWSTiers**](AWSTiers.md) |  | [optional] 
**azure_tiering** | [**AzureTiers**](AzureTiers.md) |  | [optional] 
**cloud_platform** | **str** | Specifies the cloud platform to enable tiering. | 
**google_tiering** | [**GoogleTiers**](GoogleTiers.md) |  | [optional] 
**oracle_tiering** | [**OracleTiers**](OracleTiers.md) |  | [optional] 
**current_tier_type** | **str** | Specifies the type of the current tier where the snapshot resides. This will be specified if the run is a CAD run. | [optional] 

## Example

```python
from cohesity_sdk.models.archival_target_tier_info import ArchivalTargetTierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalTargetTierInfo from a JSON string
archival_target_tier_info_instance = ArchivalTargetTierInfo.from_json(json)
# print the JSON string representation of the object
print(ArchivalTargetTierInfo.to_json())

# convert the object into a dict
archival_target_tier_info_dict = archival_target_tier_info_instance.to_dict()
# create an instance of ArchivalTargetTierInfo from a dict
archival_target_tier_info_from_dict = ArchivalTargetTierInfo.from_dict(archival_target_tier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


