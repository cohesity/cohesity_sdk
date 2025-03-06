# ViewOptions

Specifies the parameters related to the Exchange restore of type view. All the files related to one database are cloned to a view and the view can be used by third party tools like Kroll, etc. to restore exchange databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_point** | **str** | The path of the SMB share. | [optional] 
**view_name** | **str** | The name of the view. | [optional] 
**whitelist_restore_view_for_all** | **bool** | Whether to white-list the Exchange restore view for all the IP addresses | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_options import ViewOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ViewOptions from a JSON string
view_options_instance = ViewOptions.from_json(json)
# print the JSON string representation of the object
print(ViewOptions.to_json())

# convert the object into a dict
view_options_dict = view_options_instance.to_dict()
# create an instance of ViewOptions from a dict
view_options_from_dict = ViewOptions.from_dict(view_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


