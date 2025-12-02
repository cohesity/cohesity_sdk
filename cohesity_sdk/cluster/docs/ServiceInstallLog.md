# ServiceInstallLog

Install Logs for a Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Install message. | [optional] 
**service_install_status** | **str** | \&quot;The install status of services\&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 
**service_name** | **str** | The name of the service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_install_log import ServiceInstallLog

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInstallLog from a JSON string
service_install_log_instance = ServiceInstallLog.from_json(json)
# print the JSON string representation of the object
print(ServiceInstallLog.to_json())

# convert the object into a dict
service_install_log_dict = service_install_log_instance.to_dict()
# create an instance of ServiceInstallLog from a dict
service_install_log_from_dict = ServiceInstallLog.from_dict(service_install_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


