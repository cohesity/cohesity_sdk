# UpgradeLogsResponse

\"Response containing upgrade logs for services.\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helios_upgrade_status** | **str** | \&quot;The overall upgrade status\&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 
**helios_upgrade_version** | **str** | Helios upgrade version. | [optional] 
**services** | [**List[ServiceUpgradeLog]**](ServiceUpgradeLog.md) | List of service upgrade logs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.upgrade_logs_response import UpgradeLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeLogsResponse from a JSON string
upgrade_logs_response_instance = UpgradeLogsResponse.from_json(json)
# print the JSON string representation of the object
print(UpgradeLogsResponse.to_json())

# convert the object into a dict
upgrade_logs_response_dict = upgrade_logs_response_instance.to_dict()
# create an instance of UpgradeLogsResponse from a dict
upgrade_logs_response_from_dict = UpgradeLogsResponse.from_dict(upgrade_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


