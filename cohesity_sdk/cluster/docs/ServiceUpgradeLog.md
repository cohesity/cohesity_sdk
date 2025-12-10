# ServiceUpgradeLog

Upgrade Logs for a Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Messages related to the upgrade. | [optional] 
**service_name** | **str** | The name of the service. | [optional] 
**service_upgrade_status** | **str** | \&quot;The upgrade status of services\&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_upgrade_log import ServiceUpgradeLog

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUpgradeLog from a JSON string
service_upgrade_log_instance = ServiceUpgradeLog.from_json(json)
# print the JSON string representation of the object
print(ServiceUpgradeLog.to_json())

# convert the object into a dict
service_upgrade_log_dict = service_upgrade_log_instance.to_dict()
# create an instance of ServiceUpgradeLog from a dict
service_upgrade_log_from_dict = ServiceUpgradeLog.from_dict(service_upgrade_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


