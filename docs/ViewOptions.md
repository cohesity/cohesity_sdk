# ViewOptions

Specifies the parameters related to the Exchange restore of type view. All the files related to one database are cloned to a view and the view can be used by third party tools like Kroll, etc. to restore exchange databases.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist_restore_view_for_all** | **bool, none_type** | Whether to white-list the Exchange restore view for all the IP addresses | [optional] 
**view_name** | **str, none_type** | The name of the view. | [optional] 
**mount_point** | **str, none_type** | The path of the SMB share. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


