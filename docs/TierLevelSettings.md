# TierLevelSettings

Specifies the settings tier levels configured with each archival target. The tier settings need to be applied in specific order and default tier should always be passed as first entry in tiers array. The following example illustrates how to configure tiering input for AWS tiering. Same type of input structure applied to other cloud platforms also. <br>If user wants to achieve following tiering for backup, <br>User Desired Tiering- <br><t>1.Archive Full back up for 12 Months <br><t>2.Tier Levels <br><t><t>[1,12] [ <br><t><t><t>s3 (1 to 2 months), (default tier) <br><t><t><t>s3 Intelligent tiering (3 to 6 months), <br><t><t><t>s3 One Zone (7 to 9 months) <br><t><t><t>Glacier (10 to 12 months)] <br><t>API Input <br><t><t>1.tiers-[ <br><t><t><t>{'tierType': 'S3','moveAfterUnit':'months', <br><t><t><t>'moveAfter':2 - move from s3 to s3Inte after 2 months}, <br><t><t><t>{'tierType': 'S3Inte','moveAfterUnit':'months', <br><t><t><t>'moveAfter':4 - move from S3Inte to Glacier after 4 months}, <br><t><t><t>{'tierType': 'Glacier', 'moveAfterUnit':'months', <br><t><t><t>'moveAfter': 3 - move from Glacier to S3 One Zone after 3 months }, <br><t><t><t>{'tierType': 'S3 One Zone', 'moveAfterUnit': nil, <br><t><t><t>'moveAfter': nil - For the last record, 'moveAfter' and 'moveAfterUnit' <br><t><t><t>will be ignored since there are no further tier for data movement } <br><t><t><t>}]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_tiering** | [**AWSTiers**](AWSTiers.md) |  | [optional] 
**azure_tiering** | [**AzureTiers**](AzureTiers.md) |  | [optional] 
**cloud_platform** | **str** | Specifies the cloud platform to enable tiering. | 
**google_tiering** | [**GoogleTiers**](GoogleTiers.md) |  | [optional] 
**oracle_tiering** | [**OracleTiers**](OracleTiers.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.tier_level_settings import TierLevelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TierLevelSettings from a JSON string
tier_level_settings_instance = TierLevelSettings.from_json(json)
# print the JSON string representation of the object
print(TierLevelSettings.to_json())

# convert the object into a dict
tier_level_settings_dict = tier_level_settings_instance.to_dict()
# create an instance of TierLevelSettings from a dict
tier_level_settings_from_dict = TierLevelSettings.from_dict(tier_level_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


