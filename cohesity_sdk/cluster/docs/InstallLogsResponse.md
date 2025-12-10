# InstallLogsResponse

\"Response containing install logs for services.\" 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helios_install_status** | **str** | \&quot;The overall install status \&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 
**helios_install_version** | **str** | Helios install version. | [optional] 
**helios_restore_status** | **str** | \&quot;The overall restore status \&quot; \&quot;(e.g., Success, InProgress, Failed, Pending, NotApplicable).\&quot;  | [optional] 
**services** | [**List[ServiceInstallLog]**](ServiceInstallLog.md) | List of service install logs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.install_logs_response import InstallLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstallLogsResponse from a JSON string
install_logs_response_instance = InstallLogsResponse.from_json(json)
# print the JSON string representation of the object
print(InstallLogsResponse.to_json())

# convert the object into a dict
install_logs_response_dict = install_logs_response_instance.to_dict()
# create an instance of InstallLogsResponse from a dict
install_logs_response_from_dict = InstallLogsResponse.from_dict(install_logs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


