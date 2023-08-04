# FCICluster

Specifies the details of a Failover Cluster Instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies the unique identifier of the FCI. | [optional] 
**name** | **str, none_type** | Specifies the name of the FCI. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**resource_info** | [**AppResource**](AppResource.md) |  | [optional] 
**servers** | [**[SQLServer], none_type**](SQLServer.md) | Specifies the list of SQL servers which belongs to the given FCI.  | [optional] 
**is_selected_by_default** | **bool, none_type** | Indicates to the UI whether this FCI cluster should be selected by default | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


