# UpgradeLog

Specifies the log of an upgrade.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **str** | One log statement of the complete logs. | [optional] 
**time_stamp** | **int** | Time at which this log got generated. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_log import UpgradeLog

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeLog from a JSON string
upgrade_log_instance = UpgradeLog.from_json(json)
# print the JSON string representation of the object
print(UpgradeLog.to_json())

# convert the object into a dict
upgrade_log_dict = upgrade_log_instance.to_dict()
# create an instance of UpgradeLog from a dict
upgrade_log_from_dict = UpgradeLog.from_dict(upgrade_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


