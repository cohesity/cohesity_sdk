# LSUAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the LSU. | [optional] [readonly] 
**remote_lsu_source** | [**[RemoteLSU], none_type**](RemoteLSU.md) | Specifies list of remote LSUs that serve as data sources for transfer operations. This list is populated during remote LSU pairing process, and is applicable only when the LSU is associated with a View Box. The list will only contain one object for a given remote cluster Id &amp; remote LSU Id pair. | [optional] [readonly] 
**remote_lsu_target** | [**[RemoteLSU], none_type**](RemoteLSU.md) | Specifies list of remote LSUs that serve as data targets for transfer operations. This list is populated during remote LSU pairing process, and is applicable only when the LSU is associated with a View Box. The list will only contain one object for a given remote cluster Id &amp; remote LSU Id pair. | [optional] [readonly] 
**tenant_ids** | **[str], none_type** | Specifies a list of tenant ids that the LSU belongs to. This property is derived from the Storage Domain this LSU is associated with. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


