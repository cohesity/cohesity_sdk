# CreateProtectedObjectsRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonEnvSpecificObjectProtectionParams424e1a68409147dfB821C23197b469fb], none_type**](CommonEnvSpecificObjectProtectionParams424e1a68409147dfB821C23197b469fb.md) | Specifies the list of objects to be protected. Multiple objects from different adapters can be provided as input. | 
**activate_remote_object_protection** | **bool, none_type** | If set to true, it will look for the remote backup of the given user and object, and activates it. Creates a new backup if the remote backup is not found. After activation, this object cannot get snapshots from remote clusters. | [optional] 
**is_paused** | **bool, none_type** | If set to true, then the object specs will be created in the paused state preventing any runs from happening until they are unpaused. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


