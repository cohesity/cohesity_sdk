# SiteRestoreParam

Specifies the parameters to recover a MSGroup site document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_library_params** | [**List[OneDriveParam]**](OneDriveParam.md) | Specifies the list of document library items to recover in the MSGroup site. | 
**target_doc_lib_name** | **str** | Specifies the name for the target document library. Should be provided iff it is an alternate granular group site restore either to a different document library in the same group site or a document library in a different group site within the same M365 source. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.site_restore_param import SiteRestoreParam

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRestoreParam from a JSON string
site_restore_param_instance = SiteRestoreParam.from_json(json)
# print the JSON string representation of the object
print(SiteRestoreParam.to_json())

# convert the object into a dict
site_restore_param_dict = site_restore_param_instance.to_dict()
# create an instance of SiteRestoreParam from a dict
site_restore_param_from_dict = SiteRestoreParam.from_dict(site_restore_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


