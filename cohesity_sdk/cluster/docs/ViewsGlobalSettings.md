# ViewsGlobalSettings

Specifies the Global Settings for SmartFiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_remote_views_gui_visibility** | **bool** | Specifies the visibility of Remote Cohesity Views on Cohesity GUI. | [optional] 
**enable_remote_views_visibility** | **bool** | Specifies the visibility of Remote Cohesity Views for external clients. | [optional] 
**enable_smb_auth** | **bool** | Specifies if SMB Authentication should be enabled. | [optional] 
**enable_smb_multi_channel** | **bool** | Specifies if SMB Multi-Channel should be enabled. | [optional] 
**s3_virtual_hosted_domain_names** | **List[str]** | Specifies the list of domain names for S3 Virtual Hosted Style Paths. If set, all the Cohesity S3 Views in the cluster can be accessed using any of the specified domain names. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.views_global_settings import ViewsGlobalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsGlobalSettings from a JSON string
views_global_settings_instance = ViewsGlobalSettings.from_json(json)
# print the JSON string representation of the object
print(ViewsGlobalSettings.to_json())

# convert the object into a dict
views_global_settings_dict = views_global_settings_instance.to_dict()
# create an instance of ViewsGlobalSettings from a dict
views_global_settings_from_dict = ViewsGlobalSettings.from_dict(views_global_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


