# RemoteAdapterHost

Specifies params of the remote host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_type** | **str** | Specifies the Operating system type of the host. | [optional] 
**hostname** | **str** | Specifies the Hostname or IP address of the host where the pre and post script will be run. | [optional] 
**username** | **str** | Specifies the username for the host. | [optional] 
**full_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**incremental_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**log_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.remote_adapter_host import RemoteAdapterHost

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteAdapterHost from a JSON string
remote_adapter_host_instance = RemoteAdapterHost.from_json(json)
# print the JSON string representation of the object
print(RemoteAdapterHost.to_json())

# convert the object into a dict
remote_adapter_host_dict = remote_adapter_host_instance.to_dict()
# create an instance of RemoteAdapterHost from a dict
remote_adapter_host_from_dict = RemoteAdapterHost.from_dict(remote_adapter_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


